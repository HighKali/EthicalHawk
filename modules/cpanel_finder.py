"""
cpanel_finder.py - cPanel Finder Module for EthicalHawk
"""

import requests

def run(target, config):
    endpoints = [
        f"http://{target}:2082",
        f"https://{target}:2083",
        f"http://cpanel.{target}",
        f"https://cpanel.{target}"
    ]
    found = []
    for url in endpoints:
        try:
            r = requests.get(url, timeout=5)
            if "cPanel" in r.text or r.status_code in [200, 401, 403]:
                found.append(url)
        except:
            continue
    return {"cpanel_endpoints": found}