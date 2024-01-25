# def add(n1, n2):
#     return n1 + n2


# def subtract(n1, n2):
#     return n1 - n2


# def multiply(n1, n2):
#     return n1 * n2


# def divide(n1, n2):
#     return n1 / n2


# # functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.
# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)


# result = calculate(add, 5, 2)
# print(result)


# # functions can be nested in other functions
# def outer_function():
#     print("I'm outer")

#     def nested_function():
#         print("I'm inner")

#     nested_function()


# outer_function()

# output:
# I'm outer
# I'm inner


# functions can be returned from other functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function


# it prints 'I'm outer' but does not execute 'nested_function', it returns reference to 'nested_function'
inner_function = outer_function()
# the returned function is assigned to the variable 'inner_function', when 'inner_function()' is called it executes the code inside the 'nested_function()' printing 'I'm inner'
inner_function()

#--------------------------------------------------------------------------------------------------------------------------------#

# Python decorator function
# decorator function is a fucntion that wraps another function and gives that function some additional functionality
def decorator_function(function):
    def wrapper_function():
        function()

    return wrapper_function


# example
import time


# assuming, we want to add few seconds of delay before execution of teh code in each of the functions, then we'd have to add sleep() method to each of the functions. Alternatively, we can use decorator to add this few seconds delay functionality and add delay by passing in the function to the decorator

# def say_hello():
#     time.sleep(2)
#     print("Hello")


# def say_bye():
#     time.sleep(2)
#     print("Bye")


# solution (using decorators to add delay to the functions)
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # do something before we run the function
        function()
        # do something after we run the function

    return wrapper_function


# feeds the function 'say_hello' as the argument to the delay_decorator function's 'function' parameter
@delay_decorator
def say_hello():
    print("Hello")


def say_bye():
    print("Bye")


say_hello()
say_bye()

# '@delay_decorator', is a syntatic sugar. It is used to make it easier to alternatively write code
# alternativelty, we could write,
# decorated_function = delay_decorator(say_bye)
# decorated_function()