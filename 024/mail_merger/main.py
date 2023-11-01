PLACEHOLDER = "[name]"

# getting names
stripped_names = []
with open("024/mail_merger/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    
# reading the letter
with open("024/mail_merger/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    
    # stripping whitespace and new line from the names and replacing them in the letter
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

        # creating letters with the names of people who are invited
        with open(f"024/mail_merger/Output/ReadyToSend/letter_to_{stripped_name}.txt", mode="w") as completed_letter:            
            completed_letter.write(new_letter)
            
