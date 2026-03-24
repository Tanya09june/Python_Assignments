#sum=x+y+z
#product= x*y*z
#average= (x+y+z)/3
X=int(input("Enter the value of X = ")) #int(input "---) used to take input in integer form.
Y=int(input("Enter the value of Y = "))
Z=int(input("Enter the value of Z = "))
Total_Sum = (X+Y+Z)
Product = (X * Y * Z)
Average = (Total_Sum//3)
print(f"The sum of integers= {Total_Sum}")
print(f"The product of 3 integers= {Product}")
print(f"The average of 3 integers= {Average}")


#"/" single division always return in float whereas "//" double sign division always return round number of nearest whole number.