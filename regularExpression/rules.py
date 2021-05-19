import re

# rule 1
# x = '[abc]' # either a , b or c
print("Rule 1---------------------------------------------------------------------------------------------------------")
x = '[abc]' # either a , b or c
string_find = "hdeopowsqbc jvqwwfa qax45 6@?<ADFJcdscfvacsc"
matcher = re.finditer(x, string_find)
for match in matcher:
    print("@[",match.start(), "] :", match.group())

# rule 2
# x = '[^abc]' # not a, b or c

print("Rule 2---------------------------------------------------------------------------------------------------------")
y = '[^abc]'
matcher = re.finditer(y, string_find)
for match in matcher:
    print("@[",match.start(), "] :", match.group())



# rule 3
# x = '[a-z] # considering all small letters

print("Rule 3---------------------------------------------------------------------------------------------------------")
z = '[a-z]'
matcher = re.finditer(z, string_find)
for match in matcher:
    print("@[",match.start(), "] :", match.group())


# rule 4
# x = '[A-Z]' #considering all capital letters

print("Rule 4---------------------------------------------------------------------------------------------------------")
a = '[A-Z]'
matcher = re.finditer(a, string_find)
for match in matcher:
    print("@[",match.start(), "] :", match.group())


# rule 5
# x = '[a-zA-Z]'

print("Rule 5---------------------------------------------------------------------------------------------------------")
b = '[a-zA-Z]'
matcher = re.finditer(b, string_find)
for match in matcher:
    print("@[",match.start(), "] :", match.group())


# rule 6
# x = '[0-9]' #considering all numbers

print("Rule 6---------------------------------------------------------------------------------------------------------")
c = '[0-9]'
matcher = re.finditer(c, string_find)
for match in matcher:
    print("@[",match.start(), "] :", match.group())


# rule 7
# x = '[^a-zA-Z0-9]' to  check symbols

print("Rule 7---------------------------------------------------------------------------------------------------------")
d = '[^a-zA-Z0-9]'
matcher = re.finditer(d, string_find)
for match in matcher:
    print("@[",match.start(), "] :", match.group())

# rule 8
# x = '\s' to check space

print("Rule 8-----------------------------------")
e = '\s'
matcher = re.finditer(e, string_find)
for match in matcher:
    print("@[",match.start(), "] :", match.group())


# rule 9
# x = '\d' to check digits
print("Rule 9-----------------------------------")
f = '\d'
matcher = re.finditer(f, string_find)
for match in matcher:
    print("@[",match.start(), "] :", match.group())


# rule 10
# x = '\D' to check all except digits
print("Rule 10-----------------------------------")
g = '\D'
matcher = re.finditer(g, string_find)
for match in matcher:
    print("@[",match.start(), "] :", match.group())


# rule 11
# x = '\w' to check words except

print("Rule 11-----------------------------------")
h = '\w'
matcher = re.finditer(h, string_find)
for match in matcher:
    print("@[",match.start(), "] :", match.group())



# rule 12
# x = '\W' to check special characters

print("Rule 12-----------------------------------")
i = '\W'
matcher = re.finditer(i, string_find)
for match in matcher:
    print("@[",match.start(), "] :", match.group())