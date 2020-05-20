import re

# ingredients has mixed fraction followed by unit and ingredient
recipe_line = "1 1/2 mL flour"  # change to input statement in due course

mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"

if re.matched(mixed_regex, recipe_line):
    print("true")
else:
    print("false")
    