class Calculator:

    def addition(self,num1,num2):
        self.a=num1
        self.b=num2
        return (self.a+self.b)
    def sub(self,num1,num2):
        self.a=num1
        self.b=num2
        return (self.a-self.b)

    def mul(self,num1,num2):
        self.a=num1
        self.b=num2
        return (self.a*self.b)
    def div(self,num1,num2):
        self.a=num1
        self.b=num2
        return (self.a/self.b)

    def modu(self,num1,num2):
        self.a=num1
        self.b=num2
        return (self.a%self.b)


obj=Calculator()
n=1
while(n==1):
    print("1.Add 2.Sub 3.Mul 4.Div 5.Mod 0.End")
    choice=int(input(":"))
    if (0<choice<6):
        a=float(input("Num1:"))
        b=float(input("Num2:"))
        if choice==1:
            print(obj.addition(a,b))
        elif choice==2:
            print(obj.sub(a,b))

        elif choice==3:
            print(obj.mul(a,b))

        elif choice==3:
            print(obj.div(a,b))

        elif choice==4:
            print(obj.modu(a,b))

    else:
        print("Process Ending")
        n=2



#or




class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b

a=float(input(":"))
b=float(input(":"))
obj=Calculator(a, b)
print(obj.add())
print(obj.sub())
print(obj.mul())
print(obj.div())




#homewor

#book class