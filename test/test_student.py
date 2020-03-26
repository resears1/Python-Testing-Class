import unittest
from class_definitions import student as t

class TestCase1(unittest.TestCase):
    def setUp(self):
        self.student = t.Student('Sears', 'Ricky', 'CIS', 3.48)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Sears')
        self.assertEqual(self.student.first_name, 'Ricky')
        self.assertEqual(self.student.major, 'CIS')

    def test_object_created_all_attributes(self):
        student = t.Student("Sears", "Ricky", "CIS", 3.48)
        assert student.last_name == "Sears"
        assert student.first_name == "Ricky"
        assert student.major == "CIS"
        assert student.gpa == 3.48

    def test_person_str(self):
        self.assertEqual(str(self.student), 'Sears, Ricky has major CIS with gpa: 3.48')

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            s = t.Student('5', 'Ricky', 'CIS')

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            s = t.Student('Sears', '809', 'CIS')

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            s = t.Student('Sears', 'Ricky', '515')

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            s = t.Student('Sears', 'Ricky', 'CIS', 'threepointfourfive')
