import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        set up method to run before each test
        '''
        self.new_user=User("mimy","instagram","mimy@gmail","123456")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"mimy")
        self.assertEqual(self.new_user.account_name,"instagram")
        self.assertEqual(self.new_user.email,"mimy@gmail.com")
        self.assertEqual(self.new_user.password,"123456")

    def test_login_user(self):
        '''
        test_login_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.login_user() 
        self.assertEqual(len(User.user_list),1)
    
    

if __name__ == '__main__':
    unittest.main()
    