import requests



def fingerprint(url):
    technologies = []

    try:
        response = requests.get(url, timeout=5)

        headers = response.headers
        html = response.text.lower()

        server = headers.get("Server")
        powered = headers.get("X-Powered-By")

        if server:
            technologies.append(server)

        if powered:
            technologies.append(powered)

        if "wp-content" in html:
            technologies.append("WordPress")

        if "react" in html:
            technologies.append("React")

        if "angular" in html:
            technologies.append("Angular")

        if "vue" in html:
            technologies.append("Vue.js")

        return list(set(technologies))

    except:
        return []