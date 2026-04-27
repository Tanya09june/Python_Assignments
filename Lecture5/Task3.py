airports = {}

while True:
    choice = input("1=Enter a new airport, 2=Fetch airport, 3=Quit:- ")

    if choice == "1":
        code = input("Enter ICAO code:- ")
        name = input("Enter airport name:- ")
        airports[code] = name
        print("Saved")

    elif choice == "2":
        code = input("Enter ICAO code: ")
        print(airports.get(code, "Not Found"))

    elif choice == "3":
        print("GoodBye")
        break