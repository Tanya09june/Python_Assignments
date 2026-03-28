import random
Winner_Number = random.randint(1, 10)
Guess = 0
print("Welcome!")
print("Guess the Winner Number between 1 and 10.")
while Guess != Winner_Number:
    Guess = int(input(f"Enter your number: "))
    if Guess < Winner_Number:
        print("It's low, better luck next time!")
    elif Guess > Winner_Number:
            print("Its high, better luck next time!")
print("Congratulations! You won...  you guess the right winner number.")