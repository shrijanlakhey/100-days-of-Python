# adds the content to the file and does not remove previous the contents if there were any, 'a' means append
# it also creates a new file with the name given if the file does not exist
with open("024/my_file.txt", mode="a") as file:
    file.write("\nAppended text from append_in_a_file.py")
