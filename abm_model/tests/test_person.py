import unittest
from unittest import TestCase
#from unittest import mock
from unittest.mock import patch

#import abm_model as abmm
from person import Person
from status import *
#from status import Status, Susceptible, Infected, Recovered


class TestPerson(TestCase):

    def setUp(self) -> None:
        self.susceptible = Person(name='L', initial_status=Susceptible())
        self.infected = Person(name='M', initial_status=Infected())
        self.recovered = Person(name='N', initial_status=Recovered())
        
    def test__init__(self):
        """
        Test the initialisation function in person.py
        """
        self.assertEqual(self.susceptible.name, 'L')
        self.assertEqual(self.infected.name, 'M')
        self.assertEqual(self.recovered.name, 'N')
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
        person1 = Person(name='ABC', initial_status='Susceptible')
        person2 = Person(name='ABD', initial_status='Susceptible')
        self.assertEqual(Person.__eq__(person1, person2), False)

    def test_update(self):
        """
        Test the 'update' function in person.py
        """
        self.events = []
        self.infected.expiry_date = 1
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
        self.events = []
        self.infected.expiry_date = 1
        self.current_time = 0
        self.s_list = [Person(name='cavy0', initial_status=Infected()),
                       Person(name='cavy1', initial_status=Infected()),
                       Person(name='cavy2', initial_status=Infected()),
                       Person(name='cavy3', initial_status=Recovered()),
                       Person(name='cavy4', initial_status=Recovered()),
                       Person(name='cavy5', initial_status=Recovered())]
        self.infected.update(self, 1)
        self.infected.expiry_date = 0
        self.current_time = 1
        self.susceptible.update(self, 1)
        self.infected.update(self, 1)
        self.recovered.update(self, 1)
        self.assertEqual(self.events, [{ 'person': self.infected, 'status': Recovered() }])

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
