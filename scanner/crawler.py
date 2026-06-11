import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def crawl(url):
    links = set()
    js_files = set()

    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        for a in soup.find_all("a", href=True):
            links.add(urljoin(url, a["href"]))

        for script in soup.find_all("script", src=True):
            js_files.add(urljoin(url, script["src"]))

        return {
            "links": list(links),
            "js_files": list(js_files)
        }

    except Exception as e:
        print(f"[ERROR] {e}")
        return {
            "links": [],
            "js_files": []
        }