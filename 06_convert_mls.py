# ask user for amount
# ask user for unit
# check that unit is in dictionary

# if unit in dictionary, convert to mL

# if no unit given / unit is unknown, leave as is.


# Function goes here
def unit_checker():

    unit_tocheck = input("Unit? ")

    # Abbreviation lists
    teaspoon = {"tsp", "teaspoon", "t"}
    tablespoon = {"tbs", "tablespoon", "T", "tbsp"}
    cup = {"cup", "C", "c"}
    ounce = { "O", "oz", "ounce"}
    pint = {"p", "pt"}
    quart = {"q", "qt"}
    pound = {"lb", "pound", "#"}



    if unit_tocheck == "":
        print("you chose {}".format(unit_checker))
        return unit_checker

    elif unit_tocheck == "T" or unit_tocheck.lower() in tablespoon:
        return "tbs"
    elif unit_tocheck.lower() in teaspoon:
        return "tsp"
    elif unit_tocheck.lower() in cup:
        return "cup"
    elif unit_tocheck.lower() in ounce:
        return "oz"
    elif unit_tocheck.lower() in pint:
        return "pt"
    elif unit_tocheck.lower() in quart:
        return "qt"
    elif unit_tocheck.lower() in pound:
        return "lb"

# Main routine goes here
unit_central = {
    "tsp": 5,
    "tbs": 15,
    "cup": 237,
    "ounce": 28.35,
    "pint": 473,
    "quart": 946,
    "pound" : 454
}


keep_going = ""
while keep_going == "":
    amount = eval(input("How much? "))
    amount = float(amount)
    # get unit and change it to match dictionary
    unit = unit_checker()

    if unit in unit_central:
        mult_by = unit_central.get(unit)
        amount = amount * mult_by
        print("Amount in mL {}".format(amount))
    else:
        print("{} is unchanged".format(amount))

    keep_going = input("<enters> or q ")