class Book:
    def __init__(self, bname, aname, publisher, price, generic):
        self.bname = bname
        self.aname = aname
        self.publisher = publisher
        self.price = price
        self.generic = generic

    def printdetails(self):
        print("Name:", self.bname)
        print("Author:", self.aname)
        print("Type:", self.generic)
        print("Price:", self.price)
        print("Publisher:", self.publisher)

# 'to string' method
    def __str__(self):
        return self.bname
# the function used to print a string value instead of printing an object address
# with out using __str__ print(object) only prints the address of the object


bname = input("Book Name:")
aname = input("Author Name:")
type = input("Type:")
price = int(input("Price of the book:"))
pub = input("Publisher:")
bo = Book(bname, aname, pub, price, type)
bo.printdetails()
print(bo)
# prints the string value