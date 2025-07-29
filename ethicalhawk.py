#!/usr/bin/env python3
"""
EthicalHawk: Advanced Ethical Hacking, Pentesting & Bug Bounty Toolkit
CLI entrypoint.
"""
import argparse
import logging
import sys
import os
import yaml
from modules import (
    osint, pentest, cpanel_finder, http_scanner,
    tor_manager, ai_agent, exploit_generator, phishing_generator
)

# Logging setup
logging.basicConfig(
    filename="ethicalhawk.log",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

def load_config(config_path="config.yaml"):
    try:
        with open(config_path) as f:
            return yaml.safe_load(f)
    except Exception as e:
        logging.error(f"Config loading error: {e}")
        return {}

def main():
    parser = argparse.ArgumentParser(
        description="EthicalHawk: Advanced Ethical Hacking & Pentesting Toolkit"
    )
    parser.add_argument('--target', help='Target domain or IP', required=True)
    parser.add_argument('--osint', help='Run OSINT module', action='store_true')
    parser.add_argument('--owasp', help='Run OWASP vulnerability scanner', action='store_true')
    parser.add_argument('--cpanel', help='Run cPanel finder', action='store_true')
    parser.add_argument('--http', help='Run HTTP scanner', action='store_true')
    parser.add_argument('--tor', help='Route through Tor', action='store_true')
    parser.add_argument('--exploit', help='Generate exploit for detected vulns', action='store_true')
    parser.add_argument('--phishing', help='Generate phishing simulation page', action='store_true')
    parser.add_argument('--output', help='Output report file (json/csv/html)', required=False)
    parser.add_argument('--config', help='Path to config.yaml', default='config.yaml')
    parser.add_argument('--plugin', help='Run plugin module (by name)', required=False)

    args = parser.parse_args()
    config = load_config(args.config)

    # Tor integration
    if args.tor:
        tor_manager.enable_tor_proxy(config.get('tor'))

    # AI Agent main loop
    agent = ai_agent.AIAgent(
        target=args.target,
        modules={
            "osint": osint,
            "pentest": pentest,
            "cpanel_finder": cpanel_finder,
            "http_scanner": http_scanner,
            "exploit_generator": exploit_generator,
            "phishing_generator": phishing_generator
        },
        config=config,
        use_tor=args.tor
    )

    agent.run(
        use_osint=args.osint,
        use_pentest=args.owasp,
        use_cpanel=args.cpanel,
        use_http=args.http,
        use_exploit=args.exploit,
        use_phishing=args.phishing,
        output=args.output,
        plugin=args.plugin
    )

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user.")
        sys.exit(0)
    except Exception as e:
        logging.error(f"Fatal error: {e}")
        print(f"[!] Fatal error: {e}")
        sys.exit(1)