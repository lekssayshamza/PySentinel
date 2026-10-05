from urllib.parse import urljoin, urlparse

import requests
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


def crawl(url, max_depth=1):
    visited = set()
    discovered = set()

    def visit(current_url, depth):
        if depth > max_depth or current_url in visited:
            return

        visited.add(current_url)

        try:
            response = requests.get(current_url, timeout=5)
        except requests.RequestException:
            return

        if depth == max_depth:
            return

        links = discover_links(response)

        for link in links:
            discovered.add(link)
            visit(link, depth + 1)

    visit(url, 0)

    return sorted(discovered)
