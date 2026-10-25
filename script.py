import json
def load_alert(path):
    with open(path, 'r') as f:
        return json.load(f)
#function to extract important information 
def extract_alert_fields(alert):
    # 1. load the alert
    fields = alert
     # 3. return the content
    return {
        "description": fields.get('rule', {}).get('description'),
        "level": fields.get('rule', {}).get('level'),
        "agent": fields.get('agent', {}).get('name'),
        "srcip": fields.get('data', {}).get('srcip'),
    }
print(extract_alert_fields(load_alert('sample_alert.json')))
print(extract_alert_fields(load_alert('sample_alert2.json')))
