import requests

COMMON_FILES = [
    ".git/",
    ".env",
    "robots.txt",
    "backup.zip",
    "phpinfo.php",
    "debug"
]



def check_misconfig(url):
    findings = []

    for item in COMMON_FILES:
        target = url.rstrip("/") + "/" + item

        try:
            response = requests.get(target, timeout=3)

            if response.status_code == 200:
                findings.append(target)

        except:
            pass

    return findings