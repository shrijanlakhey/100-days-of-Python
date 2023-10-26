def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# higher order functions: a function that can work with other functions
# here calculator() is a higher order function because it is taking another function as an input and working with it inside the body of the function
def calculator(n1, n2, func):
    return func(n1, n2)

print(calculator(5, 5, add))

