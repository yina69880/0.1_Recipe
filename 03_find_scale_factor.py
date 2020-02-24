









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
sf_ok = "no"
while sf_ok =="no":

    serving_size = num_check("What is the recipe serving size?")
    desired_size = num_check("How many servings are needed? ")

    scale_factor = desired_size / serving_size

    if scale_factor < 0.25:
        sf_ok = input("Warning: This scale is very small "
                  "and you might struggle to accurately weigh"
                  "the ingredients. \n"
                  "Do you want to keep going? (type 'no' to change "
                  "your desired serving size)")
    elif scale_factor > 4:
        sf_ok = input("Warning: This scale is quite large - you might "
                  "have issues with mixing bowl space / oven space. \n"
                  "Do you want to keep going? (type 'no' to change"
                  "your desired serving size)")


print("Scale Factor: {}".format(scale_factor))
