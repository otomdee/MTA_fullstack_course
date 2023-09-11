import random
import time

correct_num = random.randint(1,10)
num_of_tries = 0

def guesser():
    global num_of_tries
    user_num_str = input("Choose a number between 1 and 10:")
    user_num = int(user_num_str)
    if user_num == correct_num:
        print("Congrats, you won!")
        time.sleep(1)
        usr_choice = input("do you want to play again? (yes/no):")
        if usr_choice == "yes":
            num_tries = 0
            guesser()
        else:
            print("Thanks for playing, bye")
    else:
        print("Wrong number, try again.")
        num_of_tries = num_of_tries + 1
        time.sleep(1)
        if num_of_tries < 5:
            print("you have", 5 - num_of_tries , "tries left")
            guesser()
        else:
            print("Game over :( ")


print("==================NUMBER GUESSING GAME==================")

guesser()
