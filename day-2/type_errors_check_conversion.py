num_char = len(input("What is your name?"))

# got an error running the code in line 4 because we can't concatenate string and integer
# print("Your name has" + num_char + "characters")

# checking data type of the variable num_char
print(type(num_char))

# converting variable num_char into string
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters")

# float() funtcion is converting string into float type
print(30 + float("70.5"))