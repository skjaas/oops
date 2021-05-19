#overloading
#-----------
#same method name for both parent class and child class
#different parameters
#depending on the number of parameters it will decide which method should call


class Student:
    def set(self, name, number, department, mark):
        self.name = name
        self.number = number
        self.department = department
        self. mark = mark
        print(self.name, self.number, self.department, self.mark)


class Child(Student):
    def set(self, student_name, student_age):
        self.student_name = student_name
        self.student_age = student_age
        print(self.student_name, self.student_age)


ch=Child()
ch.set("Arya",23)
#ch.set("Saint",28,"management",350) python not supporting method oveloading