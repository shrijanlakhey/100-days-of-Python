import requests
from dotenv import load_dotenv
from os import getenv
from flight_data import FlightData
from pprint import pprint

load_dotenv()
TEQUILA_API_KEY = getenv("TEQUILA_API_KEY")
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"

class FlightSearch:
    def get_destination_code(self,city_name):
        """returns the IATA airport code of the city"""
        query = {
            "term" : city_name,
            "location_types" : "city", 
        }

        headers = {
            "apikey" : TEQUILA_API_KEY,
        }
        
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=query, headers=headers)
        response.raise_for_status()
        data = response.json()
        code = data["locations"][0]["code"]
        return code
    
    def get_destination_price(self, from_code, to_code, currency, from_date, to_date):
        """get the price of the ticket from the current city to the destination city and returns them in GBP currency"""
        query = {
            "fly_from" : from_code,
            "fly_to" : to_code,
            "date_from" : from_date,
            "date_to" : to_date,
            "nights_in_dst_from" : 7,
            "nights_in_dst_to" : 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr" : currency,
        }

        headers = {
            "apikey" : TEQUILA_API_KEY,
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=query, headers=headers)
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=query, headers=headers)
            try:
                data = response.json()["data"][0]
                pprint(data)
            except IndexError:
                return None
            else:
                flight_data = FlightData(
                    departure_city = data["route"][0]["cityFrom"],
                    departure_airport = data["route"][0]["flyFrom"],
                    arrival_city = data["route"][0]["cityTo"],
                    arrival_airport = data["route"][0]["flyTo"],
                    departure_data = data["route"][0]["local_departure"].split("T")[0],
                    return_date = data["route"][0]["local_arrival"].split("T")[0],
                    price=data["price"],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                print(f"{flight_data.arrival_city}: £{flight_data.price}")
                return flight_data
        else:
            flight_data = FlightData(
                departure_city = data["route"][0]["cityFrom"],
                departure_airport = data["route"][0]["flyFrom"],
                arrival_city = data["route"][0]["cityTo"],
                arrival_airport = data["route"][0]["flyTo"],
                departure_data = data["route"][0]["local_departure"].split("T")[0],
                return_date = data["route"][0]["local_arrival"].split("T")[0],
                price=data["price"],
            )
            print(f"{flight_data.arrival_city}: £{flight_data.price}")
            return flight_data