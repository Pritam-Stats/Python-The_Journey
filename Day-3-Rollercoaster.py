h = float(input("Enter your height in Cm: "))
bill = 0
if h > 120:
    print("You can have a ride on the rollercoaster!\n")
    age = int(input("Enter your age: "))
    if age <= 12:
        bill = 5
    elif age < 18:
        bill = 7
    else:
        bill = 12

    if age >= 45 and age <= 55:
        bill = 0
        print("You can ride for FREE.\n")

    pics = input("Do you want photos? Y or N. - ")
    if pics == "Y":
        bill += 3

    print(f"Total bill = ${bill}")


else:
    print("Sorry, you need to grow taller to ride.")
