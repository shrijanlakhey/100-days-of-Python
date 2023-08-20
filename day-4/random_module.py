import random

# generate random number including 1 and 6
random_integer = random.randint(1,6)
print(f"Random integer number is {random_integer}")

# generate random float number between 0.0 and 1.0 but not 1.0
random_float = random.random()
print(f"Random float number is {random_float}")

# for generating random float number between 0 and 5
print(random_float * 5)