import unittest
from src.person import Person

class PersonTest(unittest.TestCase):

    def test_person_constructor(self):
        """
        Test if person constructor works
        """
        person = Person("Wionna", "Ryder", "212-000-0000", "blue", "10000")

        self.assertEqual(person.first_name, "Wionna")
        self.assertEqual(person.last_name, "Ryder")
        self.assertEqual(person.phone_number, "212-000-0000")
        self.assertEqual(person.color, "blue")
        self.assertEqual(person.zipcode, "10000")

    def test_convert_phone_number(self):
        """
        Test convert phone number correctly formats phone number
        """
        person = Person("Wionna", "Ryder", "212 000 0000", "blue", "10000")
        self.assertEqual(person.phone_number, "212-000-0000")

        person = Person("Wionna", "Ryder", "(212)-000-0000", "blue", "10000")
        self.assertEqual(person.phone_number, "212-000-0000")

        person = Person("Wionna", "Ryder", "2120000000", "blue", "10000")
        self.assertEqual(person.phone_number, "212-000-0000")
