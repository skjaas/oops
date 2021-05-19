class Person:
    def setVal(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def printVal(self):
        print(self.name)
        print(self.age)
        print(self.gender)


class Parent(Person):
    def pset(self,fathername,mothername):
        self.fathername=fathername
        self.mothername=mothername

    def pprint(self):
        print(self.fathername)
        print(self.mothername)

class Child(Person):
    def cset(self,dob,sibling):
        self.dob=dob
        self.sibling=sibling

    def cprint(self):
        print(self.dob)
        print(self.sibling)
class Student(Child):
    def sset(self,school,mark,std):
        self.school=school
        self.mark=mark
        self.std=std

    def sprint(self):
        print(self.school)
        print(self.mark)
        print(self.std)

name=input("Name:")
age=int(input("Age:"))
gender=input("Gender:")
fname=input("Father name:")
mname=input("Mother name:")
dob=input("DOB:")
sibling=input("Siblings:")
school=input("School Name:")
mark=float(input("Mark:"))
std=int(input("Class:"))

sobject=Student()
pobject=Parent()
sobject.setVal(name,age,gender)
sobject.printVal()
pobject.pset(fname,mname)
pobject.pprint()
sobject.sset(school,mark,std)
sobject.sprint()
