from urllib.parse import urlparse


def normalize_url(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    return url.rstrip("/")


def get_domain(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc
