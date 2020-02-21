# Get's source of recipe name and check it is not blank

#To do
#allow users to specify a custom error message
#Allow users to specify whether numbers are allowed


# Not Blank Function goes here
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


# #Main routine goes here

source = not_blank("What is the recipe name?",
                   "The recipe source can't be blank",
                   "yes")

print("you are making {}".format(source))
