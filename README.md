# Wazuh Alert Automation

A Python tool that turns raw Wazuh alert JSON into a clean, structured summary, as the first stage of an automated alert-triage pipeline.

## Status

Work in progress. Step 1 of 5 is complete.

- [x] Parse an alert and extract key fields, handling missing data safely
- [ ] Check whether the source IP is public
- [ ] Look up IP reputation (AbuseIPDB)
- [ ] Apply a simple triage rule
- [ ] Send a notification (Slack/Discord) and run on live alerts from my lab

## What it does

Given a Wazuh-style alert, it extracts the rule description, rule level, agent name, and source IP. If a field is missing (for example, no source IP), it returns `None` instead of crashing.

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
