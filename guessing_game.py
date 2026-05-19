import random
num = int(input("Enter your limit: "))
random_num = random.randint(1,num)
while True:
    choice = int(input("Enter your number: "))
    if  choice<1 or choice>num:
        print("Invalid Input....\n Try Again..")
        continue
    elif choice>random_num:
        print("Lower....\n Try Again..")
        continue
    elif choice<random_num:
        print("Higher....\n Try Again..")
        continue
    elif choice==random_num:
        print("Congratulations!!!!\n You've Won")
        break
