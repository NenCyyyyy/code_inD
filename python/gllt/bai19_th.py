import random

lucky_number = random.randrange(1, 99)
lucky_number = 9
print("lucky number to day : ", lucky_number)
print("The maximum number of predictions is 3 times!")
ran_number = int(input("input lucky number for you :"))
dem = 0
while ran_number != lucky_number:
    print("em den lam ")
    ran_number = int(input("input lucky number for you :"))
    dem = dem + 1
    if dem == 2:
        break
if ran_number == lucky_number:
    print("you win!")
