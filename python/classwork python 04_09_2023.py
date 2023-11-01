"""This program checks the sex/gender of a user, then collects a username and
verifies if the username collected is greater than or equal to 8 characters"""

user_sex = input("Please enter your Sex (Male/Female):")
if user_sex == "Male":
    print("Hello Male")
elif user_sex == "Female":
    print("Hi Female")
else:
    print("Sex not identified!")

user_name = input("Please enter your username:")

if len(user_name) >= 8:
    if "!" in user_name > 0:
        
    print("Welcome to the Code Nation")
else:
    print("Username entered is incorrect!")
