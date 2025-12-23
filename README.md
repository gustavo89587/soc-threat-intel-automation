🛡️ SOC Threat Intelligence Automation
Automated threat intelligence enrichment for SOC, DFIR and Threat Hunting workflows.
This project demonstrates how a modern SOC can automatically enrich alerts, reduce analyst fatigue, and improve decision-making by correlating multiple threat intelligence sources.

🚀 What This Project Does
This automation takes raw security alerts and enriches them with contextual threat intelligence from multiple sources, enabling analysts to quickly assess risk and prioritize response.
Inputs:
IP addresses
Domains
Hashes
URLs
Suspicious indicators from alerts
Outputs:
Threat reputation
Abuse confidence
Malware context
External intelligence correlation
Analyst-ready enriched output

🔗 Integrated Threat Intelligence Sources
VirusTotal API
AlienVault OTX
AbuseIPDB
Each indicator is queried across sources and consolidated into a single structured result, simulating how SOC platforms enrich alerts internally.

🧠 SOC Use Cases
This project is designed around real SOC workflows, not toy scripts.
✔ Alert enrichment before triage
✔ Faster incident prioritization
✔ Contextual decision support for analysts
✔ Threat hunting pivot enrichment
✔ DFIR investigation support
🧩 Example Workflow

SIEM / Alert Source
        ↓
Indicator Extraction
        ↓
Threat Intel APIs
        ↓
Correlation & Scoring
        ↓
Enriched Alert for Analyst
🛠️ Technologies Used
Python
REST APIs
JSON parsing & normalization
SOC enrichment logic
Modular, extensible design
📂 Project Structure

soc-threat-intel-automation/
├── intel/
│   ├── virustotal.py
│   ├── alienvault_otx.py
│   ├── abuseipdb.py
├── enrich.py
├── config.py
├── requirements.txt
└── README.md

🔍 Why This Matters for SOC Teams

Modern SOCs don’t investigate alerts blindly.
They:
Enrich first
Correlate context
Decide faster
Reduce false positives
Improve MTTR
This project reflects how real SOC teams operate.

🧪 Lab Context
This repository is part of my Okamoto Security Labs, where I simulate:
SOC alert pipelines
Incident response scenarios
Threat hunting workflows
Detection & enrichment logic
Automation for analyst efficiency

🎯 Who This Is For
SOC Analysts
Threat Hunters
DFIR Analysts
Detection Engineers
Security Engineers

📌 Next Improvements (Planned)
Risk scoring engine
SIEM integration simulation
MITRE ATT&CK mapping
Output to JSON / CSV / dashboard format
SOAR-style response hooks

👤 Author
Gustavo Okamoto
Cybersecurity Analyst | SOC / SIEM | Threat Detection & IR | Blue Team
Automation • Cloud Security • Incident Response
🔗 GitHub: https://github.com/gustavo89587
🔗 LinkedIn: https://linkedin.com/in/gustavo-okamoto-de-carvalho-ti