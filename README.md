# Fivetran Connect Card Generation Script in Python
Easily generate connect cards from the comfort of your chair using Python

## How this works
We're going to setup a really simple script that will generate a [Connect Card](https://fivetran.com/docs/rest-api/connectors/connect-card) URL for Google Analytics. Want to try other connector types? Check out the config examples here: https://fivetran.com/docs/rest-api/connectors/config

## Prepare
- You'll need a Fivetran account and your key and secret that you can find in settings. Find out more in our [getting started guide](https://fivetran.com/docs/rest-api/getting-started).
- Make sure you have a [working python environment](https://xkcd.com/1987/).
- Setup a destination in Fivetran (ie Snowflake, BigQuery, etc): https://fivetran.com/docs/destinations and get your destination ID from the bottom of the destination page details in your dashboard. 

## Dev Environment
- Make sure you have pip installed: `pip -V`
- Make sure you have virtualenv installed: `virtualenv --v` (install with `pip install virtualenv`)

## Install required packages
- Install a virtual env for this project: `python3 -m venv .venv`
- Activate the virtual env: `source .venv/bin/activate`
- Install requirements: `pip install -r requirements.txt`

## Create .env file
Create a `.env` file in the root of the project and add your key, secret, destination group id in the below format:
```
API_KEY=
API_SECRET=
GROUP_ID=
```

## Run the script
`python create_cc.py`

## Learn more about Connect Cards and Powered by Fivetran
- [Fivetran Connect Cards](https://fivetran.com/docs/rest-api/connectors/connect-card)
- [Powered by Fivetran QuickStart](https://fivetran.com/docs/getting-started/powered-by-fivetran)

