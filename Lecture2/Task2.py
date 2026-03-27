# #asks the user to input the cabin class on a cruise ship and prints the corresponding description based on the following list:
# LUX: Upper-deck cabin with a balcony.
# A: Cabin above the car deck with a window.
# B: Windowless cabin above the car deck.
# C: Windowless cabin below the car deck.

Cabin_Class =(input(f"Enter the Cabin Class (LUX, A, B, C):- ")).upper()
if Cabin_Class == "LUX":
    print(f"LUX:-You have Upper-Deck cabin with a balcony. Enjoy!")
elif Cabin_Class == "A":
    print(f"A:-Your cabin is above the car deck with a window.")
elif Cabin_Class == "B":
    print(f"B:- Windowless cabin above the car deck.")
elif Cabin_Class == "C":
    print(f"C:- Windowless cabin below the car deck.")
else:
    print(f"Invalid cabin class")
