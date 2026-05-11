class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        self.current_floor += 1
        print(f"Floor: {self.current_floor}")

    def floor_down(self):
        self.current_floor -= 1
        print(f"Floor: {self.current_floor}")

    def go_to_floor(self, floor):
        print(f"\nGoing to floor {floor}")
        while self.current_floor < floor:
            self.floor_up()
        while self.current_floor > floor:
            self.floor_down()


h = Elevator(1, 10)

print(f"Starting floor: {h.current_floor}")

h.go_to_floor(5)

h.go_to_floor(h.bottom_floor)