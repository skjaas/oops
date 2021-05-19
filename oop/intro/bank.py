#1.acc create
#personal details
#2.deposite
#3.withdraw

class Bank:
    Bank_name="SBI"
    min_bal=500
    def acc_create(self,name,age,acc_no):
        self.name=name
        self.age=age
        self.acc_no=acc_no
        self.bal=Bank.min_bal
        print("UserName:",self.name)
        print("Account No:",self.acc_no)
        print("Bank Name:",Bank.Bank_name)
        print("Your Current Balance:",self.bal)

    def deposite(self,name,acc_no,damount=0):
        self.name=name
        self.acc_no=acc_no
        self.amount=damount
        self.bal=Bank.min_bal+self.amount
        print("Available Balance:",self.bal)

    def withdraw(self,name,acc_no,wamount=0):
        self.wamount=wamount
        if(self.bal>=wamount):
            print("Success!!!\nBalance:",self.bal-self.wamount)
        else:
            print("Available balance less than withdraw amount")

holder1=Bank()
holder1.acc_create("Arya Aji",23,5467858955)
print()
holder1.deposite("Arya Aji",5467858955,5000)
print()
holder1.withdraw("Arya Aji",5467858955,2500)