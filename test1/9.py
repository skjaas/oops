import re

test_string = input("Enter String:")
x = "^[A-Z][a-z]+"
match = re.fullmatch(x, test_string)
if match is not None:
    print(test_string, "is a valid string")
else:
    print(test_string, "is invalid string")