# starting with a and ending with b

import re
user_number = input(":")
x = "^a[a-zA-Z0-9\W]*b$"
match = re.fullmatch(x, user_number)
if match is not None:
    print("Valid")
else:
    print("Invalid")