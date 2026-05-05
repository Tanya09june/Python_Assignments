def gallons_into_ltr(gallons):   #parameter-gallon
    return gallons*3.78

gallons=float(input(f"Enter the value of gallon (-ve value ti exist):- "))
while gallons >=0:
    litre= gallons_into_ltr(gallons)     #call function with user entered value in new variable litre
    print("After conversion litre", litre)
    gallons = float(input(f"Enter the value of gallon (-ve value ti exist):- "))