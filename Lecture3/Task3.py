user_input = input("Enter a number ( space to stop): ")

if user_input != "":
    number = float(user_input)
    smallest = number
    largest = number

    while user_input != "":
        user_input = input("Enter a number (space to stop): ")

        if user_input != "":
            number = float(user_input)

            if number < smallest:
                    smallest = number
            if number > largest:
                    largest = number

        print(f"The smallest number is: {smallest}")
        print(f"The largest number is: {largest}")

    else:
        print("Invalid Input.")