def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Shrijan Lakhey", "Thaiba") # positional arguments, as we haven't specified which specific parameter the data is being passed to, so it just looks at the position of the parameters  corresponding to the function it is being passed to

# keyword arguments
greet_with(location="Godavari", name="Ram Shakya") # the data is being passed to specific parameters so the order of passing data does not matter