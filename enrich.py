from vt_client import vt_lookup_ip
from abuseipdb_client import abuse_lookup_ip
from otx_client import otx_lookup_ip
from utils import normalize_indicator

def enrich_ip(ip: str):
    vt_result = vt_lookup_ip(ip)
    abuse_result = abuse_lookup_ip(ip)
    otx_result = otx_lookup_ip(ip)
    enriched = normalize_indicator(ip, vt_result, abuse_result, otx_result)
    return enriched
