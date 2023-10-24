Lab Task 3 - Security Settings with Cloudflare's API

In this lab, you are tasked with enhancing the functionality of the main.py script by interacting with Cloudflare's security settings. You will:

1. Set the security level.
2. Enable "I'm Under Attack" mode.
3. Adjust the challenge passage time.

**Pre-requisites**: 

- Make a new branch with your name or fork the existing repository.
- Run `pip install -r requirements.txt` to install the required dependencies.

**Implementation Steps**:

1. **Setting the Security Level**:
   Define a function that sets the security level of a specific zone.
   
```python
def set_security_level(zone_id, security_level):
    # TODO:
    # Define the URL based on the provided zone_id
    # Send a PATCH request to the URL with the appropriate headers and security_level in JSON body
    # Handle the response, outputting the result if successful, or the error if it fails
    pass
```

2. **Enabling "I'm Under Attack" Mode**:
   Define a function that enables "I'm Under Attack" mode for a specific zone.
   
```python
def enable_under_attack_mode(zone_id):
    # TODO:
    # Define the URL based on the provided zone_id
    # Send a PATCH request to the URL with the appropriate headers and "I'm Under Attack" mode payload
    # Handle the response, outputting the result if successful, or the error if it fails
    pass
```

3. **Adjusting Challenge Passage Time**:
   Define a function to set the duration of the challenge page a visitor will see before they are allowed access to your site.
   
```python
def set_challenge_passage_time(zone_id, time_in_seconds):
    # TODO:
    # Define the URL based on the provided zone_id
    # Send a PATCH request to the URL with the appropriate headers and time_in_seconds payload
    # Handle the response, outputting the result if successful, or the error if it fails
    pass
```

**Guidelines**:

- For the header section, use either your API_KEY with the EMAIL or API_TOKEN to authenticate your requests.
- Understand the structure of the Cloudflare API endpoints. Refer to the Cloudflare API Documentation for more details.
- Handle different possible errors gracefully and output helpful error messages.
- Make sure your code is well-commented to explain the logic and flow of your operations, ensuring it's easier for others to understand.
- Use of wrapper libraries like `python-cloudflare` is prohibited. You must use the `requests` library to make HTTP requests.

**Submission**:

- Once you have completed the tasks, submit your `main.py` script with the completed functions.
- Ensure that all scenarios have been tested, and everything is working as expected.

Good luck and code securely! 🔒🚀
