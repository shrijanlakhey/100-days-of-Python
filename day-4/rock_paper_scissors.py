import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game=[rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))


if user_choice >= 3 or user_choice < 0:
    print("Invalid Choice!")
else:
    print(game[user_choice])
    computer_choice = random.randint(0, len(game) - 1)
    print(f"Computer chose:\n {game[computer_choice]}")

    if user_choice == computer_choice:
        print("Draw!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("Computer wins!")
    elif user_choice > computer_choice:
        print("You win!")
    elif user_choice < computer_choice:
        print("Computer wins!")
