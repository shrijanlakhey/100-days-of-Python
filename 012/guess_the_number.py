from random import randint

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

# Function to check user's guess against actual answer.
def check_answer(guess, answer, attempts):
    """checks answer against guess. Returns the number of turns remaining."""

    if guess == answer:
        print("Correct guess")
    elif guess > answer:
        print("Too high.")
        return attempts - 1
    else:
        print("Too low.")
        return attempts - 1

# function to set difficulty.
def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ".lower())
    if difficulty == 'hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        return EASY_LEVEL_ATTEMPTS

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = randint(1, 100)
    attempts = set_difficulty()
    print(answer)
    guess = 0

    while guess != answer:
        print(f"You have {attempts} remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = check_answer(guess,answer,attempts)

        if attempts == 0:
            print(f"You ran out of attempts. The correct guess is {answer}")
            return # exits the 'game()' function. To fix the bug as the game goes on and on even if the attempts reach 0
        elif guess != answer:
            print("Guess Again!")

game()



    


