# ---------------------------- Common Errors ------------------------------- #

# FileNotFound
# trying to read a file that does not exist
# with open("file.txt") as file:
#     file.read()

# KeyError
# trying to access the value of a key that does not exist
# a_dictionary = {"key": "value"}
# print(a_dictionary["new_key"])

#IndexError
# trying to access an element at an index that does not exist in the list
# fruit_list = ["Apple", "Banana", "Melon"]
# print(fruit_list[3])

# TypeError
# trying to add or concatenate string and a non-string value
# text = "xyz"
# print(text + 5)



# ---------------------------- Cathcing Exceptions ------------------------------- #


# try: executing something that might cause and exception/error
# catch: execute this block of code if there was an exception/error
# else: execute this block of code if there was no exception/error
# finally: carry out this block of code no matter what happens, i.e., ececute this code even if the exception/error occurs or not

# FileNotFound
# try:
#     with open("030/file.txt") as file:
#         file.read()

#     a_dictionary = {"key": "value"}
#     print(a_dictionary["new_key"])
# except:
#     # if the 'file.txt' does not exist then the except block code will create one
#     with open("030/file.txt", mode="w") as file:
#         file.write("file created from except block")

# in the code above 'print(a_dictionary["new_key"])' line of code is not throwing an exception but this exception in caught in the except block and only the code given in the except block is executed meaning there is not appropriate code for this error
# so we need to specify which type of exception to catch for eg, we use 'FileNotFoundError', 'KeyError' here

try:
    file = open("030/file.txt") 

    a_dictionary = {"key": "value"}
    print(a_dictionary["new_key"]) 
# code if file is not found
except FileNotFoundError: 
    # if the 'file.txt' does not exist then the except block code will create one
    file =  open("030/file.txt", mode="w")
    file.write("File created from except block.")
# code if key does not exist
except KeyError as error_message: # getting hold of the error message in 'error_message' 
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")