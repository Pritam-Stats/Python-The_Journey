import random
from tkinter import BitmapImage # random is a module in python
random_integer = random.randint(1,10) # between 1 to 10 inclusively
print("Random integer: ",random_integer)

random_float = random.random() # this always gives a value between [0,1)
print("Random float: ",random_float)

# Now how do we print any random float

print(type(random.random() + random.randint(1,4))) # My approach

# similarly another approach can be multiply the random_float to 5

# Yesterday's reference 
love_score = random.randint(1,100)
print(f"Your love score is {love_score}.")