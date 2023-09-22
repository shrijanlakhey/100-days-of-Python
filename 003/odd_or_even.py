# '%', modulo operator gives the remainder of the division
# eg, 7 % 3 => 3 + 3 + 1, the output or the remainder will be 1

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("It is an even number")
else:
    print("It is an odd number")