#constructors used for the initialization of instant variables

class Person:
    def __init__(self,name,age,gender): #init (initialization) constructor
        self.name=name
        self.age=age
        self.gender=gender

    def printVal(self):
        print("Name:",self.name,"\nAge:",self.age,"\nGender:",self.gender)

pe=Person("Saint",28,"Male")
#pe.setVal("Saint",28,"Male")
pe.printVal()


#use of constructor

#constructor automatically invokes when the class called