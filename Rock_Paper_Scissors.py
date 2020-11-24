from random import randint
playing=True
choice=''
while(playing):
    print('\n\n')
    print("Python Rock Paper Scissors Game")
    print("Remember the rules:\n1.Rock beats scissors \n2.Scissors beats paper \n3.Paper beats rock")
    choice2 = randint(1, 3)
    choice1 = int(input("Enter your choice as 1 for Rock, 2 for Scissors and 3 for Paper:"))
    if(choice2==1):
        print("Computer choice- Rock")
    elif(choice2==2):
        print("Computer choice- Scissors")
    else:
        print("Computer choice- Paper")
        
    if(choice1==1):
        print("Your choice- Rock")
    elif(choice1==2):
        print("Your choice- Scissors")
    else:
        print("Your choice- Paper")
        
    if (choice1 == choice2):
        print("Opps! Same choice. It's a tie")
    # choice2 is computer choice
    # choice1 is the user choice
    elif (choice1 == 1) and (choice2 == 2) or (choice1 == 2) and (choice2 == 3) or (choice1 == 3) and (choice2 == 1): 
            print("User wins")
    elif (choice1 == 2) and (choice2 == 1) or (choice1 == 3) and (choice2 == 2) or (choice1 == 1) and (choice2 == 3):
            print("Computer wins")
            
    choice = input('Press n/N to exit the game, Press any key to continue :')
    if choice == 'N' or choice == 'n':
        playing=False
        break        
    else:
        playing=True
        continue
 
    print('----------------------------------------------------------')
    print('----------------------------------------------------------')
