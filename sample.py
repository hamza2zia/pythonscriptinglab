import requests

url = "https://api.cloudflare.com/client/v4/zones/zone_identifier/settings/security_level"

payload = {"value": "medium"}
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer undefined"
}

response = requests.request("PATCH", url, json=payload, headers=headers)

print(response.text)


import requests

def set_security_level(api_token, zone_identifier, security_level):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_identifier}/settings/security_level"
    
    payload = {"value": security_level}
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_token}"
    }
    
    response = requests.request("PATCH", url, json=payload, headers=headers)
    
    if response.status_code == 200:
        print(f"Security level set to {security_level} successfully.")
    else:
        print(f"Error setting security level. Status Code: {response.status_code}")
        print("Response:", response.text)

# Example usage:
api_token = "your_api_token_here"
zone_identifier = "your_zone_identifier_here"
security_level = "medium"

set_security_level(api_token, zone_identifier, security_level)


