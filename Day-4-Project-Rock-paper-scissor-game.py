import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
player = int(
    input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer = random.randint(0, 2)
print(computer)

if player == 0:
    print("You chose:\n", rock)
elif player == 1:
    print("You chose:\n", paper)
elif player >= 3 or player < 0:
    print("Invalid input.")
else:
    print("You chose:\n", scissors)

if player > 0 and player <= 2:
    if computer == 0:
        print("Computer chose:\n", rock)
    elif computer == 1:
        print("Computer chose:\n", paper)
    else:
        print("Computer chose:\n", scissors)
else:
    print("Invalid input from the user.")


if player == computer:
    print("It's a draw.")
elif ((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)):
    print("You lose.")
elif player >= 3 or player < 0:
    print("Error!!!!")
else:
    print("You Wins.")
