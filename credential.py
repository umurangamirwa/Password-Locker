class Credential:
    """
    Class that generates new instances of credentials.
    """

    credential_list = [] # Empty credential list

    def __init__(self,username,email,password):

      # docstring removed for simplicity

        self.username = username
        self.email = email
        self.password = password
        credential_list = [] # Empty credential list
 # Init method up here
    def save_credential(self):

        '''
        save_credential method saves credential objects into credential_list
        '''

        Credential.credential_list.append(self)
    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self)
    @classmethod
    def find_by_password(cls,password):
        '''
        Method that takes in a password and returns a credential that matches that password.

        Args:
            password: password to search for
        Returns :
            password of person that matches the password.
        '''

        for user in cls.credetial_list:
            if credential.password == password:
                return credential
    @classmethod
    def credential_exist(cls,password):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            password: password to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.password == password:
                return True

        return False
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list
        
