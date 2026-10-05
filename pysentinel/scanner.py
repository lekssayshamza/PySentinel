import requests

from pysentinel.technologies import detect_technologies
from pysentinel.headers import check_security_headers
from pysentinel.utils import normalize_url
from pysentinel.cookies import check_cookie_security


def scan_target(url):
    url = normalize_url(url)

    try:
        response = requests.get(url, timeout=5)

        print(f"Target: {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Server: {response.headers.get('Server', 'Unknown')}")
        print(f"Content-Type: {response.headers.get('Content-Type', 'Unknown')}")
        print(f"Response Size: {len(response.content)} bytes")

        print("\nSecurity Findings:")

        findings = check_security_headers(response)

        if not findings:
            print("[+] No security header issues detected")
        else:
            for finding in findings:
                print(
                    f"[{finding['severity']}] "
                    f"{finding['name']}: "
                    f"{finding['description']}"
                )

        print("\nCookies:")

        cookies = check_cookie_security(response)

        if not cookies:
            print("[*] No cookies detected")
        else:
            for cookie in cookies:
                print(f"Cookie: {cookie['name']}")
                print(f"  Secure: {cookie['secure']}")
                print(f"  HttpOnly: {cookie['httponly']}")
                print(f"  SameSite: {cookie['samesite']}")

        print("\nTechnologies:")

        technologies = detect_technologies(response)

        if not technologies:
            print("[*] No technology information detected")
        else:
            for technology in technologies:
                print(f"[+] {technology}")

    except requests.RequestException as error:
        print(f"Error: {error}")


