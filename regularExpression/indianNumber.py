import re
user_number = input(":")
x = "(\+91)?[0-9]{10}"
# x = "[+][9][1]\d{10}"
match = re.fullmatch(x, user_number)
if match is not None:
    print("Valid")
else:
    print("Invalid")