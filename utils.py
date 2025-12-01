def normalize_indicator(indicator, vt, abuseipdb, otx):
    return {
        "indicator": indicator,
        "virustotal": vt.get("data", {}),
        "abuseipdb": abuseipdb.get("data", {}),
        "otx": otx.get("data", {}),
        "summary": {
            "vt_malicious": vt.get("data", {}).get("attributes", {}).get("last_analysis_stats", {}).get("malicious"),
            "abuse_confidence": abuseipdb.get("data", {}).get("abuseConfidenceScore"),
            "otx_pulse_count": len(otx.get("pulse_info", {}).get("pulses", [])),
        }
    }
