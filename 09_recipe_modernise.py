# modules to be used...
import csv

# ***** Function goes here *****

def not_blank(question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok != "yes":

            for letter in response:
                if letter.isdigit():
                 has_errors = "yes"
                 break

        if response == "":
            print(error)
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response

# ***** Main routine *****

# set up dictionaries

# set up list to hold 'modernised' ingredients

# ask user for recipe name and check its not blank
source = not_blank("What is the recipe name?",
                   "The recipe source can't be blank and can't contain numbers,",
                   "no")
# ask user where the recipe is originally from (number OK)
source = not_blank("Where is the recipe from?",
                   "The recipe source can't be blank",
                   "yes")


# get serving sizes and scale factor

# Loop for each ingredient...

# get ingredient amount
# get ingredient name
# get unit
# convert unit to mL
# convert mL to g
# Put updated ingredients in list

# Output ingredient list

