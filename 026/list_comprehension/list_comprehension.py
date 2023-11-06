# list comprehension: create a new list from a previous list
# we have been doing that with a for loop but it can be done with a single line of code
# it works with Python Sequences(they have specific order): list, range, string, tuple

# old way
# numbers = [1,2,3]
# new_list = []

# # creating a new list by adding 1 to each items
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)


# new way
# syntax: new_list = [new_item for item in list] 
# 'new_item': expression or a code we need to execute in order to get a new item
# 'item': element from a list
# 'list': already existing list using which we want to create a new one 
numbers = [1,2,3]
new_list = [n+1 for n in numbers]
print(new_list)

# we can use it with strings as well
name = "Shrijan"
letters_list = [letter for letter in name] 
print(letters_list)

# using it in range
range_list = [num*2 for num in range(1,5)]
print(range_list)


# conditional list comprehension
# syntax: new_list = [new_item for item in list if test] # only execute if the condition is statisfied  

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)