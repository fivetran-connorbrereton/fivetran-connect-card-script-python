#!/usr/bin/env python3

import json
import requests
from requests.auth import HTTPBasicAuth
import environ
from random_word import RandomWords
import time

# Begin Auth
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
# End Auth

# Begin config
GROUP_ID = env("GROUP_ID")
connector_type = 'google_analytics_4'
# End config

## Random words for schema id
r = RandomWords()
schemaId = str(r.get_random_word()) + '_' + str(r.get_random_word())
# End config

# STDOUT colors
cyan = '\033[96m'
endc = '\033[0m'
failure = '\033[91m'

base_url = 'https://api.fivetran.com/v1/'

# Connector Config Payload: https://fivetran.com/docs/rest-api/connectors/config
payload = {
    "service": connector_type,
    "group_id": GROUP_ID,
    "Paused": "false",
    "run_setup_tests": False,
    "config": {
        "schema": schemaId
    },
    "connect_card_config": {
        "redirect_uri": "https://news.ycombinator.com"
    }
}

# Create the shell connector
print(f"{cyan}Creating a Connector...{endc}")

try:
    response = requests.post(base_url + 'connectors', auth=auth, json=payload).json()
    connector_id = response['data']['id']
except:
    print(f"{failure}Error{endc}\n")
    raise SystemExit(json.dumps(response, indent=2))

# Parse out the the connector_id
connector_card_url = response['data']['connect_card']['uri']

# Generate the connect card link
print(f"{cyan}All done! Get your URL below:{endc}")
print(f"{connector_card_url}")
