import random

user_choice=int(input("Enter 0 for rock, 1 for paper and 2 for scissors : "))
computer_choice=random.randint(0,2)
print(computer_choice)
if(user_choice==0):
    if(computer_choice==1) :
        print("You Lose")
    elif(computer_choice==user_choice) :
        print("Tie")
    else :
        print("Hurray ,You Won!!")
elif(user_choice==1):
    if(computer_choice==2) :
        print("You Lose")
    elif(computer_choice==user_choice) :
        print("Tie")
    else :
        print("Hurray ,You Won!!")
elif(user_choice==2):
    if(computer_choice==0) :
        print("You Lose")
    elif(computer_choice==user_choice) :
        print("Tie")
    else :
        print("Hurray ,You Won!!")
else :
    print("Wrong Choice")
