from art import logo
import os
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations= {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    keep_calculating = True

    while keep_calculating:
        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        continue_calculating = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculator: ").lower()
        if continue_calculating == "n":
            keep_calculating = False
            os.system('cls')
            calculator() # calling itself
        else:
            num1 = answer
        # note: since once the end of the function is reached, everything gets reset to the beginning so keep_calculating becomes True again so the while loop will continue working

# recursion = a function that calls itself within the function
calculator()