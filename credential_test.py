import unittest 
from credential import Credential 
class Testcredential(unittest.TestCase):

    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
       
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("mimy","instagram","mimy@gmail.com","123456") # create credential object
    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run
        """
        Credential.credential_list = []


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.username,"mimy")
        self.assertEqual(self.new_credential.account,"instagram")
        self.assertEqual(self.new_credential.email,"mimy@gmail.com")
        self.assertEqual(self.new_credential.password,"123456")  

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
         the credential list
        '''
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(Credential.credential_list),1)
        # Items up here...

    def test_save_multiple_credential(self):
            '''
            test_save_multiple_credential to check if we can save multiple credential
            objects to our credential_list
            '''
            self.new_credential.save_credential()
            test_credential = credential("mimy","instagram","mimy@gmail.com","123456") # new user
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2)
            # setup and class creation up here
    
# other test cases here
    def test_save_multiple_credential(self):
            '''
            test_save_multiple_credential to check if we can save multiple credential
            objects to our credential_list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("mimy","instagram","mimy@gmail.com","123456") # new credential
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2)
            # More tests above
    def test_delete_credential(self):
            '''
            test_delete_credential to test if we can remove a credential from our credential list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("mimy","instagram","mimy@gmail.com","123456") # new credential
            test_credential.save_credential()

            self.new_credential.delete_credential()# Deleting credential object
            self.assertEqual(len(Credential.credential_list),1)
    def test_find_credential_by_password(self):
        '''
        test to check if we can find a credential by password and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credential("mimy","instagram","mimy@gmail.com","123456") # new credential
        test_credential.save_credential()

        found_credential = Credential.find_by_password("123456")

        self.assertEqual(found_credential.email,test_credential.email) 
    # def test_credential_exists(self):
    #     '''
    #     test to check if we can return a Boolean  if we cannot find the credential.
    #     '''

    #     self.new_credential.credential_credential()
    #     test_credential = Credential("mimy","instagram","mimy@gmail.com.com","123456") # new credential
    #     test_credential.save_credential()

    #     credential_exists = Credential.credential_exist("123456")

    #     self.assertTrue(user_exists)
    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credential.display_credentials(),Credential.credential_list)
     
if __name__ ==  '__main__':
    unittest.main()