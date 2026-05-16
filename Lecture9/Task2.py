class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.kilometer_counter = 0

    def drive(self, hours):
        distance = self.current_speed * hours
        self.kilometer_counter += distance


class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume

tesla = ElectricCar("ABC-15", 180, 52.5)
beetle = GasolineCar("ACD-123", 165, 32.3)
tesla.current_speed = 120
beetle.current_speed = 100
tesla.drive(3)
beetle.drive(3)
print(f"Electric Car ({tesla.registration_number}) odometer: {tesla.kilometer_counter} km")
print(f"Gasoline Car ({beetle.registration_number}) odometer: {beetle.kilometer_counter} km")