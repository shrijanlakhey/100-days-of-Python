# try:
#     file = open("030/file.txt") 

#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"]) 
# # code if file is not found
# except FileNotFoundError: 
#     # if the 'file.txt' does not exist then the except block code will create one
#     file =  open("030/file.txt", mode="w")
#     file.write("File created from except block.")
# # code if key does not exist
# except KeyError as error_message: # getting hold of the error message in 'error_message' 
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # this will raise an error even if there are no errors
#     # raise KeyError 
#     raise KeyError("This is an error that I made up.")

height = float(input("Height: ")) # measured in meters
weight = int(input("Weight: ")) # measured in kg

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")
bmi = weight / height ** 2
print(bmi)