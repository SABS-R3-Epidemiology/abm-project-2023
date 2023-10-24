import unittest
from unittest import TestCase

#import abm_model as abmm
import person 


class TestPerson(TestCase):

    def setUp(self) -> None:
        self.person = person.Person()

    def test__init__(self):
        """
        Test the initialisation function in person.py
        """
        self.person.__init__(id='TAMYA', initial_status='Infected')
        self.assertEqual(self.person.id, 'TAMYA')
        self.assertEqual(self.person.status, 'Infected')
        self.assertEqual(len(self.person.history), 0)

    def test__eq__(self):
        self.person.__eq__()
        self.assertEqual(self.person.id, self.other.id)

    def test_update(self):
        """
        
        """

    def test_read_infection_history(self):
        """
        
        """