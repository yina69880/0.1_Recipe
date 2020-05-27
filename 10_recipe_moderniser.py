
import csv
import re

# ***** Functions *****

def not_blank(question, error_message, number_okay):
    error = error_message


    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        # Checks if the user has allowed numbers in their source

        if number_okay != "yes":
            # Look at each character in string, if any characters are numbers, give an error
            for letter in response:
                if letter.isdigit() == True:
                    has_errors = "yes"
                    break

        if response == "":
            print(error)
            continue
        elif has_errors != "":
            print()
            print(error)
            print()
            continue

        else:
            return response

# Number Checking Function:
# (Makes sure that the number is a 'float' that is more than zero (0))


def number_checker(question):

    error = "Please enter a number that is more than zero."

    valid = False
    while not valid:

        try:
            response = float(input(question))

            if response <= 0:
                print(error)

            else:

                return response

        except ValueError:
            print(error)

# Getting Scale Factor Function


def get_scale_factor():

    current_size = number_checker("How many servings does the recipe currently make? ")
    sf = ""

    # Main Routine Goes Here

    enter_scale_factor = "yes"
    while enter_scale_factor == "yes":

        desired_size = number_checker("How many servings would you like to make? ")

        sf = desired_size / current_size

        # If the scale factor is less than 0.25, warn the user

        if sf < 0.25:
            enter_scale_factor = input("Warning: This scale factor is very small, "
                                       "which might make it hard to measure accurately. \n"
                                       "You might want to make the original recipe and keep leftovers. \n"
                                       "Do you want to fix this and make more servings? ").lower()

        # If the scale factor is more than 4, warn the user

        elif sf > 4:
            enter_scale_factor = input("Warning: This scale factor is very large, "
                                       "which might not scale accurately to the average kitchen. \n"
                                       "You might want to make the original recipe in multiple batches. \n"
                                       "Do you want to fix this and make less servings? ").lower()

        # If none of these are the case, return the scale factor

        else:
            enter_scale_factor = "no"

    return sf


# General Dictionary Checking Function

# Checks if the unit is in the dictionary

def general_converter(how_much, lookup, dictionary, conversion_factor):

    if lookup in dictionary:

        multiply_by = dictionary.get(lookup)
        how_much = how_much * float(multiply_by) / conversion_factor
        # print("Amount in milliliters: {}".format(how_much))

        converted = "yes"

    else:

        converted = "no"

    return [how_much, converted]

# Unit Checking Function


def unit_checker(unit_to_check):

    # Abbreviation Lists for various measurements

    teaspoon = ["tsp", "teaspoon", "t", "teaspoons"]
    tablespoon = ["tbs", "tablespoon", "T", "tbsp", "tablespoons"]
    ounce = ["oz", "fluid ounce", "fl oz", "floz", "fluid ounces", "ounce", "ounces"]
    cup = ["c", "cups", "cup"]
    pint = ["p", "pt", "fl pt", "pint", "pints"]
    quart = ["q", "qt", "fl qt", "quart", "quarts"]
    milliliter = ["millilitre", "ml", "cc", "mL", "milliliter", "milliliters", "millilitres"]
    liter = ["l", "litre", "L", "litres", "liters", "liter"]
    deciliter = ["dl", "decilitre", "dL", "decilitres"]
    pound = ["lb", "lbs", "#", "pound", "pounds"]
    stick = ["knob"]
    grams = ["g", "gram", "grams"]

    if unit_to_check == "":

        # print("You choose {}".format(unit_to_check))
        return unit_to_check

    elif unit_to_check.lower() in grams:

        return "g"

    elif unit_to_check == "T" or unit_to_check.lower() in tablespoon:

        return "tbs"

    elif unit_to_check.lower() in teaspoon:

        return "tsp"

    elif unit_to_check.lower() in ounce:

        return "ounce"

    elif unit_to_check.lower() in cup:

        return "cup"

    elif unit_to_check.lower() in pint:

        return "pint"

    elif unit_to_check.lower() in quart:

        return "quart"

    elif unit_to_check.lower() in milliliter:

        return "milliliter"

    elif unit_to_check.lower() in liter:

        return "liter"

    elif unit_to_check.lower() in deciliter:

        return "deciliter"

    elif unit_to_check.lower() in pound:

        return "pound"

    elif unit_to_check.lower() in stick:

        return "stick"

# Main Routine

# Building list of milliliter unit conversions


unit_dictionary = {
    "tsp": 5,
    "tbs": 15,
    "cup": 237,
    "ounce": 28.35,
    "pint": 473,
    "quart": 946,
    "pound": 454,
    "stick": 113,
    "liter": 1000,
    "milliliter": 1,
    "deciliter": 100,
}

# Food Dictionary:


# Opens the Dictionary File

groceries = open('01_ingredients_ml_to_g.csv')

# Insert data into a list

csv_groceries = csv.reader(groceries)

# Create a dictionary to hold the data

food_dictionary = {}

# Add the data from the list (from the csv file) into the dictionary
# Note: The first item in a row is the ingredient, while the next is the amount of the ingredient in grams

for row in csv_groceries:

    food_dictionary[row[0]] = row[1]

# Prints the dictionary as a whole (Useful for testing, but ultimately removed)

# print(food_dictionary)

# Ingredient Getting Function:
# (Function also checks the amount, units and ingredients to see if they are valid)


def get_all_ingredients():

    # Creates an empty list to eventually contain ingredients

    all_ingredients = []

    stop = ""

    # Tells users information at the beginning of the loop

    print()
    print("Please enter ingredients one at a time, and enter 'xxx' when you have finished entering ingredients ")

    # Loop asking users to enter an ingredient

    while stop != "xxx":

        # Ask user for ingredients (via blank checker)

        get_ingredient = not_blank("Please Enter amount, unit and ingredient: ",
                                   "This can't be blank",
                                   "yes")

        # Check to see if exit code is typed...
        # ...and check that the list contains at lest two valid items.

        if get_ingredient.lower() == "xxx" and len(all_ingredients) > 1:
            break

        # If less than two ingredients are inserted into th list, show an error message

        elif get_ingredient.lower() == "xxx" and len(all_ingredients) < 2:
            print("You need at least two ingredients in the list. "
                  "Please enter more ingredients. ")

        # If exit code is not entered, add ingredient to list

        else:
            all_ingredients.append(get_ingredient)

    return all_ingredients

# Main Routine:


modernised_recipe = []


recipe_name = not_blank("What is the name of your recipe? ",
                        "The recipe name cannot be blank, and cannot contain numbers.",
                        "no")


recipe_source = not_blank("Where is your recipe from? ",
                          "The recipe source cannot be blank, but may have numbers.",
                          "yes")



scale_factor = get_scale_factor()



full_recipe = get_all_ingredients()



mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"


for recipe_line in full_recipe:
    recipe_line = recipe_line.strip()

    # get amount
    if re.match(mixed_regex, recipe_line):

        # Get mixed number by matching the regex
        pre_mixed_number = re.match(mixed_regex, recipe_line)
        mixed_number = pre_mixed_number.group()

        # replace with a + sign
        amount = mixed_number.replace(" ", "+")

        # change string into decimal
        amount = eval(amount)
        amount = amount * scale_factor

        # Get unit and ingredient
        compile_regex = re.compile(mixed_regex)
        unit_ingredient = re.split(compile_regex, recipe_line)
        unit_ingredient = (unit_ingredient[1]).strip()

    else:
        get_amount = recipe_line.split(" ", 1)

        try:
            amount = eval(get_amount[0])
            amount = amount * scale_factor
        except NameError:
            amount = get_amount[0]
            modernised_recipe.append(recipe_line)
            continue


        unit_ingredient = get_amount[1]

    # get unit and ingredient...
    get_unit = unit_ingredient.split(" ", 1)    # splits text at first space

    unit = get_unit[0]
    # convert into ml

    num_spaces = recipe_line.count(" ")
    if num_spaces > 1:
        ingredient = get_unit
        # convert into g
    else:
        modernised_recipe.append("{} {}".format(amount, unit_ingredient))
        continue

    modernised_recipe.append("{} {} {}".format(amount, unit_ingredient))

# put updated ingredient in list

# Output ingredient list
for item in modernised_recipe:
    print(item)
