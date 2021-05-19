class Person:
    def setval(self,name,age):
        self.name=name
        self.age=age

    def printval(self,gender="male"):
        self.gender=gender
        print("Name:",self.name) #using self we can use the variable of one function in another function
        print("Age:",self.age)
        print("Gender:",self.gender)

pe=Person()
pe.setval("Arya",23)
pe.printval("Female")
pe.setval("Anu",25)
pe.printval()