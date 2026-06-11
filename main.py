import argparse
from scanner.crawler import crawl
from scanner.dir_bruteforce import brute_force
from scanner.js_analyzer import analyze_js
from scanner.fingerprint import fingerprint
from scanner.misconfig import check_misconfig
from scanner.reporter import save_report


def banner():
    print("=" * 50)
    print(" Automated Web Recon Framework ")
    print("=" * 50)
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", required=True)
    args = parser.parse_args()

    target = args.url

    banner()

    print("[*] Crawling target...")
    crawl_data = crawl(target)

    print("[*] Running fingerprinting...")
    tech = fingerprint(target)

    print("[*] Running directory brute force...")
    directories = brute_force(target, "wordlists/common.txt")

    print("[*] Running JavaScript analysis...")
    endpoints = []

    for js in crawl_data["js_files"]:
        endpoints.extend(analyze_js(js))

    print("[*] Checking misconfigurations...")
    findings = check_misconfig(target)

    report = {
        "target": target,
        "links": crawl_data["links"],
        "js_files": crawl_data["js_files"],
        "technologies": tech,
        "directories": directories,
        "endpoints": list(set(endpoints)),
        "misconfigurations": findings
    }

    save_report(report)

    print("[+] Scan completed")
    
if __name__ == "__main__":
    main()