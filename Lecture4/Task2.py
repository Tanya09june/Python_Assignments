num = []
while True:
    val = input("Enter the user input:- ")
    if val == " ":
        print("EXIT")
        break
    num.append(int(val))
num.sort(reverse=True)
first_five = num[:5]
print("The number are descending order :- ")
print(first_five)

