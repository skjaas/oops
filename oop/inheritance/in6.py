# Example for Multi-Level Inheritance

class Science:
    def sciPrint(self):
        print("Father of all invents")


class Physics(Science):
    def phyPrint(self):
        print("Laws of Physics")


class Motion(Physics):
    def motionPrint(self):
        print("Newtons 1st Law")


obj = Motion()
obj.motionPrint()
obj.phyPrint()
obj.sciPrint()
