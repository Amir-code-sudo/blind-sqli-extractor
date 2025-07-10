# blind-sqli-extractor
🕵️‍♂️ Blind SQLi Extractor for PostgreSQL using time-based delay &amp; binary search. Designed for educational use (e.g., PortSwigger Web Security Academy labs). Extracts user passwords via TrackingId cookie. ⚠️ For legal, ethical use only.



# 🕵️ Blind SQLi (Time-Based) Extractor

A smart Python tool to extract user passwords (e.g., administrator) via **Blind SQL Injection** using **time-based delay** and **binary search**. Designed for educational purposes, especially for **PortSwigger Web Security Academy** labs.

---

## ✅ Features

- ⏱️ Exploits time-based blind SQLi (`pg_sleep()` logic)
- ⚡ Uses binary search for fast character extraction
- 🧠 Auto-detects database type (supports PostgreSQL, MySQL, MSSQL, Oracle)
- 🔐 Extracts password for any user you specify
- 🧩 Fully customizable: URL, session cookie, delay, charset
- ❌ Optional: proxy support removed for portability
- 🧪 Designed for lab/educational use only

---

## 🛠️ Usage

```bash
python binary_search_final.py


[+] Enter target URL (e.g., https://example.com/): https://target.lab/
[+] Enter the TrackingId value (before injection): abc123xyz
[+] Enter session cookie (or press Enter if none): yourSessionCookieHere
[+] Enter the username to extract password for: administrator
[+] Enter delay in seconds (default = 10): 10



💡 How it Works
This tool leverages time-based blind SQL injection to infer data without visible output. It sends conditional payloads using pg_sleep() and measures response time. Binary search drastically reduces the number of requests needed to extract each character.

⚠️ Disclaimer
This tool is for educational and authorized penetration testing purposes only.
Do not use it on systems you do not own or have explicit permission to test.
Misuse may violate laws and ethical guidelines.

📂 File Structure
binary_search_final.py — Main tool

README.md — You're reading it!


📧 Contact
If you learned something or want to improve it, feel free to fork or suggest improvements.
: amirzaher010606828@gmail.com
