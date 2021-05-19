import re


#finditer takes oneby one not as a full
#fullmatcher takes the whole

# rule 1
# x = "a+"
print("Rule 1------------------")
x = "a+"
r = "aaa abc aaaa cga"
matcher = re.finditer(x, r)
for match in matcher:
    print("@[",match.start(), "] :", match.group())

# rule 2
# x = "a*"
print("Rule 2-----------------")
y = "a*"
matcher = re.finditer(y, r)
for match in matcher:
    print("@[",match.start(), "] :", match.group())


# rule 3
# x = "a?" count a as each including zero number of zero
print("Rule 3----------------------")
z = "a?"
matcher = re.finditer(z, r)
for match in matcher:
    print("@[",match.start(), "] :", match.group())


# rule 4
# x = "a{2}" consider the expression having 2a's
print("Rule 4------------------------------------")
a = "a{2}"
matcher = re.finditer(a, r)
for match in matcher:
    print("@[",match.start(), "] :", match.group())


# rule 5
# x = "a{2,3}" considering expressions having min 2a's and max 3a's
print("Rulle 5-------------------------------------")
b = "a{2,3}"
matcher = re.finditer(b, r)
for match in matcher:
    print("@[",match.start(), "] :", match.group())


# rule 6
# x = "^a" starting with a , whole string
print("Rule 6-------------------------------------")
c = "^a"
matcher = re.finditer(c, r)
for match in matcher:
    print("@[",match.start(), "] :", match.group())


# rule 7
# x = "a$" ending with a
print("Rule 7---------------------------------------")
d = "a$"
matcher = re.finditer('sda', r)
for match in matcher:
    print("@[",match.start(), "] :", match.group())
