print("Welcome to treasure Island your mission is to find the treasure.")
direction = input("left or right?\n")
if direction.lower() == "right":
    print("Game Over.")
else:
    step2 = input("Swim or wait? \n")
    if step2.lower() == "swim":
        print("Game Over.")
    else:
        door = input("Which door? Blue, Red or Yellow.\n")
        if (door.lower() == "red") or (door.lower() == "blue"):
            print("Game Over.")
        else:
            print("Congrats, You Won!")
