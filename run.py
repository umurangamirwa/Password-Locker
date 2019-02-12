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