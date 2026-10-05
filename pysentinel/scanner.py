import requests
import sys

from headers import check_security_headers


def scan_target(url):
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


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <URL>")
        sys.exit(1)

    scan_target(sys.argv[1])
