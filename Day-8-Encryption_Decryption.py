alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input(
    "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
index = 0


# def encrypt(text, shift):
#   cipher_text = ""
#   new_position = 0
#   for letters in text:
#     index = alphabet.index(letters)
#     new_position = index + shift
#     if new_position > 25:
#       new_position = new_position - 26
#     else:
#       new_position = new_position
#     cipher_text += alphabet[new_position]
#   print(f"The encoded text is: {cipher_text}")

# #encrypt(text,shift)
#   #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#   #e.g.
#   #plain_text = "hello"
#   #shift = 5
#   #cipher_text = "mjqqt"
#   #print output: "The encoded text is mjqqt"

#   ##HINT: How do you get the index of an item in a list:
#   #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

#   ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.


# def decrypt(text, shift):
#   plain_text = ""
#   for letter in text:
#     position = alphabet.index(letter)
#     new_position = position - shift
#     if new_position < 0:
#       new_position = new_position + 26
#     else:
#       new_position = new_position
#     plain_text += alphabet[new_position]
#   print(f"The decoded text is: {plain_text}")

# #decrypt(text,shift)


# if (direction == "encode"):
#   encrypt(text, shift)
# elif (direction == "decode"):
#   decrypt(text, shift)
# else:
#   print("Invalid input. Only decode or encode is acceptable.")

# all in a single function

def ceaser_cipher(text, shift, direction):
    if (direction == "encode"):
        cipher_text = ""
        new_position = 0
        for letters in text:
            index = alphabet.index(letters)
            new_position = index + shift
            if new_position > 25:
                new_position = new_position - 26
            else:
                new_position = new_position
            cipher_text += alphabet[new_position]
        print(f"The encoded text is: {cipher_text}")
    
    elif (direction == "decode"):
        plain_text = ""
        for letter in text:
            position = alphabet.index(letter)
            new_position = position - shift
            if new_position < 0:
                new_position = new_position + 26
            else:
                new_position = new_position
            plain_text += alphabet[new_position]
        print(f"The decoded text is: {plain_text}")

    else:
        print("Invalid input.")

ceaser_cipher(text, shift, direction)