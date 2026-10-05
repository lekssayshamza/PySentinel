TECHNOLOGY_HEADERS = {
    "Server": "Server",
    "X-Powered-By": "X-Powered-By",
}


TECHNOLOGY_PATTERNS = {
    "WordPress": ["wp-content", "wp-includes"],
    "Laravel": ["laravel_session"],
    "Django": ["csrfmiddlewaretoken"],
    "React": ["__REACT_DEVTOOLS_GLOBAL_HOOK__"],
}


def detect_technologies(response):
    technologies = []

    for header, name in TECHNOLOGY_HEADERS.items():
        value = response.headers.get(header)

        if value:
            technologies.append(f"{name}: {value}")

    page = response.text.lower()

    for technology, patterns in TECHNOLOGY_PATTERNS.items():
        for pattern in patterns:
            if pattern.lower() in page:
                technologies.append(technology)
                break

    return technologies
