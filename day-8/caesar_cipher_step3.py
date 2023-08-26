# step 3
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(input_text, shift_amount, cipher_direction):
    final_text = ""
    for letter in input_text:
        position = alphabet.index(letter)
        if cipher_direction == "encode":
            new_position = position + shift_amount
        elif cipher_direction == "decode":
            new_position = position - shift_amount
        final_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is {final_text}")



#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(input_text=text, shift_amount=shift, cipher_direction=direction)