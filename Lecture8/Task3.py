class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
        print(f"Elevator is at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
        print(f"Elevator is at floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        if target_floor > self.top or target_floor < self.bottom:
            print("Invalid floor!")
            return

        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for i in range(num_elevators):
            new_elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(new_elevator)

    def run_elevator(self, elevator_number, destination_floor):
        print(f"\n Moving Elevator {elevator_number} ")
        target_elevator = self.elevators[elevator_number - 1]
        target_elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        print("\n!!! FIRE ALARM DETECTED !!!")
        print("Returning all elevators to the bottom floor...")
        for i, elevator in enumerate(self.elevators):
            print(f"Evacuating Elevator {i + 1}:")
            elevator.go_to_floor(self.bottom_floor)
        print("All elevators are safely at the bottom floor.")



city_tower = Building(1, 15, 3)

city_tower.run_elevator(1, 12)
city_tower.run_elevator(2, 5)
city_tower.run_elevator(3, 15)

city_tower.fire_alarm()