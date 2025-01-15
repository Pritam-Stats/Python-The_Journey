# Calculator
from art10 import logo
print(logo)
# add


def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2



operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": div,
}
def calculator():
    num1 = float(input("What's the first number?: "))
    for keys in operations:
        print(keys)

    operation = input("Pick an operation from the line above: ")
    num2 = float(input("What's the second number?: "))

    function = operations[operation]
    answer = function(num1, num2)
    print(f"{num1} {operation} {num2} = {answer}")

    restart = input(
        f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation and 'c' to close the calculator.: ").lower()



    while restart == "y":
        operation2 = input("Pick an operation: ")
        num3 = float(input("What's the next number?: "))
        function = operations[operation2]
        answer2 = function(answer, num3)
        print(f"{answer} {operation2} {num3} = {answer2}")
        answer = answer2
        restart = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation and 'c' to close the calculator.: ").lower()
    if restart == "n":
        restart = "n"
        calculator()
    else:
      greet = "Thank You."
      return greet

calculator()

# operation2 = input("Pick another operation: ")
# num3 = int(input("What's the third number?: "))

# function2 = operations[operation2]

# second_answer = function2(first_answer,num3)
# print(f"{first_answer} {operation2} {num3} = {second_answer}")
