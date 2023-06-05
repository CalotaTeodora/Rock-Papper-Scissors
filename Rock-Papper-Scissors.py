import random

winning = 3 # variable that stores the score 

while (winning > 0 and winning <= 10):
    user_choice = input("What do you choice? (rock, papper, scissors) ")
    user_choice = user_choice.lower()
    
    random_choice = random.choice(['rock', 'papper', 'scissors'])

    if user_choice == 'quit':
        break

    if user_choice != 'rock' or user_choice != 'papper' or user_choice != 'scissors':
        print("Please choose a correct answer")
        continue

    if user_choice == random_choice:
        print("It's equallity")
        winning -= 1
        
    elif user_choice == 'rock' and random_choice == 'scissors':
        print("You win!")
        winning += 1
        
    elif user_choice == 'scissors'  and random_choice == 'papper':
        print("You win!")
        winning += 1
        
    elif user_choice == 'papper' and random_choice == 'rock':
        print("You win!")
        winning += 1
        
    else:
        print("You lose!")
        winning -= 2
    
    print(winning)
