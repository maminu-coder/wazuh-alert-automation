import json
import ipaddress
def load_alert(path):
    with open(path, 'r') as f:
        return json.load(f)
#function to extract important information 
def extract_alert_fields(alert):
     # 3. return the content
    return {
        "description": alert.get('rule', {}).get('description'),
        "level": alert.get('rule', {}).get('level'),
        "agent": alert.get('agent', {}).get('name'),
        "srcip": alert.get('data', {}).get('srcip')}
    
def is_public_ip(ip):
    #determine if the given IP address is a public IP address
    try:
        ip_obj = ipaddress.ip_address(ip)
        return (ip_obj.is_global)
    
    except ValueError:
        return False
    

if __name__ == "__main__":
    '''
    This is a test function to test the extract_alert_fields and is_public_ip functions. It loads two sample alert JSON files and extracts the important information from them. It also tests the is_public_ip function with various IP addresses to check if they are public or not.
    '''
    # print(extract_alert_fields(load_alert('sample_alert.json')))
    # print(extract_alert_fields(load_alert('sample_alert2.json')))
    assert is_public_ip(None) is False
    assert is_public_ip('192.168.1.5') is False 
    assert is_public_ip('8.8.8.8') is True
    assert is_public_ip('abc') is False
    assert is_public_ip('203.0.113.45') is False
    assert is_public_ip('192.168.1.1') is False
    assert is_public_ip('100.64.0.1') is False
