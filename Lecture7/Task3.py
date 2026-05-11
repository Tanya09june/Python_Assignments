class Car:
    def __init__(self, make, model, year, current_speed=0, travelled_distance=0):
        self.make = make
        self.model = model
        self.year = year
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

    def accelerate(self, amount):
        self.current_speed += amount

    def brake(self, amount):
        self.current_speed = max(0, self.current_speed - amount)

    def __str__(self):
        return (f"{self.year} {self.make} {self.model} | "
                f"Speed: {self.current_speed} km/h | "
                f"Distance Travelled: {self.travelled_distance} km")


car = Car("Toyota", "Camry", 2022)

car.accelerate(60)
print(car)

car.drive(1.5)
print(car)

car.accelerate(40)
print(car)

car.drive(2)
print(car)

car.brake(30)
print(car)