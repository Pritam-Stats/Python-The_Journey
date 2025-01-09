alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input(
#     "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

index = 0

def caeser_cipher(text, shift, direction):
    if (direction == "encode"):
        cipher_text = ""
        new_position = 0
        for letters in text:
            if letters not in alphabet:
                cipher_text += letters
            else:
                index = alphabet.index(letters)
                new_position = index + shift
                if new_position > 25:
                    new_position = new_position % 26
                else:
                    new_position = new_position
                cipher_text += alphabet[new_position]
        print(f"The encoded text is: {cipher_text}")

    elif (direction == "decode"):
        plain_text = ""
        for letter in text:
            if letter not in alphabet:
                plain_text += letter
            else:
                position = alphabet.index(letter)
                new_position = position - shift
                if new_position < 0:
                    new_position = new_position + (26*((-1)*new_position // 26))
                else:
                    new_position = new_position
                plain_text += alphabet[new_position]
        print(f"\nThe decoded text is: {plain_text}")

    else:
        print("Invalid input.")

from art import logo
print(logo)

#caeser_cipher(text, shift, direction)

restart = "yes"
while restart == "yes":

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caeser_cipher(text, shift, direction)

    restart = input("\nType 'yes' to restart the cipher program or 'no' to end.\n").lower()


