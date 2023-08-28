# dictionary has key and value. eg, "Bug" is the key and "An eroor in a program that...." is its value
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])# here bug is the key, the output will be "An error in a program that...", i.e. it prints its corresponding value

# adding new data to the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)

# recommended to create an empty dictionary beforehand
empty_dictionary = {}



# edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# loop through a dictionary
for key in programming_dictionary:
    print(key) # prints the keys  only
    print(programming_dictionary[key]) # accessing the value of corresponding key

# wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)