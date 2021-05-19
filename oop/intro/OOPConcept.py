#Object Oriented Programming
#---------------------------

#class: design pattern
#object: real world entity
#references: name that referce a memory location of a object

#how to create a class
#---------------------

#create using 'class' keyword
#the class name must start with capital letter
#functions within a class is known as 'method'

class Person:
    def print(self):
        print("inside print method")
#self : its the instance variable

#to use a class need to create a object of the class
pe=Person() #createing the reference
pe.print() #using the reference calling the methods


#attribute setting

class Person1:
    def print(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print("inside print method",self.name,self.age,self.gender)

pe1=Person1()
pe1.print("Arya",23,"female")

#we can create a number of objects for a class

