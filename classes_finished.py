class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed


class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.engine = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.engine, "Car at ", self.speed)


class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        if (hassidecar):
            self.wheels = 2
        else:
            self.wheels = 3
        self.doors = 0
        self.engine = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.engine, "motorcycle at ", self.speed)

class Bike(Vehicle):
    def __init__(self, type_bike):
        if(type_bike == "unicycle"):
            self.tire = 1
        if(type_bike == "bicycle"):
            self.tire = 2
        if(type_bike == "tricycle"):
            self.tire = 3
    
    def drive(self, speed):
        super().drive(speed)
        print("riding with my", self.tire, "tired bike at ", self.speed)


car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle("gas", True)
bike1 = Bike("bicycle")

bike1.drive(30)
print(mc1.wheels)
print(car1.engine)
print(car2.doors)

bike1.drive(10)
car1.drive(30)
car2.drive(40)
mc1.drive(50)