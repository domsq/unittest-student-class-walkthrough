import unittest
from student import Student


class TestStudent(unittest.TestCase):

    #  Set up test data and creates an entire class, not just an instance.
    #  Runs once before all tests.
    # @classmethod
    # def setUpClass(cls):
    #     print("setUpClass")

    #  Removes class test data. Runs after all tests completed.
    # @classmethod
    # def tearDownClass(cls):
    #     print("tearDownClass")

    #  Sets up test data for each test and creates an instance of a class.
    #  Runs before each test.
    def setUp(self):
        print("setUp")
        self.student = Student("John", "Doe")

    #  Removes class instance test data and runs after each test.
    # def tearDown(self):
    #     print("tearDown")

    def test_full_name(self):
        print("test_full_name")
        self.assertEqual(self.student.full_name, "John Doe")

    def test_alert_santa(self):
        print("test_alert_santa")
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        print("test_email")
        self.assertEqual(self.student.email, "john.doe@email.com")


if __name__ == "__main__":
    unittest.main()
