import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):
    """
    this function gets called while the initiation every test - everytime - its redundant
    """
    def setUp(self):
        print('setUp is called')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    """
    this function gets called at the end of every test  - everytime - its redundant
    """
    def tearDown(self):
        print('tearDown\n')

    """
    setUpClass and tearDownClass 
    by defining the setUpClass and tearDownClass methods (they should be class methods)
    setUpClass will get called once before running the tests and 
    tearDownClass at end of all tests - e.g. database instances

    """

    @classmethod
    def setUpClass(cls):
        print('main setUp is called')

    @classmethod
    def tearDownClass(cls):
        print('main teardownClass is called')


    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')


    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')






if __name__ == '__main__':
    unittest.main()
