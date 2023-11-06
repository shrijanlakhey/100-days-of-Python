sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words_list = sentence.split()

result = {word:len(word) for word in words_list}
print(result)