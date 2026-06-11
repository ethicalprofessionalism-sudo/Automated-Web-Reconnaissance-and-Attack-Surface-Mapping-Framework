import requests
import re

ENDPOINT_REGEX = r'["\'](\/[a-zA-Z0-9_\-\/]+)["\']'
PARAM_REGEX = r'[?&]([a-zA-Z0-9_\-]+)='



def analyze_js(js_url):
    findings = []

    try:
        response = requests.get(js_url, timeout=5)
        content = response.text

        endpoints = re.findall(ENDPOINT_REGEX, content)
        params = re.findall(PARAM_REGEX, content)

        findings.extend(endpoints)
        findings.extend(params)

        return list(set(findings))

    except:
        return []