#!/usr/bin/env python3.6
import pyperclip
from user import User
from credential import Credential
def create_user(username,account,email,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,account,email,password)
    return new_user
def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()
def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()
def find_user(password):
    '''
    Function that finds a user by password and returns the user
    '''
    return User.find_by_password(password)
def check_existing_users(password):
    '''
    Function that check if a user exists with that password and return a Boolean
    '''
    return User.user_exist(password)
def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()
def main():
    print("Hello Welcome to your user list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new user, dc - display users, fc -find a user, ex -exit the user list ")

        short_code = input().lower()

        if short_code == 'cc':
            print("New User")
            print("-"*10)

            print ("username ....")
            username = input()
                            
            print ("account ...")
            account = input()

            print("email ...")
            email = input()

            print("password ...")
            password = input()

                            


            save_users(create_user(username,account,email,password)) # create and save new user.
            print ('\n')
            print("New User {username} {email} created")
            print ('\n')

        elif short_code == 'dc':

            if display_users():
                print("Here is a list of all your users")
                print('\n')

                for user in display_users():
                        print("{user.username} {user.email} .....{user.password}")

                        print('\n')
            else:
                    print('\n')
                    print("You dont seem to have any users saved yet")
                    print('\n')

        elif short_code == 'fc':

                print("Enter the password you want to search for")

                search_password = input()
                if check_existing_users(search_password):
                        search_user = find_user(search_password)
                        print(f"{search_password.username} {search_user.email}")
                        print('-' * 20)

                        print(f"password.......{search_user.password}")
                        print(f"email.......{search_user.email}")
                else:
                        print("That user does not exist")

        elif short_code == "ex":
                        print("Bye .......")
                        break
        else:
                        print("I really didn't get that. Please use the short codes")


    