import pandas
import datetime as dt
from random import randint
import smtplib
from dotenv import load_dotenv
from os import getenv

load_dotenv()
MY_EMAIL = getenv('EMAIL')
MY_PASSWORD = getenv('PASSWORD')

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("032/birthday_wisher/birthdays.csv")
birthday_dict = {
    (data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    file_path = f"032/birthday_wisher/letter_templates/letter_{randint(1,3)}.txt"
    with open(file_path) as letter_file:
        reciever_name = birthday_dict[today_tuple]["name"]
        receiver_email = birthday_dict[today_tuple]["email"]
        contents = letter_file.read()
        # simply replacing the name does not change the content, we need to save it to the contents variable itself
        contents = contents.replace("[NAME]", reciever_name)
      
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=receiver_email, 
            msg=f"Subject:Happy Birthday\n\n{contents}"
        )