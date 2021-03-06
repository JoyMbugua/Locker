import unittest
import pyperclip
from creds import Credentials

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def tearDown(self):
        '''
        test method that clears the password locker after each test
        '''
        Credentials.locker = {}

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credentials("Twitter", "JM", "Password2021")

    def test_init(self):
        '''
        test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.platform, "Twitter")
        self.assertEqual(self.new_credential.username, "JM")
        self.assertEqual(self.new_credential.password, "Password2021")

    def test_save_password(self):
        '''
        test to check whether the password details are saved 
        '''
        self.new_credential.save_password()
        self.assertEqual(len(Credentials.locker), 1)

    def test_save_multiple_passwords(self):
        '''
        test_save_multiple_contact to check whether we can save multiple contacts in the contact_list
        '''
        self.new_credential.save_password()
        test_password = Credentials("Test","user","bvgtfy65")
        test_password.save_password()
        self.assertEqual(len(Credentials.locker),2)

    def test_delete_password(self):
        '''
        test method that tests whether passwords get deleted from the password locker
        '''
        self.new_credential.save_password()
        test_password = Credentials("Test","user","1234")
        test_password.save_password()

        self.new_credential.delete_password()
        self.assertEqual(len(Credentials.locker),1)
        # print("The length is stll", len(Credentials.locker), Credentials.locker)
    def test_displays_passwords(self):
        '''
        method that returns a list of all passwords in the locker
        '''
        self.assertEqual(Credentials.display_password(), Credentials.locker)

    def test_copy_password(self):
        '''
        test to check whether we can copy passwords
        '''
        self.new_credential.save_password()
        

        self.new_credential.copy_password()

        self.assertEqual(self.new_credential.password, pyperclip.paste())

    
if __name__ == '__main__':
    unittest.main()
