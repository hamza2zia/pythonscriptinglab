import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

api_token = os.getenv("API_TOKEN")
email = os.getenv("EMAIL")
api_key = os.getenv("API_KEY")

BASE_URL = "https://api.clouflare.com/client/v4/zones"
HEADERS = {
    "X-Auth-Email": "YOUR_EMAIL",
    "X-Auth-Key": "YOUR_API_KEY",
    "Content-Type": "application/json"
}


def set_security_level(zone_id, security_level):
    # TODO:
    # Define the URL based on the provided zone_id
    # Send a PATCH request to the URL with the appropriate headers and security_level in JSON body
    # Handle the response, outputting the result if successful, or the error if it fails
    pass


def enable_under_attack_mode(zone_id):
    # TODO:
    # Define the URL based on the provided zone_id
    # Send a PATCH request to the URL with the appropriate headers and "I'm Under Attack" mode payload
    # Handle the response, outputting the result if successful, or the error if it fails
    pass


def set_challenge_passage_time(zone_id, time_in_seconds):
    # TODO:
    # Define the URL based on the provided zone_id
    # Send a PATCH request to the URL with the appropriate headers and time_in_seconds payload
    # Handle the response, outputting the result if successful, or the error if it fails
    pass


if __name__ == "__main__":
    zone_id = "123"
    security_level = {}

    print("___________________________________________________")
    print("setting securiy level")
    set_security_level(zone_id=zone_id, security_level=security_level)
    print("___________________________________________________")
    print("enabling under attack mode")
    enable_under_attack_mode(zone_id=zone_id)
    print("___________________________________________________")
    print("setting challenge passage time")
    set_challenge_passage_time(zone_id=zone_id, time_in_seconds=60)
