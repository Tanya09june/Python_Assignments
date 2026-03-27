# Write a program that asks the user to enter a year and tells them whether the year is a leap year.
# A year is a leap year if:
# - It is divisible by 4, and
# - If divisible by 100, it must also be divisible by 400.
# leap year condition, no. should be divisible by 4 or 400 with remainder 0 and not divisible by 100


year=int(input("Enter the Year:- "))
if (year % 4 == 0 or year % 400 == 0) and (year % 100 != 0):
    print(f" {year:} is a Leap Year!")
else:
    print(f" {year:} is not a leap year")
