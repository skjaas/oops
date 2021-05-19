class Addition:
    def operation(self,num1,num2):
        self.num1=num1
        self.num2=num2
        return (self.num1+self.num2)

ad=Addition()
num1=int(input(":"))
num2=int(input(":"))
print(num1,"+",num2,"=",ad.operation(num1,num2))


#employee class
#attr: name,id,designation,salary,company_name,etc
#setVal
#printVal
