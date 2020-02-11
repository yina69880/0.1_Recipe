# Get's recipes name and check that its nit blank

# Not Blank Function goes here
def not_blank(question):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            continue
        else:
            return response


# #Main routine goes here

recipe_name = input("What is the recipe name? ")

print("you are making {}".format(recipe_name))
