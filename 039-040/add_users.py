import requests
from dotenv import load_dotenv
from os import getenv

USERS_SPREADSHEET_ENDPOINT = "https://api.sheety.co/b120e9ac753937bce877e68d19db026a/flightDeals/users"

load_dotenv()
# Sheety API
FLIGHT_SPREADSHEET_ENDPOINT = getenv("FLIGHT_SPREADSHEET_ENDPOINT")
FLIGHT_SPREADSHEET_AUTH_CODE = getenv("FLIGHT_SPREADSHEET_AUTH_CODE")

def add_new_user(first_name, last_name, email):
    body = {
        "user" : {
            "firstName" : first_name,
            "lastName" : last_name,
            "email" : email,
        }
    }
    headers = {
        "Authorization" : FLIGHT_SPREADSHEET_AUTH_CODE,
    }
    response = requests.post(url=USERS_SPREADSHEET_ENDPOINT, json=body, headers=headers)