#1->Rock
#2->Paper
#3->Scissors

import random as rd
choices =["Rock", "Paper", "Scissors"]
flag = 'y'
print("Welcome to Rock, Paper, Scissors!")

while flag == 'y':
    user = input("Enter choice ->1: Rock, 2: Paper, 3: Scissors ->")
    if user not in ['1', '2', '3']:
        print("Invalid choice. Please enter 1, 2 or 3.")
        continue
    user_choice = choices[int(user)-1]
    computer_choice = rd.choice(choices)
    if user_choice == computer_choice:
        print(f"Both players selected {computer_choice}. It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or (user_choice == "Paper" and computer_choice == "Rock") or (user_choice == "Scissors" and computer_choice == "Paper"):
        print("Bot Choice-> ", computer_choice)
        print("You win!")
    else:
        print("Bot Choice-> ", computer_choice)
        print("You lose!")
    flag = input("Do you want to play again? (y/n): ").lower()
        
