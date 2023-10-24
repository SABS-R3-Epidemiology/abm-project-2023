import unittest
from unittest import TestCase
from unittest.mock import patch

#import abm_model as abmm
import person 


class TestPerson(TestCase):

    def setUp(self) -> None:
        self.person = person.Person(id='AA', initial_status='Susceptible')

    def test__init__(self):
        """
        Test the initialisation function in person.py
        """
        self.person = person.Person(id='TAMYA', initial_status='Infected')
        self.assertEqual(self.person.id, 'TAMYA')
        self.assertEqual(self.person.status, 'Infected')
        self.assertEqual(len(self.person.history), 0)

    def test__eq__(self):
        """
        Test the '__eq__' function in person.py
        """
        person1 = person.Person(id='ABC', initial_status='Susceptible')
        person2 = person.Person(id='ABD', initial_status='Susceptible')
        self.assertEqual(self.__eq__(person1, person2), False)

    def test_update(self):
        """
        Test the 'update' function in person.py
        """

    @patch('builtins.print')
    def test_read_infection_history(self):
        """
        Test the 'read_infection_history' function in person.py
        """
        self.person = person.Person(id='AT', initial_status='Infected')
        self.assert_called_with('AT' + " was not infected")

    def test__repr__(self):
        """
        Test the '__repr__' function in person.py
        """
        self.person = person.Person(id='TAMYA', initial_status='Infected')
        self.assertEqual(f"Person(ID = '{self.id}', status = {self.status})", "Person(ID = 'TAMYA', status = 'Infected')")