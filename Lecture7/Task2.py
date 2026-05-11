class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_speed):

        updated_speed = self.current_speed + change_speed #variable for store value

        if updated_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed


        elif updated_speed < 0: #speed 0
            self.current_speed = 0


        else:
            self.current_speed = updated_speed #updated speed


new_car = Car("ABC-123", 100)
new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)

print(f"Registration Number: {new_car.registration_number}\n"
      f"Maximum Speed: {new_car.maximum_speed} km/h\n"
      f"Current Speed: {new_car.current_speed} km/h\n"
      f"Travelled Distance: {new_car.travelled_distance} km")

new_car.accelerate(-200) #brake

print(f"\nFinal speed after emergency brake: {new_car.current_speed} km/h")