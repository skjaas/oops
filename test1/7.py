import re
f = open("file2","r")
x = "[+][9][1][0-9]{10}"
p = open("file3","w")
q = open("file3","a")
for i in f:
    i = i.rstrip("\n")
    match = re.fullmatch(x, i)
    if match is not None:
        q.write(i)
        q.write("\n")
    else:
        print(i,"is invalid")
