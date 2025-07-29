# EthicalHawk

**EthicalHawk** è uno strumento avanzato per hacking etico, pentesting e bug bounty, con un agente AI integrato per gestire le azioni in modo logico e sequenziale.  
**⚠️ USO SOLO AUTORIZZATO!**  
Utilizza questo strumento **solo** su target di cui hai ottenuto esplicita autorizzazione.

---

## Funzionalità principali

- **OSINT**: Colleziona info tramite Shodan, Censys, HaveIBeenPwned, enumerazione sottodomini, social media.
- **Scanner OWASP**: Analisi automatizzata delle vulnerabilità Top 10 con report dettagliato.
- **cPanel Finder**: Individua endpoint cPanel in modo automatico.
- **HTTP Scanner**: Riconoscimento tecnologie, ricerca file/directory sensibili, verifica header di sicurezza.
- **Tor Integration**: Tutte le richieste possono essere instradate tramite Tor.
- **Exploit Generator**: Genera PoC per vulnerabilità rilevate, senza esecuzione automatica.
- **Phishing Generator**: Genera template HTML/PHP per simulazioni di phishing **solo etiche**.
- **AI Agent**: Gestisce la sequenza dei moduli e suggerisce azioni all'utente in tempo reale.
- **Plugin System**: Aggiungi nuovi moduli in `modules/plugins/`.

---

## Installazione


---

## 1. Prerequisiti

Assicurati di avere installato:
- Python 3.7 o superiore
- pip
- Tor
- git

Installa i pacchetti necessari (se non presenti):

```bash
sudo apt update
sudo apt install python3 python3-pip tor git
```

---

## 2. Clona il repository e accedi alla cartella

```bash
git clone <repository-url>
cd EthicalHawk
```
Sostituisci `<repository-url>` con il link del tuo repository GitHub.

---

## 3. Installa le dipendenze Python

```bash
pip3 install -r requirements.txt
```

---

## 4. Installa EthicalHawk come pacchetto

```bash
pip3 install .
```

---

## 5. Configura API Key & Tor

1. Copia e modifica il file di configurazione:
   ```bash
   cp config.yaml.example config.yaml
   nano config.yaml
   ```
2. Inserisci le tue API key (Shodan, Censys, HaveIBeenPwned, ecc.)
3. Verifica che la sezione Tor sia così:
   ```yaml
   tor:
     proxy_address: "127.0.0.1"
     proxy_port: 9050
   ```

---

## 6. Avvia il servizio Tor

```bash
sudo service tor start
# oppure
sudo systemctl start tor
```

---

## 7. Esempi di utilizzo CLI

- OSINT + OWASP + phishing via Tor, output JSON:
  ```bash
  python3 ethicalhawk.py --target example.com --osint --owasp --phishing --tor --output report.json
  ```

- Solo OSINT:
  ```bash
  python3 ethicalhawk.py --target example.com --osint
  ```

- Scansione completa e report HTML:
  ```bash
  python3 ethicalhawk.py --target example.com --osint --owasp --cpanel --http --tor --output report.html
  ```

---

## 8. Note importanti

- **Utilizza EthicalHawk solo su target autorizzati!**
- I log sono salvati in `ethicalhawk.log`
- Non condividere mai `config.yaml` o report sensibili

---

## 9. Aggiornare EthicalHawk

Per aggiornare il tool all’ultima versione:

```bash
git pull
pip3 install . --upgrade
```
