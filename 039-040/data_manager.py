import requests
from dotenv import load_dotenv
from os import getenv
from pprint import pprint

load_dotenv()

# Sheety API
FLIGHT_SPREADSHEET_ENDPOINT = "https://api.sheety.co/b120e9ac753937bce877e68d19db026a/flightDeals/prices"
FLIGHT_SPREADSHEET_AUTH_CODE = getenv("FLIGHT_SPREADSHEET_AUTH_CODE")

# users
USERS_SPREADSHEET_ENDPOINT = "https://api.sheety.co/b120e9ac753937bce877e68d19db026a/flightDeals/users"
sheety_headers = {
    "Authorization" : FLIGHT_SPREADSHEET_AUTH_CODE,
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        """Gets the data for the flights from the Google Sheet"""
        response = requests.get(url=FLIGHT_SPREADSHEET_ENDPOINT, headers=sheety_headers)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        # 'pprint()' prints in more readable format (pretty print) 
        # pprint(data)
        return self.destination_data
    
    def update_destination_codes(self):
        """Updates the Google sheet with the IATA airport code"""
        for city in self.destination_data:
            new_data = {
                "price" :{
                    "iataCode" : city["iataCode"]
                }   
            }
            
            response = requests.put(url=f"{FLIGHT_SPREADSHEET_ENDPOINT}/{city['id']}", json=new_data, headers=sheety_headers)
            response.raise_for_status()
            print(response.text)

    def get_user_emails(self):
        """Gets the emails of the registered users from the Google Sheet"""
        response = requests.get(url=USERS_SPREADSHEET_ENDPOINT, headers=sheety_headers)
        response.raise_for_status()
        data = response.json()
        self.user_data = data["users"]
        return self.user_data