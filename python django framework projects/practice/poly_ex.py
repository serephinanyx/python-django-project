class vehicleClass:
    def speed(self):
        print("speed of vehicle:")
class car(vehicleClass):
            def speed(self):
                vehicleClass.speed(self)
                print("180")
class bike(vehicleClass):
            def speed(self):
                vehicleClass.speed(self)
                print("80")
car=car()
car.speed()
bike=bike()
bike.speed()