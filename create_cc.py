#!/usr/bin/env python3

import json
import requests
from requests.auth import HTTPBasicAuth
import environ

# Reads the API_KEY and API_SECRET from .env file.
# Create one in the same directory as this file.
env = environ.Env()
environ.Env.read_env()
API_KEY = env("API_KEY")
API_SECRET = env("API_SECRET")

auth = HTTPBasicAuth(API_KEY, API_SECRET)

headers = {
    'Authorization': 'Basic ' + API_KEY,
    'Content-Type': 'application/json'
}

base_url = 'https://api.fivetran.com/v1/'
group_id = 'wad_crewmate'

payload = {
    "service": "adwords", # Put in your service id
    "group_id": "quenched_serotonin", # Put in your group_id (destination pipeline)
    "run_setup_tests": False,
    "config": {
        "schema": "test_0" # Name your schema in the destination
    }
}

# Create the shell connector
response = requests.post(base_url + 'connectors', auth=auth, json=payload).json()

# Parse out the the connector_id
connector_id = response['data']['id']

# Create the connect card token
response_token = requests.post(base_url + 'connectors/' + connector_id + 
    '/' + 'connect-card-token', auth=auth, json=payload).json()

# Parse out the connectors token
token = response_token['token']

# Generate the connect card link
print('https://fivetran.com/connect-card/setup?redirect_uri=fivetran.com&auth=' + token)
