from dotenv import load_dotenv
from os import getenv
import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

load_dotenv()
# Openweathermap API
MY_LAT = getenv("MY_LATITUDE")
MY_LONG = getenv("MY_LONGITUDE")
OWM_API_KEY = getenv("OWM_API_KEY") 


# Twilio API
account_sid = getenv("TWILIO_ACCOUNT_SID")
auth_token = getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)


weather_params = {
    "lat" : MY_LAT,
    "lon" : MY_LONG,
    "exclude" : "current,minutely,daily,alerts",
    "appid" : OWM_API_KEY,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

# Getting only 12 hours weather code
hour_data = [weather_data["hourly"][n]["weather"][0]["id"] for n in range(0,12)]

for condition_code in hour_data:
    # sets 'will_rain' to True if the condition code is less than 700
    if condition_code < 700:
        will_rain = True

if will_rain:
    # print("Bring an umbrella.")
    message = client.messages \
                .create(
                     body="It's going to rain today. Remember to bring an umbrella ☔",
                     from_='+18572147350',
                     to='+977 981 8435762'
                 )

    print(message.status)

# Another method to get 12 hour only weather code
# weather_slice = weather_data["hourly"][:12] # 0-11

# for hour_data in weather_slice:
#     condition_code = hour_data["weather"][0]["id"]

#     if int(condition_code) < 700:
#         print("Bring an umbrella.")