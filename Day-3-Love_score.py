# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is her name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

combined_name = name1 + name2
print("Combined name = ", combined_name)
p = combined_name.lower()

true = p.count("t") + p.count("r") + p.count("u") + p.count("e")
love = p.count("l") + p.count("o") + p.count("v") + p.count("e")

love_score = true*10 + love

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
