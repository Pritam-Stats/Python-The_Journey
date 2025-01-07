# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomized:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# My code ------->
password = ""
for j in range(1, nr_letters + 1):
    i = random.randint(0, len(letters)-1)  # or just use random.choice(letters)
    password += letters[i]
for j in range(1, nr_symbols + 1):
    s = random.randint(0, len(symbols)-1)  # or just use random.choice(symbols)
    password += symbols[s]
for k in range(1, nr_numbers + 1):
    n = random.randint(0, len(numbers)-1)  # or just use random.choice(numbers)
    password += str(numbers[n])
print(password)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_password = ""

hard_password_list = random.sample(password, len(password))

for i in range(0, len(hard_password_list)):
    hard_password += hard_password_list[i]


print(hard_password)


# # ma'am code ------->

# password_list = []
# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))
# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)
# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)
# print(password_list)
# random.shuffle(password_list)
# print(password_list)

# password2 = ""
# for char in password_list:
#   password2 += char

# print(password2)
