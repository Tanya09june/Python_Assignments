# Design a program that asks the user for their biological gender and hemoglobin level (g/L).
# Based on the provided values, the program should inform the user if their hemoglobin is low, normal, or high. The normal ranges are:
# - For adult females:117-155 g/L.
# - For adult males:134-167 g/L.

Gender =str(input("Enter the gender (Male, Female):- ")).upper()
age= int(input("Enter your age:- "))
if age<18:
    print(f"NOT ELIGIBLE: You're underage.")
else:
    HL= float(input("Enter the Hemoglobin Level (g/l):- "))
    if Gender=="FEMALE" or Gender=="MALE":

        if Gender=="FEMALE":
            if HL<117:
                print(f"Low Hemoglobin Level.")
            elif 117 <= HL <= 155:
                print(f"Normal Hemoglobin Level")
            else:
                print(f"High Hemoglobin Level")

        elif Gender=="MALE":
            if HL<134:
                print(f"Low Hemoglobin Level.")
            elif 134<=HL<=167:
                print(f"Normal Hemoglobin Level")
            else:
                print(f"High Hemoglobin Level")
    else:
        print(f"Invalid Input:- Please type Male or Female for gender")



