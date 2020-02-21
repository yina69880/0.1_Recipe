# Get's recipes name and check that its nit blank


# Not Blank Function goes here
def not_blank(question):
    error = "Your recipe name has numbers in it"

    valid = False
    while not valid:
        has_errors = ""
        response = input(question)

        for letter in response:
            if letter.isdigit():
                has_errors = "yes"
                break

        if response == "":
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response


# #Main routine goes here

recipe_name = not_blank("What is the recipe name? ")

print("you are making {}".format(recipe_name))
