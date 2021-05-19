# combination of lower case and upper case ending with a number

import re
user_number = input(":")
x = "\[a-zA-z]+\d{1}$"
match = re.fullmatch(x, user_number)
if match is not None:
    print("Valid")
else:
    print("Invalid")