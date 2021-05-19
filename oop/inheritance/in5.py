#Multi-Level Inheritance
#-----------------------


class Parent:
    def m1(self):
        print("Inside Parent class")

class Child(Parent):
    def m2(self):
        print("Inside Child class")

class Subclass(Child):
    def m3(self):
        print("Inside SubChild")

obj=Subclass()
obj.m3()
obj.m2()
obj.m1()