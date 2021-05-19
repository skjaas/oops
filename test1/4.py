class Animal:
    def __init__(self, family, place):
        self.family = family
        self.place = place
        print("Type of the Animal:", self.family)
        print("Where commonly seems:", self.place)


class Dog(Animal):
    def details(self, number_of_legs, food):
        self.number_of_legs = number_of_legs
        self.food = food
        print("Number of Legs:", self.number_of_legs, "\nFood:", self.food)


family = input("Family:")
place = input("Place:")
legs = int(input("Number of legs:"))
food = input("Food:")
dg = Dog(family, place)
dg.details(legs, food)
