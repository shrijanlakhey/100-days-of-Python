piano_keys = ["c", "d", "e", "f", "g", "a", "b"]
piano_tuple = ["do", "re", "mi", "fa", "so", "la", "ti"]

# slicing, used to extract part of a string, list, or tuple
print(piano_keys[2:5]) # here 2 is the position of 3 and 5 is the position right after g, to get output: ['e', 'f', 'g']  
print(piano_keys[2:]) # extracts from 'e' to the end of the list
print(piano_keys[:5]) # extracts from 'g' to the start of the list

print(piano_keys[2:5:2]) # same as [2:5] but only returns every other item, i.e. it increments by 2
print(piano_keys[::2]) # returns every second item
print(piano_keys[::-1]) # reverses the list

print(piano_tuple[2:5])
