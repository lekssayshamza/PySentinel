TECHNOLOGY_HEADERS = {
    "Server": "Server",
    "X-Powered-By": "X-Powered-By",
}


def detect_technologies(response):
    technologies = []

    for header, name in TECHNOLOGY_HEADERS.items():
        value = response.headers.get(header)

        if value:
            technologies.append(f"{name}: {value}")

    return technologies
