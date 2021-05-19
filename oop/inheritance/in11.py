class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printVal(self):
        print(self.name, "\t", self.age)


f = open("student", "r")

for i in f:
    data = i.rstrip("\n").split(",")
    st=Student(data[0], data[1])
    st.printVal()
