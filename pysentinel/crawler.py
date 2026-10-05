from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup


def discover_links(response):
    links = set()

    base_domain = urlparse(response.url).netloc
    soup = BeautifulSoup(response.text, "html.parser")

    for anchor in soup.find_all("a", href=True):
        url = urljoin(response.url, anchor["href"])
        parsed_url = urlparse(url)

        if parsed_url.netloc == base_domain:
            links.add(url)

    return sorted(links)
