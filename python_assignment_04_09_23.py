"""This program checks the sex/gender of a user,
Then collects a username and verifies if the username collected is greater
than or equal to 8 characters, and checks if the username contains any symbols
"""


#defining "split" function to convert string to a list of characters 
def split(word):
    return list(word)

#define function "user_sex_collect" to collect and check user's sex
def user_sex_collect():
    user_sex = input("Please enter your Sex (Male/Female):")
    if user_sex == "Male":
        print("Hello Male")
    elif user_sex == "Female":
        print("Hi Female")
    else:
        print("Sex not identified, please enter Male/Female")
        user_sex_collect()


"""defining the function 'username_collect' to collect and check username length,
then check for symbols in the username by converting the username string into
a list. The function is recalled whenever the
user inputs a wrong username, until a correct username is collected."""

def username_collect():
    user_name = input("Please enter your username:")
    if len(user_name) >= 8:
        user_split = split(user_name)
        if "!" in user_split != 0:
            print("Symbol found in username! Please re-enter")
            username_collect()
        elif "@" in user_split != 0:
            print("Symbol found in username! Please re-enter")
            username_collect()
        elif "#" in user_split != 0:
            print("Symbol found in username! Please re-enter")
            username_collect()
        elif "$" in user_split != 0:
            print("Symbol found in username! Please re-enter")
            username_collect()
        elif "%" in user_split != 0:
            print("Symbol found in username! Please re-enter")
            username_collect()
        elif "&" in user_split != 0:
            print("Symbol found in username! Please re-enter")
            username_collect()
        elif ";" in user_split != 0:
            print("Symbol found in username! Please re-enter")
            username_collect()
        elif "?" in user_split != 0:
            print("Symbol found in username! Please re-enter")
            username_collect()
        else:
            print("Welcome to the Code Nation")
    else:
        print("Length of Username entered is too short! Please re-enter")
        username_collect()

#Call user_sex_collect
user_sex_collect()

#Call username_collect
username_collect()









