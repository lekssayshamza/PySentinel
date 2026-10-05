import requests

from pysentinel.headers import check_security_headers
from pysentinel.utils import normalize_url


def scan_target(url):
    url = normalize_url(url)

    try:
        response = requests.get(url, timeout=5)

        print(f"Target: {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Server: {response.headers.get('Server', 'Unknown')}")
        print(f"Content-Type: {response.headers.get('Content-Type', 'Unknown')}")
        print(f"Response Size: {len(response.content)} bytes")

        print("\nSecurity Headers:")

        results = check_security_headers(response)

        for header, present in results.items():
            if present:
                print(f"[+] {header}: Present")
            else:
                print(f"[-] {header}: Missing")

    except requests.RequestException as error:
        print(f"Error: {error}")


