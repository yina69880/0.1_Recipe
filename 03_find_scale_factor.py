









def num_check(question):

    Error = "Plese enter a number that is more than zero"

    valid = False
    while not valid:
        try:
            response = float(input(question))

            if response <= 0:
                print(Error)
            else:


                return response

        except ValueError:
            print(Error)
# Main routine

serving_size = num_check("What is the recipe serving size?")
desired_size = num_check("How many servings are needed? ")

scale_factor = desired_size / serving_size

print("Scale Factor: {}".format(scale_factor))
