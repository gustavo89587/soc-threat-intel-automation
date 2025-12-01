import os
import requests

OTX_KEY = os.getenv("OTX_KEY")

def otx_lookup_ip(ip):
    url = f"https://otx.alienvault.com/api/v1/indicators/IPv4/{ip}/general"
    headers = {"X-OTX-API-KEY": OTX_KEY}
    response = requests.get(url, headers=headers)
    return response.json()
