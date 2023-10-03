#!/usr/bin/python3
import requests
from requests.auth import HTTPBasicAuth
import json
# Define the API endpoint URL
#url = https://api.edamam.com/

# Replace 'YOUR_APP_ID' and 'YOUR_APP_KEY' with your actual credentials
app_id = '1acebed0'
app_key = '9113192b449f7d8fdc62424fb60d569b'

# Create a dictionary containing the headers with your credentials
#headers = {
#    'App-ID': app_id,      
#    'App-Key': app_key
#}

#basica=('1acebed0', '28fb9e9052c61a209ca82f95f3497e07')

# Make a GET request to the API with the headers
response = requests.get('https://api.edamam.com/api/recipes/v2', auth=(app_id, app_key)).json

#try:
#    response.json()
#except JSONDecodeError as e:
#    <handle exception>
# Check if the request was successful (status code 200)


if response.status_code == requests.codes.ok:
      api_data = _session.get(response).content
      print(api_data)
else:
    print(f"Request failed with status code: {response.status_code}")

#except Exception as e:
#print(f"An error occurred: {str(e)}")