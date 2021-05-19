class Person:
    def printHai(self,a,b):
        self.a = a
        self.b = b
        print(self.a,self.b)


class Child(Person):
    def printHai(self,d,e):
        self.d = d
        self.e = e
        print("Haiiiiiii")


ch=Child()
ch.printHai(4,5)