import unittest
from datetime import timedelta
from unittest.mock import patch
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

    def test_apply_extension(self):
        old_ed = self.student.end_date
        self.student.apply_extension(5)

        self.assertEqual(self.student.end_date, old_ed + timedelta(days=5))

    def test_course_schedule_success(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")

    def test_course_schedule_failed(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong" +
                             " with the request!")

    def test_start_date(self):
        self.assertEqual(self.student.start_date, str(
                         self.student._start_date))


if __name__ == "__main__":
    unittest.main()
