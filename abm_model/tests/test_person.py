import unittest
from unittest import TestCase
#from unittest import mock
from unittest.mock import patch

#import abm_model as abmm
from person import Person
from status import Susceptible, Infected, Recovered
#from status import Status, Susceptible, Infected, Recovered


class TestPerson(TestCase):

    def setUp(self) -> None:
        self.susceptible = Person(name='S', initial_status=Susceptible())
        self.infected = Person(name='I', initial_status=Infected(threshold=3))
        self.recovered = Person(name='R', initial_status=Recovered())

    def test__init__(self):
        """
        Test the initialisation function in person.py
        """
        self.assertEqual(self.susceptible.name, 'S')
        self.assertEqual(self.infected.name, 'I')
        self.assertEqual(self.recovered.name, 'R')
        self.assertEqual(self.susceptible.status, Susceptible())
        self.assertEqual(self.infected.status, Infected())
        self.assertEqual(self.recovered.status, Recovered())
        self.assertEqual(len(self.susceptible.history), 0)
        self.assertEqual(len(self.infected.history), 0)
        self.assertEqual(len(self.recovered.history), 0)

    def test__eq__(self):
        """
        Test the '__eq__' function in person.py
        """
        self.assertFalse(self.susceptible == self.infected)
        self.assertFalse(self.susceptible == self.recovered)
        self.assertFalse(self.infected == self.recovered)
        cavy_S, cavy_I, cavy_R = (Person(name='cavy', initial_staus=Susceptible()),
                                  Person(name='cavy', initial_staus=Infected()),
                                  Person(name='cavy', initial_staus=Recovered()))
        self.assertFalse(self.susceptible == cavy_S)
        self.assertFalse(self.susceptible == cavy_I)
        self.assertFalse(self.recovered == cavy_R)
        self.assertEqual(self.susceptible, Person(name='S', initial_staus=self.susceptible.status))
        self.assertEqual(self.infected, Person(name='I', initial_staus=self.infected.status))
        self.assertEqual(self.recovered, Person(name='R', initial_staus=self.recovered.status))
        self.assertRaises(Error('Two people shall not have the same name!'), cavy_S == cavy_I)
        self.assertRaises(Error('Two people shall not have the same name!'), cavy_S == cavy_R)
        self.assertRaises(Error('Two people shall not have the same name!'), cavy_I == cavy_R)

    def test_update(self):
        """
        Test the 'update' function in person.py
        """
        self.events = []
        self.infected.status.expiry_date = 1
        self.current_time = 0
        self.s_list = [Person(name='cavy0', initial_status=Susceptible()),
                       Person(name='cavy1', initial_status=Susceptible()),
                       Person(name='cavy2', initial_status=Susceptible()),
                       Person(name='cavy3', initial_status=Susceptible()),
                       Person(name='cavy5', initial_status=Susceptible()),
                       Person(name='cavy4', initial_status=Susceptible())]
        self.beta = 1
        self.infected.update(self, 0)
        self.beta = 0
        self.infected.update(self, 1)
        self.assertEqual(self.events, [])
        self.beta = 2
        self.infected.update(self, 2)
        for event in self.events:
            assert event['person'] in self.s_list
            self.assertEqual(str(event['status']), 'Infected')
        self.s_list = []
        self.events = []
        self.infected.status.expiry_date = 1
        self.current_time = 0
        self.susceptible.update(self, 1)
        self.infected.update(self, 1)
        self.recovered.update(self, 1)
        self.assertEqual(self.events, [])
        self.infected.status.expiry_date = 1
        self.current_time = 1
        self.infected.update(self, 1)
        self.assertEqual(self.events, [{'person': self.infected, 'status': Recovered(), 'bla': self.infected.status.expiry_date}])
        self.events = []

    @patch('builtins.print')
    def test_read_infection_history(self, mock_print):
        """
        Test the 'read_infection_history' function in person.py
        """
        self.person = Person(name='AT', initial_status='Infected')
        self.person.read_infection_history()

        mock_print.assert_called_with('AT was not infected')

    def test__repr__(self):
        """
        Test the '__repr__' function in person.py
        """
        self.person = Person(name='TAMYA', initial_status='Infected')
        test_string = f"Person(ID = '{self.person.name}'"
        test_string += f", status = {self.person.status})"
        self.assertEqual(test_string,
                         "Person(ID = 'TAMYA', status = Infected)")


if __name__ == '__main__':
    unittest.main()
