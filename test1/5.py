class Base:
    def printDetails(self):
        print("Hello")



class Derived(Base):
    def printDetails(self):
        print("This is Child CLass!!!!!!!!!!!!!!!!!!!")


obj = Derived()
obj.printDetails()
