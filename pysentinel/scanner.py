import requests

from pysentinel.sqli import check_sql_injection
from pysentinel.xss import check_reflected_xss
from pysentinel.crawler import crawl
from pysentinel.technologies import detect_technologies
from pysentinel.headers import check_security_headers
from pysentinel.utils import get_parameters, normalize_url
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

        print("\nParameters:")

        parameters = get_parameters(url)

        if not parameters:
            print("[*] No query parameters detected")
        else:
            for name, values in parameters.items():
                print(f"[+] {name}: {values}")

        print("\nXSS Findings:")

        xss_findings = check_reflected_xss(url)

        if not xss_findings:
            print("[+] No reflected XSS detected")
        else:
            for finding in xss_findings:
                print(
                    f"[{finding['severity']}] "
                    f"{finding['name']}: "
                    f"{finding['description']}"
                )

        print("\nSQL Injection Findings:")

        sqli_findings = check_sql_injection(url)

        if not sqli_findings:
            print("[+] No potential SQL injection detected")
        else:
            for finding in sqli_findings:
                print(
                    f"[{finding['severity']}] "
            	    f"{finding['name']}: "
            	    f"{finding['description']}"
                )

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

        print("\nCookie Findings:")

        cookie_findings = check_cookie_security(response)

        if not cookie_findings:
            print("[+] No cookie security issues detected")
        else:
            for finding in cookie_findings:
                print(
                     f"[{finding['severity']}] "
                     f"{finding['name']}: "
                     f"{finding['description']}"
                )

        print("\nTechnologies:")

        technologies = detect_technologies(response)

        if not technologies:
            print("[*] No technology information detected")
        else:
            for technology in technologies:
                print(f"[+] {technology}")

        print("\nDiscovered Links:")

        links = crawl(url, max_depth=1)

        if not links:
            print("[*] No internal links discovered")
        else:
            for link in links:
                print(f"[+] {link}")

    except requests.RequestException as error:
        print(f"Error: {error}")


