# method overriding
# -----------------

# same method name and same arguments for parent class and child

class Parent:
    def properties(self):
        print("Hello hai")

    def marry(self):
        print("with abc")



class Child:
    def marry(self):
        print("with xyz")


c = Child()
c.marry()





