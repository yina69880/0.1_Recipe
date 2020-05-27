# Recipe Moderniser Component 9
# Improves the experience of inserting information on the recipe into the program.

import re

# Ingredient has a mixed fraction followed by a unit and ingredient
# (Change below into input statement at a later date)

full_recipe = [
    "1 1/2 cups flour",
    "3/4 cup milk",
    "1 cup flour",
    "2 tablespoons white sugar",
    "1.5 tsp baking powder",
    "pinch of cinnamon"
]

# The regular expression that is used in splitting

mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"

# The 'for' loop that allows for constant input

for recipe_line in full_recipe:

    # Strips whitespace from the inputted recipe

    recipe_line = recipe_line.strip()

    # Checks to see if the regular expression is functional

    if re.match(mixed_regex, recipe_line):

        # Get mixed number by matching the regular expression
        pre_mixed_number = re.match(mixed_regex, recipe_line)

        # Using the group method to isolate the number
        mixed_number = pre_mixed_number.group()

        # Replace the space with a 'plus' sign:
        amount = mixed_number.replace(" ", "+")

        # Change the above string into a decimal:
        amount = eval(amount)

        # Get Unit and ingredient:
        compile_regex = re.compile(mixed_regex)

        # Inserts data gained so far into a list
        unit_ingredient = re.split(compile_regex, recipe_line)

        # Removes the extra whitespace (spaces) from a unit
        unit_ingredient = (unit_ingredient[1]).strip()

    else:

        # Splits the code at the first 'space'

        get_amount = recipe_line.split(" ", 1)

        try:

            # Converts the amount to a 'float' if possible

            amount = eval(get_amount[0])

        except NameError:

            # When no number is present:

            amount = get_amount[0]
            convert = "no"

        # Combines Unit and ingredient together

        unit_ingredient = get_amount[1]

    # Getting the unit and ingredient:

    # Splits the text at the first space
    get_unit = unit_ingredient.split(" ", 1)

    # Sets the Unit to the first item in the list
    unit = get_unit[0]

    # Sets the Ingredient to the second item in the list
    ingredient = get_unit[1]

    # Prints the Amount, Unit and Ingredient of the line

    print("{} {} {}".format(amount, unit, ingredient))



