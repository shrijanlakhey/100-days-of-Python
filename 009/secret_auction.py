from arts import logo
import os

print(logo)
print("Welcome to the secret auction program.")
continue_bidding = True
secret_auction = {}
highest_bid = 0
highest_bidder = ""
while continue_bidding:
    bidder = input("What is your name? ")
    bid_amount = int(input("What's your bid? $"))
    secret_auction[bidder] = bid_amount
    if bid_amount > highest_bid:
        highest_bidder = bidder
        highest_bid = secret_auction[bidder]
    result = input("Do you want to comintue? Type 'yes' or 'no'\n").lower()
    os.system('cls')
    if result == "no":
        continue_bidding = False
        print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
    