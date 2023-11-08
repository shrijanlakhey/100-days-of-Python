def calculate(**kwargs): # 'kwargs' will be in a form of a dictionary
    print(kwargs) # Output: {'add': 4, 'multiply': 2}

    # looping through the dictionary
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    print(kwargs["add"]) # printing the value of 'add' key

calculate(add=4, multiply=2)# here 'add' & 'multiply' are keys and 4 & 2 are their values. 


def new_calculate(n, **kwargs): # here 'n' is a normal positional argument and 'kwargs' is a dictionary of the remainder arguments
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

new_calculate(2, add=4, multiply=2)# here 'add' & 'multiply' are keys and 4 & 2 are their values. 


# kwargs are optional arguments meaning they can be either given or not

class Car:
    def __init__(self, **kwargs) :
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]
        
        # alternative way to access values of a key in dictionary
        # benefit of using this method is that it will return None if the key doesnt exist in the dictionary
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")


mycar1 = Car(make="Ford", model="GT-R")
print(mycar1.model)


mycar2 = Car(make="Ford")
print(mycar2.model) # prints None