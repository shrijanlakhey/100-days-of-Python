import os
from game_data import data
from random import choice
from art import logo, vs

score = 0
continue_game = True

def format_data(account):
    """Format the account into printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

# def instagram_data():
#     """Selects random data from data dictionary"""
#     option = choice(data)
#     return option

def compare_answer(answer, a_followers, b_followers):
    """Compares the followers of two accounts and returns true if the answer given matches the account with highest follower count"""
    if a_followers > b_followers:
        return answer == 'a'
    else:
        return answer == 'b'


account_b = choice(data)

print(logo)
while continue_game:
  
    account_a = account_b
    if account_a == account_b:
        account_b = choice(data)

    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]


    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    compare = compare_answer(answer, a_followers_count, b_followers_count)
    os.system('cls')
    print(logo)

    if compare:
        score += 1
        print(f"You are right! Current score is {score}")
    else:
        continue_game=False
        print(f"You lose! Final score is {score}")




