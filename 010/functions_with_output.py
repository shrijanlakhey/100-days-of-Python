def my_function():
    result = 3*2
    return result # return is an output keyword

output = my_function()
print(output)


def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"
    # when the word return is encountered, the code after that line is not executed or ignored as it assumes that it is the end of the function


formatted_string = format_name("shrijan", "LAKHEY")
print(formatted_string)


# print vs return
# what if we want to use the output of a function as an input for another? Thats why it is more suitable to use return keyword to return the output form a function rather then just printing it