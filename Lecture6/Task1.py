import random
def roll_dice():
    return random.randint(1,6)
result=0   #variable assign value is 0
while result !=6:
    result = roll_dice()
    print(result)

