import requests
from datetime import datetime
import pytz
from dateutil import parser
from os import getenv
from dotenv import load_dotenv

load_dotenv()
MY_LAT = getenv("MY_LATITUDE")
MY_LONG = getenv("MY_LONGITUDE")

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

# 'split()' method splits the string into a list
#  in our case, 2023-11-23T00:44:05+00:00 into:
# 'sunrise.split("T")' = ['2023-11-23', '00:44:05+00:00'] then to
# 'sunrise.split("T")[1].split(":")' = ['00', '44', '05+00', '00'] then to 
# 'sunrise.split("T")[1].split(":")[0]' = 00
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunrise)

print(sunset)


# # UTC timezone
# # since the api retruns only UTC time, we need to convert it to out local timezone
# # here parsing/changing the date and time string received to a datetime object
# utc_sunrise = parser.parse(data["results"]["sunrise"])
# utc_sunset = parser.parse(data["results"]["sunset"])

# # Target timezone
# target_timezone = pytz.timezone("Asia/Kathmandu")

# # Convert UTC time to target timezone 
# local_sunrise = utc_sunrise.replace(tzinfo=pytz.utc).astimezone(target_timezone).hour
# local_sunset = utc_sunset.replace(tzinfo=pytz.utc).astimezone(target_timezone).hour

# print(type(local_sunrise))
# print(local_sunset)

time_now = datetime.now()
print(time_now.hour)