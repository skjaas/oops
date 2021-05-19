#2. Multiple Inheritance
#----------------------
class Parent:
    def m1(self):
        print("Inside Parent class")

class Child:
    def m2(self):
        print("inside child")

class SubChild(Parent,Child):
    def m3(self):
        print("Inside Subchild")

obj=SubChild()
obj.m3()
obj.m2()
obj.m1()