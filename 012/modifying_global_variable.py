# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# output:
# enemies inside function: 2
# enemies outside function: 1

# --------------------------------------------------------------------------------------------------------------------------------

# enemies = 1

# def increase_enemies():
#   # to modify a global variable within a function, we have to explicitly say that we have a global varibale with the following name
#   global enemies
#   enemies = 2

#   # now the changes made to the 'enemies' variable will be reflected on the global variable 'enemies' i.e, its value will be set to 2 
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# output:
# enemies inside function: 2
# enemies outside function: 2


# but it is recommended to avoid modifying global varibale

# --------------------------------------------------------------------------------------------------------------------------------

# alternative way
enemies = 1

def increase_enemies():
  return enemies + 1
 

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# output: enemies outside function: 2