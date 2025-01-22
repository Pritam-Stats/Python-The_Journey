
def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name""" #Docstring
    if f_name == "" or l_name == "":
        return "You didn't provide any valid input."

    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"Result: {formatted_f_name} {formatted_l_name}"
# computer takes return as the end of the function

print(format_name(input("What's your first name? "), input("What's your last name? ")))

format_name()