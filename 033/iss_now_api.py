import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# raises an HTTPError if the HTTP request returned an unsuccessful status code
response.raise_for_status()

data = response.json()
# we can tap into it just like we would with any python dicitonary
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude,latitude)
print(iss_position)