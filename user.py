class User:
    """
    class that generates new instances of user
    """
    
    user_list=[]

    def __init__(self,username,account_name,email,password):
    
        '''
        __init__ method that helps us define properties for our objects.
        Args:
            username: New user username.
            account : New user account_name.
            email: New user create email.
            password : New user password .
        '''
        self.username = username
        self.account = account_name
        self.email = email
        self.password= password
    
    user_list=[]
    def login_user(self):
        '''
        login_user method saves contact object into user_list
        '''
        User.user_list.append(self)