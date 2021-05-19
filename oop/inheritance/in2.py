#Person-Employee program for Single-Inheritance
#8962 passsword

class Person:
    def generalInfo(self,name,age,gender,address):
        self.name=name
        self.age=age
        self.gender=gender
        self.address=address
    def printInfo(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
        print("Address:",self.address)

class Employee(Person):
    def empDetails(self,empId,designation,department):
        self.empId=empId
        self.designation=designation
        self.department=department

    def empPrintInfo(self):
        print("Employee ID:",self.empId)
        print("Designation:",self.designation)
        print("Department:",self.department)


emp1=Employee()
emp1.generalInfo("Arya",23,"female","thiruvalla")
emp1.printInfo()
emp1.empDetails(12,"python developer","IT")
emp1.empPrintInfo()