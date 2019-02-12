#!/usr/bin/env python3.6
import pyperclip
from user import User
from credential import Credential
def create_user(username,email,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,email,password)
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

    