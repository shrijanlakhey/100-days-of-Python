from dotenv import load_dotenv
from os import getenv
import requests
from smtplib import SMTP
from email.mime.text import MIMEText

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

load_dotenv()

# Alpha Vantage API
ALPHAVANTAGE_ACCESS_KEY = getenv("ALPHAVANTAGE_ACCESS_KEY")
ALPHAVANTAGE_ENDPOINT= "https://www.alphavantage.co/query"

# newsapi
NEWSAPI_KEY = getenv("NEWSAPI_KEY")
NEWSAPI_ENDPOINT = "https://newsapi.org/v2/everything"

# mail
MY_EMAIL = getenv('EMAIL')
MY_PASSWORD = getenv('PASSWORD')

def calculate_percentage_change(today_closing_value, previous_closing_value):
    """Calculates the percentage change between today and yesterdays closing value of a stock"""
    diff = float(today_closing_value) - float(previous_closing_value)
    percentage_change = round((diff/float(today_closing_value)) * 100)
    return percentage_change


# Alpha Vantage API
aplhavantage_parmas = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : ALPHAVANTAGE_ACCESS_KEY,
}

alpha_vantage_response = requests.get(ALPHAVANTAGE_ENDPOINT, params=aplhavantage_parmas)
alpha_vantage_response.raise_for_status()

data = alpha_vantage_response.json()["Time Series (Daily)"]

# Each item in this new list is composed of only values and not their keys from the dictionary
data_list = [value for (key,value) in data.items()]

# share closing price
yesterday_closing_value = data_list[0]["4. close"]
day_before_yesterday_closing_value = data_list[1]["4. close"]


percentage_change = calculate_percentage_change(yesterday_closing_value, day_before_yesterday_closing_value)

up_down = None
if percentage_change > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


# Newsapi API
newsapi_parms = {
    "qInTitle" : COMPANY_NAME,
    "apikey" : NEWSAPI_KEY,
}

newsapi_response = requests.get(NEWSAPI_ENDPOINT, params=newsapi_parms)
newsapi_response.raise_for_status()

article_data = newsapi_response.json()
three_articles = article_data["articles"][1:4]

formatted_articles= [f"Headline: {article['title']} \nBrief: {article['description']}" for article in three_articles]

# mail
for article in formatted_articles:
    sender_email = MY_EMAIL
    receiver_email = "lakheyshrijan@gmail.com"
    subject = f"{STOCK} {up_down}{percentage_change}%"
    body = article

    # Create the MIMEText object and set the character encoding to UTF-8
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = MY_EMAIL
    msg['To'] = receiver_email

    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            sender_email,
            receiver_email,
            msg.as_string(),
        )