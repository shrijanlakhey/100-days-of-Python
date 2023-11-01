# normally, we would just write "my_file.txt" but since i am opening this project from the 100-days-of-Python folder itself, the folder it is stored in must be specified in the path as well

# When using this method, we have to manually add file.close() at the end of the code
# file = open("024/my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with keyword manages the file directly. It closes the file as soon as we are done using the file
with open("024/my_file.txt") as file:
    contents = file.read()
    print(contents)


# note: in relative path, use '..' two dots to go back one folder, if we want to go back 2 folders then it would be '../../file.txt' 