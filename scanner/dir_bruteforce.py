import requests
from urllib.parse import urljoin


def brute_force(url, wordlist):
    found = []

    with open(wordlist, "r") as file:
        paths = file.read().splitlines()

    for path in paths:
        target = urljoin(url, path)

        try:
            response = requests.get(target, timeout=3)

            if response.status_code in [200, 301, 302, 403]:
                print(f"[FOUND] {target}")
                found.append(target)

        except:
            pass

    return found