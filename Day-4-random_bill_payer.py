
import random
# 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. then single space. eg. A, B, C, D, E\n")
names = names_string.split(", ") # splits the words which are separated by (", ") this format and makes a list
# 🚨 Don't change the code above 👆
print(f"\nYour input: {names_string}\n")
print("After names_string.split(", ") effect: ", names , "- its a list.\n")


#Write your code below this line 👇
n = len(names) #length of the name list

i = random.randint(0, n-1) #random indexes for list

random_name = names[i]

print(f"{random_name} is going to buy the meal today!")
