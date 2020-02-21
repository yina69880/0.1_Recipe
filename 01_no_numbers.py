recipe_name = input("What is recipe name?")

error = "Your recipe name has numbers in it"
has_errors = ""

for letter in recipe_name:
    if letter.isdigit() == True:
        print(error)
        has_errors = "yes"

        break


if has_errors != "yes":
    print("you are OK")