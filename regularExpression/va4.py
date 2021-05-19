import re
user_number = input(":")
x = "^KL\d{2}[A-Z]{2}[0-9]{4}"

match = re.fullmatch(x, user_number)
if match is not None:
    print("Valid")
else:
    print("Invalid")