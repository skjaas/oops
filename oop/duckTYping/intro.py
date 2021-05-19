# functionality has more importance than the class

class Swift:
    def start(self):
        print("Swift car starts")

    def accelerate(self):
        print("Swift car accelerating functionality")

    def breaks(self):
        print("Swift car break method")

    def stop(self):
        print("Swift car stooping")


class Seltos:
    def start(self):
        print("Seltos car starts")

    def accelerate(self):
        print("Seltos car accelerating functionality")

    def breaks(self):
        print("Seltos car break method")

    def stop(self):
        print("Seltos car stooping")


class Person:
    def drive(self,car):
        car.start()
        car.accelerate()
        car.breaks()
        car.stop()


p = Person()
sw = Swift()
p.drive(sw)
