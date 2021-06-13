import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):
    #
    # @classmethod
    # def setUpClass(cls) -> None:
    #     print('run in the beginning')

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print('run in the end')
    #
    def setUp(self) -> None:
        self.emp_1 = Employee('taras', 'salashniy', 10000)
        print('initializing prerequisites for test')
    #
    # def tearDown(self) -> None:
    #     print('Test results have been destroyed')

    def test_email(self):

        self.assertEqual(self.emp_1.email, 'taras.salashniy@gmail.com')

        self.emp_1.last = 'salashnyi'
        self.assertEqual(self.emp_1.email, 'taras.salashnyi@gmail.com')

        self.emp_1.first = 'tara'
        self.assertEqual(self.emp_1.email, 'tara.salashnyi@gmail.com')

        self.emp_1.last = 'test.learner'
        self.emp_1.first = 'unit'
        self.assertEqual(self.emp_1.email, 'unit.test.learner@gmail.com')

    def test_fullname(self):

        self.assertEqual(self.emp_1.full_name, 'taras salashniy')

        self.emp_1.last = 'Pirohov'
        self.assertEqual(self.emp_1.full_name, 'taras Pirohov')

        self.emp_1.first = 'tara'
        self.assertEqual(self.emp_1.full_name, 'tara Pirohov')

        self.emp_1.last = 'test.learner'
        self.emp_1.first = 'unit'
        self.assertEqual(self.emp_1.full_name, 'unit test.learner')

    def test_apply_raise(self):

        self.assertEqual(self.emp_1.apply_raise(), 10500)

        Employee.raise_amt = 2
        self.assertEqual(self.emp_1.apply_raise(), 20000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('March')
            mocked_get.assert_called_with('http://company.com/salashniy/March')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_1.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/salashniy/June')
            self.assertEqual(schedule, 'Bad requests')


if '__name__' == '__main__':
    unittest.main()
