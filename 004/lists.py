# in programming, indexing starts from 0
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]  

print(states_of_america[0])

# can also use negative index to start counting from the back
print(states_of_america[-1])

# changing values in a list
states_of_america[1] = "Pencilvania"
print(states_of_america)

# adding an item to the list
states_of_america.append("Shrijanvania")
print(states_of_america)

# adding multiple values or items to a list
states_of_america.extend(["Conoraia", "Demarhoma"])
print(states_of_america)