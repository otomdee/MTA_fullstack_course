import random
import time
options = ["rock", "paper", "scissors"]

def usr_chooses():
    global user_choice
    user_choice = input("Pick one: rock, paper, scissors: ")
    user_choice = user_choice.lower()
    if user_choice != "rock":
        if user_choice != "paper":
            if user_choice != "scissors":
                print("wrong entry, please enter a valid option.")
                usr_chooses()

usr_chooses()
comp_choice = random.choice(options)
time.sleep(1)
print("computer chose", comp_choice)
time.sleep(1)

if user_choice == "rock":
    if comp_choice == "rock":
        print("It's a tie")
    elif comp_choice == "paper":
        print("Paper beats rock, You lost :(")
    else:
        print("Rock beats scissors, you win!")
elif user_choice == "paper":
    if comp_choice == "rock":
        print("Paper beats rock, You win!")
    elif comp_choice == "paper":
        print("It's a tie")
    else:
        print("Scissors beats Paper, You lost :(")
else:
    if comp_choice == "rock":
        print("Rock beats Scissors, You lost :(")
    elif comp_choice == "paper":
        print("Scissors beats paper, You win!")
    else:
        print("It's a tie")
