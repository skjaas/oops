class Student:
    school_name="GGHSS Peringara"
    def setVal(self,rollno,name,std,total_mark):
        self.rollno=rollno
        self.name=name
        self.std=std
        self.total_mark=total_mark

    def printVal(self):
        print("Roll No:",self.rollno)
        print("Name:",self.name)
        print("STD:",self.std)
        print("School Name:",Student.school_name)
        print("Total Mark:",self.total_mark)

stud1=Student()
stud1.setVal(1,"Arya Aji",12,500)
stud1.printVal()
stud2=Student()
stud2.setVal(2,"Aswathi Anil",12,550)
stud2.printVal()