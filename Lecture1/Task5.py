Talents=float(input("Enter the value of Talent:- "))
Pounds=float(input("Enter the value of pound:- "))
Lots=float(input("Enter the value of lot:- "))
total_lots=(Talents*20*32)+(Pounds*20)+Lots
total_grams = total_lots*13.5
kilograms = int(total_grams//1000)
grams= total_grams%1000
print("The weight in modern units:- ")
print(f"{kilograms} kilograms and {grams:.2f} grams")