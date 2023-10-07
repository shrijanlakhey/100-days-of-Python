############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# for loop is looping through 1 to 19 and the if statment is supposed to print the statement when the value of 'i' is 20 but value of 'i' never reaches 20 as it loop from 1 to 19 only


# solution:
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()


# ----------------------------------------------------------------------------------------------------------------------------------------

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])


# when the dice_num = 6, an error is beng produced as lists are indexed starting form 0

# solution:
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])


# ----------------------------------------------------------------------------------------------------------------------------------------

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# nothing is printed when 1994 is the input

# solution
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# ----------------------------------------------------------------------------------------------------------------------------------------


# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")


# solution
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")


# ----------------------------------------------------------------------------------------------------------------------------------------


# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# solution
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(f"Pages = {pages} and word per page = {word_per_page}")
# print(total_words)

# ----------------------------------------------------------------------------------------------------------------------------------------

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

# solution
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])