import os
import requests

ABUSEIPDB_KEY = os.getenv("ABUSEIPDB_KEY")

def abuse_lookup_ip(ip):
    url = "https://api.abuseipdb.com/api/v2/check"
    params = {"ipAddress": ip, "maxAgeInDays": 90}
    headers = {"Key": ABUSEIPDB_KEY, "Accept": "application/json"}
    response = requests.get(url, headers=headers, params=params)
    return response.json()
