################### Scope ####################

# --------------------Local Scope--------------------
# it exists within functions
def drink_potion():
  potion_strength = 2
  print(potion_strength)

drink_potion()

# print(potion_stength)
# when we try to print the 'potion_strength' variable outside of the 'drink_potion()' function, we will get an error:
# print(potion_stength)
#           ^^^^^^^^^^^^^^
# NameError: name 'potion_stength' is not defined
# we cant access the variable outside the function because it is locally declared or it has local scope




# --------------------Global Scope--------------------

player_health = 10
def eat_food():
    print(player_health)

eat_food()

# here we can access 'player_health' variable even inside the function as it is globally declared or it has global scope
# note: the variable must be declared before the function is called

# scopes can be applied to not just to variables but to functions as well or basically anything else we name or has a namespace
# namespace - a container that holds a set of identifiers (such as variable names, function names, and class names) and their corresponding objects. Namespaces are used to organize and manage the names of entities in a Python program, preventing naming conflicts and ensuring that each name refers to the correct object within the program's scope.

# bad idea to call local variable and global variable with same name


# --------------------there is no block scope in python--------------------
# block scope - Variables declared within a block are said to have block scope, which means they are only accessible within that specific block and any nested blocks.

# blocks like if, while, for, etc. with colons and indentations, they dont count as creating local scope

game_level = 2

enemies = ["zombies", "skeleton", "phantom"]
if game_level < 5:
   new_enemy = enemies[0]

print(new_enemy)
# the new varibale created in the if block can be easily accessed from anywhere as it does not have a local scope but a global scope

def fruit():
    fruits = ["apple", "mango", "grape"]
    if game_level < 5:
        new_food = enemies[0]

# print(new_food)
# but when we try to print 'new_food' outside of the 'fruit()' function, we cant because it has local scope as it is declared inside the function so we can print it inside the function but not outside of it