class Employee:
    def __init__(self, eid, name, designation):
        self.eid = eid
        self.name = name
        self.designation = designation
        print(self.eid, "\t", self.name, "\t", self.designation)

    def __str__(self):
        return self.name + str(self.eid)


name = input("Name:")
eid = int(input("Employee ID:"))
designation = input("Designation:")

emp1 = Employee(eid, name, designation)
print(emp1)
