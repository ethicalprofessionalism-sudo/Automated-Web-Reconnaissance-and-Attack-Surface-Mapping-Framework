import json
from datetime import datetime

def save_report(data):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    json_file = f"reports/report_{timestamp}.json"
    txt_file = f"reports/report_{timestamp}.txt"
    html_file = f"reports/report_{timestamp}.html"

    # JSON Report
    with open(json_file, "w") as f:
        json.dump(data, f, indent=4)

    # TXT Report
    with open(txt_file, "w") as f:

        f.write("WEB RECONNAISSANCE REPORT\n")
        f.write("=" * 50 + "\n\n")

        for key, value in data.items():
            f.write(f"{key.upper()}\n")
            f.write("-" * 30 + "\n")
            f.write(str(value))
            f.write("\n\n")

    # HTML Report
    html = f"""
    <html>
    <head>
        <title>Web Recon Report</title>
    </head>
    <body>

    <h1>Web Reconnaissance Report</h1>

    <h2>Target</h2>
    <p>{data['target']}</p>

    <h2>Technologies</h2>
    <ul>
    {''.join(f'<li>{t}</li>' for t in data['technologies'])}
    </ul>

    <h2>Directories</h2>
    <ul>
    {''.join(f'<li>{d}</li>' for d in data['directories'])}
    </ul>

    <h2>Endpoints</h2>
    <ul>
    {''.join(f'<li>{e}</li>' for e in data['endpoints'])}
    </ul>

    <h2>Misconfigurations</h2>
    <ul>
    {''.join(f'<li>{m}</li>' for m in data['misconfigurations'])}
    </ul>

    </body>
    </html>
    """

    with open(html_file, "w") as f:
        f.write(html)

    print(f"[+] JSON Report: {json_file}")
    print(f"[+] TXT Report : {txt_file}")
    print(f"[+] HTML Report: {html_file}")