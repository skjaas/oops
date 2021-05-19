class Student:
    def setVal(self,id,name,dept,yr):
        self.id=id
        self.name=name
        self.dept=dept
        self.yr=yr
    def printVal(self):
        print("Id:",self.id)
        print("Name:",self.name)
        print("Dept:",self.dept)
        print("Year:",self.yr)
stud=Student()
stud.setVal(1,"Arya Aji","CSE",4)
stud.printVal()