import random

print("Rules of the Game: ")
print("1) Your score starts from 3")
print("2) If you make equallity you will lose 1 point")
print("3) If you lose your points will decrease with 2")
print("4) If you win you will collect 3 points")
print("5) The game will end if you remain with 0 points or less or if you collect 10 points")
print("Good lack!!!")
print()

winning = 3

while (winning > 0 and winning <= 10):
    user_choice = input("What do you choice? (rock, papper, scissors) ")
    user_choice = user_choice.lower()
    random_choice = random.choice(['rock', 'papper', 'scissors'])
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


# python3 Rock-Papper-Scissors.py