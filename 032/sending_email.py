import smtplib
from dotenv import load_dotenv
from os import getenv

load_dotenv()
MY_EMAIL = getenv('EMAIL')
MY_PASSWORD = getenv('PASSWORD')

with smtplib.SMTP("smtp.gmail.com") as connection:
# securing connection to email server (if someone trys to intercept our email and try to read it, the message will be encrypted so they can't read it )
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL, 
        to_addrs="uoriga7@gmail.com", 
        msg="Subject:Hello\n\nThis is the body of my email."
    )
