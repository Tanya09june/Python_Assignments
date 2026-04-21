import random
num=int(input("Enter the number for dice roll:- "))
sum=0
for i in range(num):
    roll=random.randint(1, 6)
    sum+=roll
    print(f"The number of roll dice {roll} and sum is {sum}")



















