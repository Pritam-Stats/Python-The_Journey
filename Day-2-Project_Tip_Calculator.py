# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you love to give? 10, 12, or 15? "))
total_bill = bill + bill*(tip/100)
n = int(input("How many people to split the bill? "))
p = total_bill/n

print(f"Each person should pay: ${p:.2f}")


# rounding numbers
x = 3.468
round(x,2)
x = 3.4
round(x,2) # will give 3.4 but we need 3.40

print(f"{x:.2f}")

rounded_x = "{:.2f}".format(x) #actual way to rounding numbers
print(rounded_x)