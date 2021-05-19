class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        print("****************GENERAL INFORMATIONS*****************")
        print("Name:", self.name, "\nAge:", self.age, "\nHeight:", self.height, "\nWeight:", self.weight)


class Father(Person):
    def fatherDetails(self, father_name, father_age, father_occupation):
        self.father_name = father_name
        self.father_age = father_age
        self.father_occupation = father_occupation
        print("_______________FATHER'S DETAILS___________________")
        print("Name of Fathe:", self.father_name, "\nFathers Age:", self.father_age, "\n Fathers Occupation:", self.father_occupation)


class Mother(Person):
    def motherDetails(self, mother_name, mother_age, mother_occupation):
        self.mother_name = mother_name
        self.mother_age = mother_age
        self.mother_occupation = mother_occupation
        print("_______________MOTHER'S DETAILS___________________")
        print("Name of Mothe:", self.mother_name, "\nMothers Age:", self.mother_age, "\n Mothers Occupation:", self.mother_occupation)


class Child(Father,Mother):
    def childDetails(self,occupation):
        self.occupation = occupation
        print("Occupation:", self.occupation)

name = input("Name:")
age = int(input("Age:"))
height = input("Height:")
weight = input("Weight:")
occupation = input("Occupation of the Child:")
fname = input("Fathers Name:")
fage = input("Fathers Age:")
foccupation = input("Fathers Occupation")
mname = input("Mothers Name:")
mage = input("Mothers Age:")
moccupation = input("Mothers Occupation:")
ch1 = Child(name, age, height, weight)
ch1.childDetails(occupation)
ch1.fatherDetails(fname, fage, foccupation)
ch1.motherDetails(mname, mage, moccupation)

