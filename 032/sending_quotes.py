import smtplib
from dotenv import load_dotenv
from os import getenv
import datetime as dt
from random import choice

load_dotenv()
MY_EMAIL = getenv('EMAIL')
MY_PASSWORD = getenv('PASSWORD')

# text file
with open("032/quotes.txt") as file:
    all_quotes = file.readlines()
    quote = choice(all_quotes)

# date and time
now = dt.datetime.now()
day = now.weekday()

# checks if the day is Monday, i.e., 0 (as in programming, we count from 0 and Monday is 0), and sends mail only if it is Monday
if day == 0:
    # mail
    with smtplib.SMTP("smtp.gmail.com") as connection:
    # securing connection to email server (if someone trys to intercept our email and try to read it, the message will be encrypted so they can't read it )
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs="uoriga7@gmail.com", 
            msg=f"Subject:Quote\n\n{quote}"
        )
