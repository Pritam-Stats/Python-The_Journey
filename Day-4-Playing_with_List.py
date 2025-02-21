# You are going to write a program that will mark a spot with an X.

# In the starting code, you will find a variable called map.

# This map contains a nested list. When map is printed this is what the nested list looks like:

# ['⬜️', '⬜️', '⬜️'], ['⬜️', '⬜️', '⬜️'], ['⬜️', '⬜️', '⬜️']

# In the starting code, we have used new lines(\n) to format the three rows into a square, like this:

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']

# This is to try and simulate the coordinates on a real map.


# Your job is to write a program that allows you to mark a square on the map using a two-digit system. The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:


# First, your program must take the user input and convert it to a usable format.

# Next, you need to use it to update your nested list with an "x".

# Example Input 1

# column 2, row 3 would be entered as:

# 23
# Example Output 1
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', 'X', '⬜️']







# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?as columnRow. eg. 23 means 2nd column 3rd row.: ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
digit1 = int(position) // 10  # column means inside lists
digit2 = int(position) % 10

map[digit2 - 1][digit1 - 1] = "X"


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
