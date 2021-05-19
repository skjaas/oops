class Student:
    def __init__(self, name, roll_no, department, mark):
        self.name = name
        self.roll_no = roll_no
        self.department = department
        self.mark = mark
        print("Name:", self.name,"\tRoll Number:", self.roll_no, "\tDepartment:", self.department, "\tMark:", self.mark)


f = open("file1","r")
dic = {}
for i in f:
    data = i.rstrip("\n").split(",")
    index = data[1]
    dic[index] = data

mark_lst = dic["1"]
max_mark = mark_lst[3]
max_index = "1"
for i in dic:
    index = i
    lst = dic[index]
    if (int(lst[3]) > int(max_mark)):
        max_mark = lst[3]
        max_index = i

lst = dic[max_index]
name = lst[0]
roll_no = lst[1]
department = lst[2]
mark = lst[3]
obj = Student(name, roll_no, department, mark)
