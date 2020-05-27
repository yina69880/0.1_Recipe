

import csv


def general_converter(how_much, lookup, dictionary, conversion_factor):

    if lookup in dictionary:
        mult_by = dictionary.get(lookup)
        how_much = how_much * float(mult_by) / conversion_factor

        converted = "yes"

    else:
        converted = "no"

    return [how_much, converted]

# Unit Checking Function


def unit_checker():

    unit_tocheck = input("What is your unit? ")

    teaspoon = ["tsp", "teaspoon", "t", "teaspoons"]
    tablespoon = ["tbs", "tablespoon", "T", "tbsp", "tablespoons"]
    ounce = ["oz"]
    cup = ["c", "cups", "cup"]
    pint = ["p", "pt", "fl pt", "pint", "pints"]
    quart = ["q", "qt", "fl qt", "quart", "quarts"]
    milliliter = ["millilitre", "ml", "mL", "milliliter", "milliliters", "millilitres"]
    liter = ["l", "litre", "L", "litres", "liters", "liter"]
    pound = ["lb", "lbs", "#", "pound", "pounds"]

    if unit_tocheck == "":

        return unit_tocheck

    elif unit_tocheck == "T" or unit_tocheck.lower() in tablespoon:
        return "tbs"
    elif unit_tocheck.lower() in teaspoon:
        return "tsp"
    elif unit_tocheck.lower() in ounce:
        return "ounce"
    elif unit_tocheck.lower() in cup:
        return "cup"
    elif unit_tocheck.lower() in pint:
        return "pint"
    elif unit_tocheck.lower() in quart:
        return "quart"
    elif unit_tocheck.lower() in milliliter:
        return "milliliter"
    elif unit_tocheck.lower() in liter:
        return "liter"
    elif unit_tocheck.lower() in pound:
        return "pound"


unit_dictionary = {
    "tsp": 5,
    "tbs": 15,
    "cup": 237,
    "ounce": 28.35,
    "pint": 473,
    "quart": 946,
    "pound": 454,
    "liter": 1000,
    "milliliter": 1,
}

groceries = open('01_ingredients_ml_to_g.csv')


csv_groceries = csv.reader(groceries)


food_dictionary = {}


for row in csv_groceries:

    food_dictionary[row[0]] = row[1]



keep_going = ""
while keep_going == "":
    amount = eval(input("How much? "))
    amount = float(amount)

    unit = unit_checker()
    ingredient = input("Ingredient? ").lower()


    amount = general_converter(amount, unit, unit_dictionary, 1)
    print(amount)


    if amount[1] == "yes":
        amount_2 = general_converter(amount[0], ingredient, food_dictionary, 250)


        if amount_2[1] == "yes":
            print(amount_2)


        else:
            print("unchanged")

    else:
        print("unchanged")

