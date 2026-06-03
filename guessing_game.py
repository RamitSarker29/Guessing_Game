import random
while True:
    try:
        num = int(input("Enter your limit: "))
        break
    except ValueError:
        print("Enter number only!")
random_num = random.randint(1,num)
count=0
while True:
    choice = int(input("Enter your number: "))
    count+=1

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
        print(f"You've guessed the number in {count} tries...")
        break
