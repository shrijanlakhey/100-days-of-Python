class FlightData:
    def __init__(self, departure_city, departure_airport, arrival_city, arrival_airport, departure_data, return_date, price, stop_overs=0, via_city=""):
        self.departure_city = departure_city
        self.departure_airport = departure_airport
        self.arrival_city = arrival_city
        self.arrival_airport = arrival_airport
        self.departure_data = departure_data
        self.return_date = return_date
        self.price = price
        self.stop_overs = stop_overs
        self.via_city = via_city

