# Wazuh Alert Automation

A Python tool that turns raw Wazuh alert JSON into a clean, structured summary, as the first stage of an automated alert-triage pipeline.

## Status

Work in progress. Step 1 of 5 is complete.

- [x] Parse an alert and extract key fields, handling missing data safely
- [x] Check whether the source IP is public
- [ ] Look up IP reputation (AbuseIPDB)
- [ ] Apply a simple triage rule
- [ ] Send a notification (Slack/Discord) and run on live alerts from my lab

## What it does

Given a Wazuh-style alert, it extracts the rule description, rule level, agent name, and source IP. If a field is missing (for example, no source IP), it returns `None` instead of crashing.

1. **Extracts key fields** from a Wazuh-style alert: rule description, rule level, agent name, and source IP. If a field is missing (for example, no source IP), the value is `None` instead of a crash.

2. **Checks whether the source IP is public.** Private, loopback, link-local, carrier-grade NAT, documentation-range, and invalid addresses return `False`, so later steps skip them instead of wasting lookups.

## Functions

| Function | Purpose |
|---|---|
| `load_alert(path)` | Reads an alert JSON file and returns it as a dictionary |
| `extract_alert_fields(alert)` | Takes the alert dictionary and returns `description`, `level`, `agent`, `srcip` |
| `is_public_ip(ip)` | Returns `True` only for valid, globally routable IPs |

## Example

Input (`sample_alert.json`, simplified):

```json
{
  "timestamp": "2026-10-23T17:00:00.000+0000",
  "rule": {"id": "5710", "level": 5, "description": "sshd: attempt to login using a non-existent user"},
  "agent": {"name": "ubuntu-lab"},
  "data": {"srcip": "203.0.113.45"}
}
```

Output:

```python
{'description': 'sshd: attempt to login using a non-existent user', 'level': 5, 'agent': 'ubuntu-lab', 'srcip': '203.0.113.45'}

```
## Design note

`is_public_ip` uses Python's `ipaddress` module and its `is_global` property rather than a hand-written list of excluded ranges. My first version excluded known private and reserved categories and treated everything else as public, which wrongly accepts ranges like `100.64.0.0/10` (carrier-grade NAT). Asking whether an address is globally routable is shorter and more reliable.

For an alert with no source IP (`sample_alert2.json`), `srcip` is `None`.

## Run it

```
python extract_alert.py
```

Tested with Python 3.14. No external dependencies yet.

## Notes

- Sample alerts are simplified and synthetic. The IP `203.0.113.45` is from a reserved documentation range.
- No credentials are stored in this repo. Future API keys will be read from environment variables.

## Why I'm building this

Part of my transition from cybersecurity research (IoT malware detection with deep learning) into security automation. The lab runs Wazuh on Ubuntu, with Kali and Metasploitable as attack and target machines.
