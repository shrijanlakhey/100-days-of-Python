from dotenv import load_dotenv
from os import getenv
from smtplib import SMTP
from email.mime.text import MIMEText

load_dotenv()
# mail
MY_EMAIL = getenv('EMAIL')
MY_PASSWORD = getenv('PASSWORD')

class EmailManager:
    def __init__(self):
        self.user = MY_EMAIL
        self.password = MY_PASSWORD


    def send_mail(self, emails, message):
        sender_email = MY_EMAIL
        subject = "Low Price Alert!"
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.user, password=self.password)
        
            for email in emails:
                msg = MIMEText(message, 'plain', 'utf-8')
                receiver_email = email
                msg['Subject'] = subject
                msg['From'] = MY_EMAIL
                msg['To'] = receiver_email
            
                connection.sendmail(
                    sender_email, 
                    receiver_email,
                    msg.as_string(),
                )
