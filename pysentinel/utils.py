from urllib.parse import parse_qs, urlparse


def normalize_url(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    return url.rstrip("/")


def get_domain(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc


def get_parameters(url):
    parsed_url = urlparse(url)
    return parse_qs(parsed_url.query)
