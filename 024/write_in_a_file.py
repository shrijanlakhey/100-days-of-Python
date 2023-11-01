# by default the mode parameter is "r", i.e. read only mode

# it writes in a file and also replaces all the previous contents of the file if there were any
# it also creates a new file with the name given if the file does not exist
with open("024/my_file.txt", mode="w") as file:
    file.write("New text from write_in_a_file.py")
