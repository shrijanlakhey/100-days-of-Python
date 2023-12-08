import requests
from dotenv import load_dotenv
from os import getenv
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 77.7
HEIGHT_CM = 182.88
AGE = 22

load_dotenv()
# Nutrionix API
NUTRITIONIX_API_ID = getenv("NUTRITIONIX_API_ID")
NUTRITIONIX_API_KEY = getenv("NUTRITIONIX_API_KEY")
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Sheety API
SPREADSHEET_ENDPOINT = getenv("SPREADSHEET_ENDPOINT")
SPREADSHEET_AUTH_CODE = getenv("SPREADSHEET_AUTH_CODE")

query = input("Tell me which exercises you did: ")

exercise_headers = {
    "x-app-id" : NUTRITIONIX_API_ID,
    "x-app-key" : NUTRITIONIX_API_KEY,
}

exercise_params = {
    "query" : query,
    "gender" : GENDER,
    "weight_kg" : WEIGHT_KG,
    "height_cm" : HEIGHT_CM,
    "age" : AGE,
}

exercise_data = requests.post(url=nutritionix_endpoint, json=exercise_params, headers=exercise_headers)
exercise_data.raise_for_status()
result = exercise_data.json()
# print(f"Nutritionix API call: \n {result} \n")

today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
time_now = today.strftime("%H:%M:%S")

# Sheety API
GOOGLE_SHEET_NAME = "sheet1"
sheety_headers = {
    "Authorization" : SPREADSHEET_AUTH_CODE,
}
sheety_endpoint = SPREADSHEET_ENDPOINT

for exercise in result["exercises"]:
    new_row = {
        GOOGLE_SHEET_NAME : {
            "date" : today_date,
            "time" : time_now,
            "exercise" : exercise["name"].title(),
            "duration" : exercise["duration_min"],
            "calories" : exercise["nf_calories"],

        }
    }

    response = requests.post(url=sheety_endpoint, json=new_row, headers=sheety_headers)
    print(response.text)