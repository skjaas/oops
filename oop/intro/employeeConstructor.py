class Employee:
    company="Luminar"
    def __init__(self,id,name,designation,salary):
        self.id=id
        self.name=name
        self.designation=designation
        self.salary=salary
    def printVal(self):
        print("Id:",self.id,"\nName:",self.name)
        print("Designation:",self.designation,"\nSalary:",self.salary)

emp=Employee(23,"Saint","HR Manager",25000)
emp.printVal()