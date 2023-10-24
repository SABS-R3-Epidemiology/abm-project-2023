import unittest
from unittest import TestCase
from unittest import mock
from unittest.mock import patch

#import abm_model as abmm
from person import Person
from status import Status, Susceptible, Infected, Recovered

class TestPerson(TestCase):

    def setUp(self) -> None:
        self.person = Person(name='AA', initial_status='Susceptible')

    def test__init__(self):
        """
        Test the initialisation function in person.py
        """
        self.person = Person(name='TAMYA', initial_status='Infected')
        self.assertEqual(self.person.name, 'TAMYA')
        self.assertEqual(self.person.status, 'Infected')
        self.assertEqual(len(self.person.history), 0)

    def test__eq__(self):
        """
        Test the '__eq__' function in person.py
        """
        person1 = Person(name='ABC', initial_status='Susceptible')
        person2 = Person(name='ABD', initial_status='Susceptible')
        self.assertEqual(Person.__eq__(person1, person2), False)

    def test_update(self):
        """
        Test the 'update' function in person.py
        """

    @patch('builtins.print')
    def test_read_infection_history(self):
        """
        Test the 'read_infection_history' function in person.py
        """
        self.person = Person(name='AT', initial_status='Infected')
        Person.read_infection_history()
        self.assert_called_with('AT', "was not infected")

    def test__repr__(self):
        """
        Test the '__repr__' function in person.py
        """
        self.person = Person(name='TAMYA', initial_status='Infected')
        self.assertEqual(f"Person(ID = '{self.person.name}', status = {self.person.status})", f"Person(ID = 'TAMYA', status = Infected)")