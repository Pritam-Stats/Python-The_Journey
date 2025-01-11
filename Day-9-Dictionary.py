# # Dictionaries

# definition_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }

# print(definition_dictionary)
# # syntax of dictionaries = {"Key": Value}

# # dictionaries identified by their key instead of index

# #print(definition_dictionary["Bug"])

# # Adding new items in dictionaries

# definition_dictionary["Loop"] = "The action of doing something over and over again."
# print(definition_dictionary)

# # Create empty dictionary
# empty_dictionary = {}

# # Wipe an existing dictionary
# # definition_dictionary = {} # clear out the existing dictionary
# # print(definition_dictionary)

# # Edit an item in a dictionary
# # definition_dictionary["Bug"] = "A moth in our computer."
# # print(definition_dictionary)

# # Loop through a dictionary
# for key in definition_dictionary:
#     print(key) # gives key
#     print(definition_dictionary[key]) # to get the value


# Nesting list and dictionaries
# we can also put a list also a dict as the value inside a dictionary

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting list in a dictionary
travel_log1 = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#print(travel_log1["France"])


# Nesting dictionary to a dictionary
# dictionaries inside each key of the main dictionary
# i.e., each value is itself a dictionary of the main dict
travel_log2 = {
    "France": {
        "Cities_Visited": ["Paris", "Lille", "Dijon"], "total_visits": 12
        },
    "Germany": {
        "Cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5
        },
}


# Nesting Dictionaries inside a list

travel_log3 = [
    {
        "country": "India",
        "Cities":  ["Siliguri", "Kolkata", "Mumbai",            "Bangalore", "Chennai", "Delhi"],
        "total_visits": 2
    },
    {
        "Country": "USA",
        "Cities": ["Massachusets", "New York"],
        "total_visits":0,
    },
]
print(travel_log3[0]["country"])