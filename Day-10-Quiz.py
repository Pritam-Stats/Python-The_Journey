# What will be the output
def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)


result = outer_function(5, 10)
print(result)

#What will be printed in the console after running the following code?
# The return keyword will exit the function and prevent the rest of the code being executed.
def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"


print(my_function(25))


# difference bw return and print
