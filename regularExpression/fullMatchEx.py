import re

n = "hello"
x = "\w*"
match = re.fullmatch(x, n)
if match is not None:
    print("Valid")
else:
    print("Invalid")


n = "57kg"
x = "\d{2}[a-z]{2}"
match = re.fullmatch(x, n)
if match is not None:
    print("Valid")
else:
    print("Invalid")

user_number = input(":")
x = "[0-9]{10}"
match = re.fullmatch(x, user_number)
if match is not None:
    print("Valid")
else:
    print("Invalid")
