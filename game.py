print("\033c",end="")
heading=("ROCK PAPER SCISSORS GAME")
print(heading.center(400))
import random
print("Winning rules of the game Rock Paper Scissor are as follows:\n \tRock vs Paper - Paper wins.\n \tRock vs Scissor - Rocks wins.\n \tPaper vs Scissor - Scissors wins.")
while True:
    print("Game starts now:-")
    print("Enter your choice \n \t1 - Rock\n \t2 - Paper\n \t3 - Scissors \n")
    user_choice=int(input("Enter your option:"))
    while user_choice >3 or user_choice<1:
        user_choice=int(input("Enter data is invalid. Please enter valid data : "))
    if user_choice==1:
        choice="Rock"
    elif user_choice==2:
        choice="Paper"
    else:
        choice="Scissors"
    print(f"\nYour choice is:{choice}")
    
    comp_choice=random.randint(1,3)
    if comp_choice==1:
        choiceofcomp="Rock"
    elif comp_choice==2:
        choiceofcomp="Paper"
    else:
        choiceofcomp="Scissors"
    print(f"\nComputer choice is:{choiceofcomp}")
    result=""
    if user_choice==comp_choice:
        result="Draw"
    elif(user_choice==1 and comp_choice==3) or (user_choice==2 and comp_choice==1) or (user_choice==3 and comp_choice==2):
        result="user"
    
    if result=="Draw":
        print("\nThe game is tie.")
    elif result=="user":
        print("\nYou are the winner.")
    else:
        print("\nComputer is the winner.")
    
    print("\nDo you want to play again? (y/n)")
    ans=input()
    print("\033c",end="")
    if ans=="n":
        break
print("Thankyou for playing!")