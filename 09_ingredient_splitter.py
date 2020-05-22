import re

# ingredients has mixed fraction followed by unit and ingredient
recipe_line = "1 1/2 mL flour"  # change to input statement in due course

mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"

if re.match(mixed_regex, recipe_line):
    print("true")
    # Get mixed number by matching the regx
    pre_mixed_num = re.match(mixed_regex, recipe_line)
    mixed_num = pre_mixed_num.group()

    # Replace space with a + sign
    amount = mixed_num.replace(" ", "+")
    # change the string into a decimal
    amount = eval(amount)
    print(amount)

    # get unit and ingredient...
    compile_regex = re.compile(mixed_regex)
    print(compile_regex)
    unit_ingredient = re.split(compile_regex, recipe_line)




