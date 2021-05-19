#inheritance
#python supports 3 types of inheritance
#1.Single-level inheritance : When the child class inherits from only one parent class
#2.Multiple-level inheritance : When the child class inherits from multiple parent classes
#3.Hierarchical inheritance : When more than one class is derived from the single base class
#4.Hybrid inheritance : Hybrid inheritance is a combination of multiple inheritance and multilevel inheritance
#.............................................................................................................................



#1. Single Inheritance
#--------------------------------------------------------------------------


#Here Person parent class has only one child class "Student" class
#hence it is known as the single inheritance

class Person: #parent class,base class,super class
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def printDetails(self):
        print(self.name,"\n",self.age,"\n",self.gender)


class Student(Person): #child class,sub class,derived class
    def det(self,rollno,school):
        self.rollno=rollno
        self.school=school
    def prints(self):
        print(self.rollno,"\n",self.school)

per=Person()
per.details("Arya",23,"female")
per.printDetails()
st=Student()
st.det(11,"GGHSS Peringara")
st.prints()
st.details("Aswathi",24,"female")
st.printDetails()