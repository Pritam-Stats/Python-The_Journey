#from replit import clear
from artAuction import logo
import os

print(logo)
bidders = {}
restart = "yes"
while restart == "yes":
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    bidders[name] = bid
    restart = input("\nAre there any other bidders? Type 'yes' or 'no'.\n").lower()
    os.system('CLS')
    


winner = max(bidders)
print(f"The winner is {winner} with a bid of ${bidders[winner]}.")

