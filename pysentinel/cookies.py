from http.cookies import SimpleCookie

from pysentinel.findings import create_finding


def check_cookie_security(response):
    findings = []

    responses = list(response.history) + [response]

    for current_response in responses:
        set_cookie_headers = current_response.raw.headers.getlist("Set-Cookie")

        for header in set_cookie_headers:
            cookie = SimpleCookie()
            cookie.load(header)

            for name, morsel in cookie.items():
                if not morsel["secure"]:
                    findings.append(
                        create_finding(
                            f"Cookie: {name}",
                            "MEDIUM",
                            "Cookie is missing the Secure flag",
                            "Cookie Security",
                        )
                    )

                if not morsel["httponly"]:
                    findings.append(
                        create_finding(
                            f"Cookie: {name}",
                            "MEDIUM",
                            "Cookie is missing the HttpOnly flag",
                            "Cookie Security",
                        )
                    )

                if not morsel["samesite"]:
                    findings.append(
                        create_finding(
                            f"Cookie: {name}",
                            "LOW",
                            "Cookie is missing the SameSite attribute",
                            "Cookie Security",
                        )
                    )

    return findings
