class Car:
    def __init__(self, reg_no, max_speed):
        self.registration_number= reg_no
        self.maximum_speed = max_speed
        self.actual_speed=0
        self.distance_travel=0

new_car= Car("Xyz123", 100)
print(f"Car registration number is {new_car.registration_number}\n",
      f"Maximum speed is {new_car.maximum_speed}\n"
    f"Actual Speed is {new_car.actual_speed}\n"
    f"Distance travelled {new_car.distance_travel}")