from http.cookies import SimpleCookie


def check_cookie_security(response):
    results = []

    responses = list(response.history) + [response]

    for current_response in responses:
        set_cookie_headers = current_response.raw.headers.getlist("Set-Cookie")

        for header in set_cookie_headers:
            cookie = SimpleCookie()
            cookie.load(header)

            for name, morsel in cookie.items():
                results.append({
                    "name": name,
                    "secure": bool(morsel["secure"]),
                    "httponly": bool(morsel["httponly"]),
                    "samesite": morsel["samesite"] or None,
                })

    return results
