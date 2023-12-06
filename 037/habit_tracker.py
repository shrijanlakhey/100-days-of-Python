import requests
from dotenv import load_dotenv
from os import getenv
from datetime import datetime

USERNAME = "shrijan"
GRAPH_ID = "graph1"
load_dotenv()
PIXElA_USER_TOKEN = getenv("PIXELA_USER_TOKEN")
PIXELA_ENDPOINT = "https://pixe.la/v1/users"


user_params = {
    "token" : PIXElA_USER_TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# creating a user (commenting it out since the user has been created)
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)

# returns the response as a piece of text
# print(response.text)


# creating a graph
# GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

# graph_config = {
#     "id" : "graph1",
#     "name" : "Reading Graph",
#     "unit" : "pages",
#     "type" : "int",
#     "color" : "kuro",
#     "timezone" : "Asia/Kathmandu"

# }

headers = {
    "X-USER-TOKEN" : PIXElA_USER_TOKEN,
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

# Posting a pixel
# POST_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

# # 'strftime()' is used to format datetime objects into readable strings
today = datetime.now() # adding pixel for today
# today = datetime(year=2023, month=12, day=5) # adding pixel for a specific date

# post_config = {
#     "date" : today.strftime("%Y%m%d"),
#     "quantity" : "10",	
# }

# response = requests.post(url=POST_ENDPOINT, json=post_config, headers=headers)
# print(response.text)


# Updating a pixel
# UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# update_config = {
#     "quantity" : "7",
# }

# response = requests.put(url=UPDATE_ENDPOINT, json=update_config, headers=headers)
# print(response.text)


# Deleting a pixel
DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=DELETE_ENDPOINT, headers=headers)
print(response.text)