# Unlimited positional arguments (as position of the arguments being passed into teh function matters)

# takes any number of arguments
# '*' tells that this function accepts any number of arguments 
def add(*args):
    # args[0] can also access them by index as it is a tuple after all
    sum=0
    for n in args: # 'args' will be in a form of a tuple
        sum += n
    return sum 

print(add(1,2,3))