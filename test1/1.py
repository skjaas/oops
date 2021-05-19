class Vehicle:
    def tyre(self, design, type):
        self.design = design
        self.type = type
        print("Tyre Details")
        print("Design:", self.design, "\tType:", self.type)

    def speed(self, min_speed, max_speed):
        self.min_speed = min_speed
        self.max_speed = max_speed
        print("Minimum speed:", self.min_speed, "\tMaximum speed:",self.max_speed)


class Bus(Vehicle):
    def details(self, model, price, date):
        self.model = model
        self.price = price
        self.date = date
        print("General Details")
        print("Model:", self.model, "\tPrice:", self.price, "\tDate of Purchase:", self.date)


volvo = Bus()
model = input("Model Name:")
price = input("Price:")
date = input("Date of Purchase")
min_speed = input("Minimum Speed:")
max_speed = input("Maximum Speed:")
type = input("Tyre Type:")
design = input("Tyre Design:")
volvo.details(model, price, date)
volvo.tyre(design, type)
