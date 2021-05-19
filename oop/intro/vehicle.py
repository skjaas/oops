class Vehicle:
    def speed(self,velocity):
        self.velocity=velocity
        return (self.velocity)

car=Vehicle()
print("Car speed:",car.speed(40))
bike=Vehicle()
print("Bike speed:",bike.speed(120))



