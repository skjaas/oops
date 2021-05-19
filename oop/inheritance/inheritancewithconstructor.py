class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    # def printVal(self):
    #     print("Name:",self.name)
    #     print("Age:",self.age)
class Student(Person):
    def __init__(self,rollno,mark,name,age):
        super().__init__(name,age)#calling super class's construcotor
        self.rollno=rollno
        self.mark=mark
    def prints(self):
        print(self.rollno)
        print(self.mark)
        print(self.name)
        print(self.age)
cr=Student(2,34,"Arya",23)
#cr.printVal()
cr.prints()