import re
user_number = input(":")

x = "[a-zA-Z0-9\W]+"
match = re.fullmatch(x, user_number)
if match is not None:
    print("Valid")
else:
    print("Invalid")