import requests

url = input("Enter target URL: ").strip()

if not url.startswith(("http://", "https://")):
    url = "https://" + url

print("Scanning:", url)
try:
    response = requests.get(url, timeout=10)
except requests.exceptions.Timeout:
    print("[-] ERROR: Connection timed out.")
    exit()
except requests.exceptions.ConnectionError:
    print("[-] ERROR: Could not connect to the target.")
    exit()
except requests.exceptions.RequestException:
    print("[-] ERROR: An unexpected request error occurred.")
    exit()
    if response.status_code >= 400:
        print(f"[!] WARNING: Target returned HTTP {response.status_code}")

print("Status:", response.status_code)
print("Headers:")
print(response.headers)

security_headers = {
    "Content-Security-Policy": {
    "weight": 3,
    "risk": "HIGH",
    "description": "Helps mitigate XSS and code injection attacks.",
    "recommendation": "Implement a restrictive Content-Security-Policy."
},
   "Strict-Transport-Security": {
    "weight": 3,
    "risk": "HIGH",
    "description": "Forces browsers to use secure HTTPS connections.",
    "recommendation": "Enable HSTS with an appropriate max-age value."
},
   "X-Frame-Options": {
    "weight": 2,
    "risk": "MEDIUM",
    "description": "Helps protect the website against clickjacking.",
    "recommendation": "Set X-Frame-Options to DENY or SAMEORIGIN."
},
    "X-Content-Type-Options": {
    "weight": 2,
    "risk": "MEDIUM",
    "description": "Prevents MIME-type sniffing.",
    "recommendation": "Set X-Content-Type-Options to nosniff."
},
    "Referrer-Policy": {
    "weight": 1,
    "risk": "LOW",
    "description": "Controls information sent in the Referer header.",
    "recommendation": "Configure an appropriate Referrer-Policy."
},
   "Permissions-Policy": {
    "weight": 1,
    "risk": "LOW",
    "description": "Controls access to browser features.",
    "recommendation": "Restrict unnecessary browser features."
}
}

print("\n--- SECURITY ANALYSIS ---")

score = 0
max_score = 0

for header, data in security_headers.items():
        max_score += data["weight"] 
if header in response.headers:  
        print(f"[+] {header}: PRESENT")
        score += data["weight"]
else:
        print(f"[-] {header}: MISSING")
        print(f"    Risk: {data['risk']}")
print(f"    Issue: {data['description']}")
print(f"    Recommendation: {data['recommendation']}")
percentage = (score / max_score) * 100

print("\n==============================")
print("     NULLTRACE SECURITY SCORE")
print("==============================")

print(f"Score: {score}/{max_score}")
print(f"Security: {percentage:.0f}%")
if percentage >= 80:
    risk = "LOW"
elif percentage >= 50:
    risk = "MEDIUM"
else:
    risk = "HIGH"

print(f"Risk level: {risk}")
print("==============================")