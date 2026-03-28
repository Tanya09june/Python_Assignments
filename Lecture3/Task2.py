

inches = 0
while inches >= 0:
    inches = float(input("Enter the measurement in inches (negative to quit): "))
    if inches < 0:
        print("Negative value. Existing")
        break
    centimeters = inches * 2.54
    print(f"{inches} inches is {centimeters:.2f} cm.\n")


# # Alternate
# Inches=float(input(f"Enter the measurement in inches (-ve for exit):- "))
# while Inches>=0:
#     CM=Inches*2.54
#     print(f"{Inches} inches is equal to {CM:.2f} cm.")
#     Inches = float(input(f"Enter the measurement in inches (-ve for exit):- "))
# print("Invalid Input... Successfully Exit.")