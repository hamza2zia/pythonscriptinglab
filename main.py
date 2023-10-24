import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

api_token = os.getenv("API_TOKEN")
email = os.getenv("EMAIL")
api_key = os.getenv("API_KEY")
zone_id = os.getenv("ZONE_ID")


HEADERS = {
    "X-Auth-Email": email,
    "X-Auth-Key": api_key,
    "Content-Type": "application/json"
}


def set_security_level(zone_id, security_level):
    # TODO:

    # Define the URL based on the provided zone_id
    url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/settings/security_level'

    data = {
        "value" : security_level
    }


    # Send a PATCH request to the URL with the appropriate headers and security_level in JSON body
    response = requests.patch(url, json=data,headers=HEADERS)

    # Handle the response, outputting the result if successful, or the error if it fails
    if response.status_code == 200:
        print(f"Security level set to {security_level} successfully.")
    else:
        print(f"Error setting security level. Status Code: {response.status_code}")
        print("Response:", response.text)

    pass


def enable_under_attack_mode(zone_id):
    # TODO:
    # Define the URL based on the provided zone_id
    url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/settings/security_level'

    # Send a PATCH request to the URL with the appropriate headers and "I'm Under Attack" mode payload
    data = {
        "value" : security_level
    }
    response = requests.patch(url, json=data,headers=HEADERS)
    # Handle the response, outputting the result if successful, or the error if it fails
    if response.status_code == 200:
        print(f"Security level set to {security_level} successfully.")
    else:
        print(f"Error setting security level. Status Code: {response.status_code}")
        
    pass


def set_challenge_passage_time(zone_id, time_in_seconds):
    # TODO:
    # Define the URL based on the provided zone_id
    url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/settings/challenge_ttl'
    # Send a PATCH request to the URL with the appropriate headers and time_in_seconds payload

    data= {
        "value" : time_in_seconds
    }

    response = requests.patch(url, json=data,headers=HEADERS)
    # Handle the response, outputting the result if successful, or the error if it fails
    if response.status_code == 200:
        print(f"Challenge Passage Time set to {time_in_seconds} successfully.")
    else:
        print(f"Error setting Challenge passage time. Status Code: {response.status_code}")
        
    pass


if __name__ == "__main__":
    zone_id = os.getenv("ZONE_ID")
    security_level = "under_attack"
    

    # print("___________________________________________________")
    # print("setting security level")
    # set_security_level(zone_id=zone_id, security_level=security_level)
    # print("___________________________________________________")
    # print("enabling under attack mode")
    # enable_under_attack_mode(zone_id=zone_id)
    print("___________________________________________________")
    print("setting challenge passage time")
    set_challenge_passage_time(zone_id=zone_id, time_in_seconds=1800)
