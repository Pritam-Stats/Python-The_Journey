# user defined function
def prime_checker(number):
    count = 0

    if(number <= 0):
        print("Invalid input.")

    else:
        for i in range(1, number+1):
            if (number % i == 0):
                count += 1

    if (count == 2):
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


# Calling the function
n = int(input("Check this number: "))
prime_checker(number=n)
