import re
user_number = input(":")
x = "[\D]{8,15}"

match = re.fullmatch(x, user_number)
if match is not None:
    print("Valid")
else:
    print("Invalid")