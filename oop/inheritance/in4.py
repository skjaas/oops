#example for Multiple Inheritance
#--------------------------------


class Person:
    def genInfo(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def printInfo(self):
        print(self.name, "\t", self.age, "\t", self.gender)

class Education:
    def eduInfo(self, degree, mark):
        self.degree = degree
        self.mark = mark

    def printEduInfo(self):
        print(self.degree, "\t", self.mark)

class Employee(Person, Education):
    def empInfo(self, empid, salary):
        self.empid = empid
        self.salary = salary

    def empPrint(self):
        print(self.empid, "\t", self.salary)

emp1 = Employee()
name = input("Name:")
age = int(input("Age:"))
gender = input("Gender:")
emp1.genInfo(name, age, gender)
emp1.printInfo()
degree = input("Degree:")
cgpa = float(input("CGPA:"))
emp1.eduInfo(degree, 7.2)
emp1.printEduInfo()
eid = int(input("ID:"))
salary = int(input("Salary:"))
emp1.empInfo(eid, salary)
emp1.empPrint()