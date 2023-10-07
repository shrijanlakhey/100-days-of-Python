# note if the computer ends up with score < 17, they must take anotehr card
import random
from art import logo
import os

def cards_dealt():
    """Deals random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    # check if the score passes 21 if yes then retrun 0 i.e.,the user or the computer has got a blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(player_score, computer_score):
    if player_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose, opponent has Blackjack"
    elif player_score == 0:
        return "You win with a Blackjack"
    elif player_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif player_score > computer_score:
        return "Blackjack"
    else:
        return "Bust"
    
def blackjack():
    print(logo)
    player_cards = []
    computer_cards = []
    is_game_over = False

    for i in range(2):
        player_cards.append(cards_dealt())
        computer_cards.append(cards_dealt())

    while not is_game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\n     Your cards: {player_cards}, current score: {player_score}")
        print(f"     Computer's first card: {computer_cards[0]}\n")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            deal_more = input("Type 'y' to get another card, type 'n' to pass: ")
            if deal_more == "y":
                player_cards.append(cards_dealt())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(cards_dealt())
        computer_score = calculate_score(computer_cards)

    print(f"\n     Your final hand is {player_cards}, final score is {player_score}")
    print(f"     Computer's final hand is {computer_cards}, final score is {computer_score}\n")
    print(compare(player_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('cls')
    blackjack()