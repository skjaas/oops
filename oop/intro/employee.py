
#employee class
#attr: name,id,designation,salary,company_name,etc
#setVal
#printVal


class Employee:
    company="Luminar Tehnolab" #static variable
    def setVal(self,id,name,designation,salary):
        self.id=id
        self.name=name
        self.designation=designation
        self.salary=salary

    def printVal(self):
        print("ID:",self.id,"\nName:",self.name)
        print("Designation:",self.designation,"\nSalary:",self.salary)
        print("Company Name:",Employee.company)


emp1=Employee()
emp1.setVal(1,"Arya Aji","Python Developer",25000)
emp1.printVal()

#types of variable-2
#1.Static Variable: related to class-called using class name
#eg.Employee.company
#2.Instant variable: related to methods-called using self
#eg.self.id,self.name,self.designation