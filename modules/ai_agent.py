"""
ai_agent.py - AI Agent for EthicalHawk
Orchestrates modules based on logic and user context.
"""

import logging

class AIAgent:
    def __init__(self, target, modules, config, use_tor=False):
        self.target = target
        self.modules = modules
        self.config = config
        self.use_tor = use_tor
        self.results = {}

    def suggest(self, message):
        print(f"[AI Suggestion] {message}")

    def run(self, use_osint, use_pentest, use_cpanel, use_http, use_exploit, use_phishing, output, plugin):
        logging.info(f"Starting AI Agent for target {self.target}")
        # Sequential logic:
        if use_osint:
            self.suggest("Eseguo OSINT sul target...")
            self.results['osint'] = self.modules['osint'].run(self.target, self.config)
        if use_http:
            self.suggest("Scansione HTTP in corso...")
            self.results['http'] = self.modules['http_scanner'].run(self.target, self.config)
        if use_pentest:
            self.suggest("Avvio scanner OWASP Top 10...")
            self.results['owasp'] = self.modules['pentest'].run(self.target, self.config)
            # Suggerimento automatico
            if 'xss' in str(self.results['owasp']).lower():
                self.suggest("Rilevata possibile vulnerabilità XSS, vuoi generare un exploit?")
        if use_cpanel:
            self.suggest("Cerco endpoint cPanel...")
            self.results['cpanel'] = self.modules['cpanel_finder'].run(self.target, self.config)
        if use_exploit:
            self.suggest("Generazione exploit PoC per vulnerabilità rilevate...")
            self.results['exploit'] = self.modules['exploit_generator'].run(self.target, self.results, self.config)
        if use_phishing:
            self.suggest("Generazione pagina di phishing etico (solo autorizzato)...")
            self.results['phishing'] = self.modules['phishing_generator'].run(self.target, self.config)
        if plugin:
            self.suggest(f"Eseguo plugin: {plugin} ...")
            try:
                plugin_mod = __import__(f"modules.plugins.{plugin}", fromlist=['run'])
                self.results[plugin] = plugin_mod.run(self.target, self.config)
            except Exception as e:
                logging.error(f"Plugin error: {e}")
                self.suggest(f"Errore nel plugin {plugin}: {e}")

        # Save report
        if output:
            self.save_report(output)

    def save_report(self, output):
        import json, csv
        from datetime import datetime
        ext = output.split('.')[-1]
        try:
            if ext == "json":
                with open(output, "w") as f:
                    json.dump(self.results, f, indent=2)
            elif ext == "csv":
                with open(output, "w", newline='') as f:
                    writer = csv.writer(f)
                    for k, v in self.results.items():
                        writer.writerow([k, str(v)])
            elif ext == "html":
                with open(output, "w") as f:
                    f.write(f"<html><body><h1>EthicalHawk Report - {datetime.now()}</h1>")
                    for k, v in self.results.items():
                        f.write(f"<h2>{k}</h2><pre>{v}</pre>")
                    f.write("</body></html>")
            print(f"[+] Report salvato in {output}")
        except Exception as e:
            logging.error(f"Report saving error: {e}")