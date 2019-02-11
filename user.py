class user:
    """
    Class that generates new instances of users.
    """

    user_list = [] # Empty contact list

    def __init__(self,username,email,password):

      # docstring removed for simplicity

        self.username = username
        self.email = email
        self.password = password
        
