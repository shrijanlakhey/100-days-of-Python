import requests
from datetime import datetime
import pytz
from dateutil import parser
import smtplib
from os import getenv
from dotenv import load_dotenv
from time import sleep

load_dotenv()

MY_LAT = float(getenv("MY_LATITUDE"))
MY_LONG = float(getenv("MY_LONGITUDE"))

MY_EMAIL = getenv('EMAIL')
MY_PASSWORD = getenv('PASSWORD')

#position is within +5 :or -5 degrees of the ISS position.
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():   
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    # getting sunrise and sunset times in UTC
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    # for UTC
    # sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    # sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # for my local timezone (Asia/Kathmandu)
    # since the api retruns only UTC time, we need to convert it to out local timezone
    # here parsing/changing the date and time string received to a datetime object
    utc_sunrise = parser.parse(data["results"]["sunrise"])
    utc_sunset = parser.parse(data["results"]["sunset"])

    # Target timezone
    target_timezone = pytz.timezone("Asia/Kathmandu")

    # Converting UTC time to Asia/Kathmandu timezone 
    sunrise = utc_sunrise.replace(tzinfo=pytz.utc).astimezone(target_timezone).hour
    sunset = utc_sunset.replace(tzinfo=pytz.utc).astimezone(target_timezone).hour
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


# runs the code every sixty seconds checking if the iss is above my location and if it is night time
while True:
    sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs="lakheyshrijan@gmail.com", 
                msg="Subject:Hey look Up\n\nISS is above you in the sky."
            )

