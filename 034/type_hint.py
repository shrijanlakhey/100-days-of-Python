# Type hints
# We can declare the data type of the variable
# Python doesn't actually enforce type hints at runtime. This means that a function can specify any desired return type, and the program would still run without actually returning a value of that type or raising an exception.
age:int
name:str
height:float
is_human:bool


# We can provide type hints for function parameters and return values. This helps other developers understand what types of arguments are expected by the function and what type the function returns.
# Arrows = '-> bool' means this function is expected to return a boolean data type
def police_check(age:int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False 
    return can_drive

if police_check(19):
    print("You may pass.")
else:
    print("Pay a fine.")
