import unittest # Importing the unittest module
from user import User # Importing the user class

class Testuser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
        # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("mimy","mimy@gmail.com","123456") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"mimy")
        self.assertEqual(self.new_user.email,"mimy@gmail.com")
        self.assertEqual(self.new_user.password,"123456")  

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)
        # Items up here...

    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user list
            '''
            self.new_user.save_user()
            test_user = user("mimy","mimy@gmail.com","123456") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)
            # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

# other test cases here
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("mimy","mimy@gmail.com","123456") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)
            # More tests above
    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("mimy","mimy@gmail.com","123456") # new user
            test_user.save_user()

            self.new_user.delete_user()# Deleting user object
            self.assertEqual(len(User.user_list),1)
    def test_find_user_by_password(self):
        '''
        test to check if we can find a user by password and display information
        '''

        self.new_user.save_user()
        test_user = User("mimy","mimy@gmail.com","123456") # new user
        test_user.save_user()

        found_user = User.find_by_password("123456")

        self.assertEqual(found_user.email,test_user.email) 
    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("mimi","mimy@gmail.com","123456") # new user
        test_user.save_user()

        user_exists = User.user_exist("123456")

        self.assertTrue(user_exists)
    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(),User.user_list)
     
if __name__ ==  '__main__':
    unittest.main()
    