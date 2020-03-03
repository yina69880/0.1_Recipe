# Ingrdients List


# Not blank Function goes here
def not_blank(question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok != "yes":
            # look at charactere in string if it's a number
            for letter in response:
                if letter.isdigit() == True:
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
# Main routine...

# Set up empty ingredients list
ingredients = []

# Loop to ask users to enter an ingredient
stop = ""
while stop != "xxx":

    # Ask user for ingrdint (via not blank function)
    get_ingredient = not_blank("Please type in an ingredient name "
                           "This can't be left blank",
                           "yes")
    # If exit code is typed...
    if get_ingredient.lower() == "xxx" and len(ingredients) > 1:
        break

    elif get_ingredient.lower()== "xxx" and len(ingredients) <2:
        print("You need at least two ingredients in the list. "
              "Please add more ingredients.")
    # if exit code is not entered, add ingredients to list
    else:
        ingredients.append(get_ingredient)
# Check that list contains at least 2 items

# If list contains at least 2 items, break out of the loop

# If exit code is not entered, add ingredient to list

# Output list
print(ingredients)