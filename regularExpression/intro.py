# REGULAR EXPRESSION
# ------------------


# 're'(regular expression) - package used for the pattern matching
# 'finditer' used for store the matching items
# matcher = re.finditer('the pattern to be find','the pattern in which we need to perform the operation')


import re

count = 0
matcher = re.finditer("ab", "aabaabaabaabababa")
for match in matcher:
    count += 1
    print("Match available @ ", match.start()) # it return the position, the starting index of the pattern
    print("Pattern:", match.group()) # it returns the pattern found
print("Count:", count)


# Rules creation


