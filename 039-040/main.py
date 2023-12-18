#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from datetime import datetime, timedelta
from email_manager import EmailManager
from add_users import add_new_user


ORIGIN_CITY_CODE = "LON"

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
email_manager = EmailManager()


tommorow = datetime.now() + timedelta(days=1)
from_date = tommorow.strftime("%d/%m/%Y")
serach_till = tommorow + timedelta(6*30) # 6 months
to_date = serach_till.strftime("%d/%m/%Y")


# Signing users up
print("Welcome to Shrijan's Flight Club. \nWe find the best flight deals and email you.")
first_name = input("What is your first name?\n").title()
last_name = input("What is your last name?\n").title()
email = input("What is your email?\n")
retype_email = input("Type your email again.\n")

if email != "" and email == retype_email:
    add_new_user(first_name, last_name, email)
    print("Welcome to the FLight club.")
else:
    print("Please make sure your emails match or is not empty.")

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        # pprint(f"First entry: {sheet_data[0]}")
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        data_manager.destination_data = sheet_data
        pprint(sheet_data[0]["iataCode"])

        data_manager.update_destination_codes()


for row in sheet_data:
    flight = flight_search.get_destination_price(from_code=ORIGIN_CITY_CODE, to_code=row["iataCode"], from_date=from_date, to_date=to_date, currency="GBP")
    if flight is None:
        continue
    if flight.price < row["lowestPrice"]:
        message=f"Only £{flight.price} to fly from {flight.departure_city}-{flight.departure_airport} to {flight.arrival_city}-{flight.arrival_airport} from {flight.departure_data} to {flight.return_date}"
        
        users = data_manager.get_user_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            print(message)
        email_manager.send_mail(emails, message)