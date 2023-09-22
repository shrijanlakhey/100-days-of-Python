def greet():
    print("Hello there")

def greet_with_name(name): # here, name is the parameter, parameter is the name used to refer the data being passed when the function is being called
    print(f"Hello {name}")

greet()
greet_with_name("Shrijan") # and 'Shrijan' is the argument, argument is the actual piece of data that is going to be passed to the function when it is being called