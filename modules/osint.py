"""
osint.py - OSINT Module for EthicalHawk
"""

import logging
import requests

def run(target, config):
    results = {}
    print(f"[OSINT] Analisi per {target}")
    # Shodan
    shodan_key = config.get('shodan_api_key')
    if shodan_key:
        try:
            r = requests.get(f"https://api.shodan.io/shodan/host/{target}?key={shodan_key}", timeout=10)
            if r.status_code == 200:
                results['shodan'] = r.json()
        except Exception as e:
            logging.error(f"Shodan error: {e}")
    # Censys
    censys_id = config.get('censys_api_id')
    censys_secret = config.get('censys_api_secret')
    if censys_id and censys_secret:
        try:
            # Example call, (use official client in real code)
            r = requests.get(f"https://search.censys.io/api/v2/hosts/search?q={target}", auth=(censys_id, censys_secret), timeout=10)
            if r.status_code == 200:
                results['censys'] = r.json()
        except Exception as e:
            logging.error(f"Censys error: {e}")
    # HaveIBeenPwned
    hibp_key = config.get('hibp_api_key')
    if hibp_key:
        try:
            r = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{target}", headers={"hibp-api-key": hibp_key}, timeout=10)
            if r.status_code == 200:
                results['hibp'] = r.json()
        except Exception as e:
            logging.error(f"HIBP error: {e}")
    # ...subdomain enumeration, social media, etc. (stub)
    results['subdomains'] = ["sub1."+target, "mail."+target]
    results['whois'] = "WHOIS info here"
    results['social_media'] = {"twitter": f"https://twitter.com/{target}"}
    return results