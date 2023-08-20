import random
names_string = input("Give me everybody's names, separated by a comma. ")
# split method is used to split string into a list by specifying a separator (defalut separator is whitespace)
names = names_string.split(", ")
print(names)
# len method returns the length of an object
# since we start indexing form 0 but len returns or counts the items starting from 1, we need to do '-1' 
random_name = random.randint(0, len(names) - 1 )
print(f"{names[random_name]} is going to buy the meal today!")

# alternative solution using choice method (one line code)
# print(f"{random.choice(names)} is going to buy the meal today!")