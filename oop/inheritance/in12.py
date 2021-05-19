class Student:
    def __init__(self, id, name, dept, mark):
        self.id = id
        self.name = name
        self.dept = dept
        self.mark = mark
        print(self.id, self.name, self.dept, self.mark)


f = open("student2", "r")
for i in f:
    data = i.rstrip("\n").split(",")
    if int(data[3]) > 190:
        obj = Student(data[0], data[1], data[2], data[3])

