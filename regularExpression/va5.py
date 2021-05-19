import re
user_number = input(":")
# x = "^[a-z0-9_]+@[a-z.]+[a-z]+"
x = "[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+"

match = re.fullmatch(x, user_number)
if match is not None:
    print("Valid")
else:
    print("Invalid")