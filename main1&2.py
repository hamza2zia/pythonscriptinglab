import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_token = os.getenv('CLOUDFLARE_API_TOKEN')
 
 
 
 
 # Define headers for the API requests, including the Authorization token and the content type.
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json',
}
print(headers)

# Function to fetch user details from Cloudflare's API
def fetch_user_details():
    # Define the URL for the user details endpoint
    url = 'https://api.cloudflare.com/client/v4/user'
    # Send a GET request to the specified URL, with the defined headers
    response = requests.get(url, headers=headers)
    # Check if the response status code is 200 (OK)
    if response.ok:
        # Parse the JSON response and print it
        data = response.json()
        print(data)
    else:
        # If the response status code is not 200, print the error status code and response text
        print(f'Error: {response.status_code}')
        print(response.text)


# Function to list zones in Cloudflare's account
def list_zones():
    # Define the URL for the zones listing endpoint
    url = 'https://api.cloudflare.com/client/v4/zones'
    # Send a GET request to the specified URL, with the defined headers
    response = requests.get(url, headers=headers)
    # Check if the response status code is 200 (OK)
    if response.ok:
        # Parse the JSON response and print it
        data = response.json()
        print(data)
    else:
        # If the response status code is not 200, print the error status code and response text
        print(f'Error: {response.status_code}')
        print(response.text)


# Function to create a DNS record in a specified zone
def create_dns_record(zone_id, dns_record_data):
    # Define the URL for the DNS record creation endpoint, including the specified zone ID
    url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records'
    # Send a POST request to the specified URL, with the defined headers and JSON payload
    response = requests.post(url, headers=headers, json=dns_record_data)
    # Check if the response status code is 200 (OK)
    if response.ok:
        # Parse the JSON response and print it
        data = response.json()
        print(data)
    else:
        # If the response status code is not 200, print the error status code and response text
        print(f'Error: {response.status_code}')
        print(response.text)





def fetch_dns_records(zone_id):
    # TODO: 
    # Define the URL based on the provided zone_id
    url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records'
    # Send a GET request to the URL with the appropriate headers
    response = requests.get(url, headers=headers)
    # Handle the response, outputting the result if successful, or the error if it fails
    if response.ok:
        # Parse the JSON response and print it
        data = response.json()
        print(data)
        for record in data['result']:
            print(f"Record ID: {record['id']}, Name: {record['name']}, Type: {record['type']}, Content: {record['content']}")
    else:
        # If the response status code is not 200, print the error status code and response text
        print(f'Error: {response.status_code}')
        print(response.text)




def edit_dns_record(zone_id, record_id, record_data):
    # TODO: 
    # Define the URL based on the provided zone_id and record_id
    url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}'
    # Send a PUT request to the URL with the appropriate headers and the updated record_data as JSON
    response = requests.put(url, headers=headers, json=record_data)
    # Handle the response, outputting the result if successful, or the error if it fails
    if response.ok:
        # Parse the JSON response and print it
        data = response.json()
        print(data)
    else:
        # If the response status code is not 200, print the error status code and response text
        print(f'Error: {response.status_code}')
        print(response.text)




def delete_dns_record(zone_id, record_id):
    # TODO: 
    # Define the URL based on the provided zone_id and record_id
    url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}'
    # Send a DELETE request to the URL with the appropriate headers
    response = requests.delete(url, headers = headers)
    # Handle the response, outputting the result if successful, or the error if it fails
    if response.ok:
        # Parse the JSON response and print it
        data = response.json()
        print(data)
    else:
        # If the response status code is not 200, print the error status code and response text
        print(f'Error: {response.status_code}')
        print(response.text)





# Main execution starts here when the script is run
if __name__ == "__main__":
    # Example usage of the defined functions
    print("__________________________________________________")
    print("Fetching User Details")
    fetch_user_details()  # Fetch and print user details
    print("__________________________________________________")
    print("Listing Zones")
    list_zones()  # List and print zones

    # Create and print a new DNS record in a specified zone
    print("__________________________________________________")
    print("Creating New DNS Record in Specified Zone")
    create_dns_record('f1a0dd6e101707f2ffcfcb26ba3e054b', {
        'type': 'A',
        'name': 'example.com',
        'content': '192.0.2.1',
        'ttl': 120,
     })
    
    # Fetch DNS records
    print("__________________________________________________")
    print("Fetching DNS Records")
    fetch_dns_records('f1a0dd6e101707f2ffcfcb26ba3e054b')

    # Edit the DNS record we created earlier
    print("__________________________________________________")
    print("Editing the DNS Record Created Earlier")
    edit_dns_record('f1a0dd6e101707f2ffcfcb26ba3e054b' ,'b4f8d9c4ed6166cea45ef7d2252cf5d1', {
    'type': 'A',
    'name': 'example.com',
    'content': '203.0.113.1',  # New IP address
    'ttl': 3600,  # New TTL
    })
    
    # Delte the DNS record we created and then edited
    print("__________________________________________________")
    print("Deleting the DNS Record Created and Edited Earlier")
    delete_dns_record('f1a0dd6e101707f2ffcfcb26ba3e054b' ,'b4f8d9c4ed6166cea45ef7d2252cf5d1') 

