import shutil
import unittest
from unittest import TestCase

#import abm_model as abmm
from abm_model.minicell import Minicell
from abm_model.status import Infected


class TestMinicell(TestCase):

    def setUp(self) -> None:
        self.minicell = Minicell()

    def test__init__(self):

        '''
        Test the possibility of specifying the path directory
        '''
        Minicell(path='data/tests')
        shutil.rmtree('data/tests')

        """
        Test the initialisation function in minicell.py
        """
        self.assertRaises(TypeError, self.minicell.__init__, beta='0.01')
        self.assertRaises(TypeError, self.minicell.__init__, recovery_period='1')
        self.assertRaises(TypeError, self.minicell.__init__, population_size=2.1)
        self.assertRaises(TypeError, self.minicell.__init__, population_size='2.1')

        self.minicell = Minicell(population_size=56, beta=0.66,
                                 recovery_period=1)

        self.assertEqual(self.minicell.beta, 0.66)
        self.assertEqual(self.minicell.recovery_period, 1)

        self.minicell = Minicell()
        self.assertEqual(self.minicell.current_time, 0)
        self.assertEqual(len(self.minicell.i_list), 1)
        self.assertEqual(self.minicell.r_list, [])

        self.assertEqual(len(self.minicell.s_list),
                         self.minicell.population_size - 1)

        # Test that there are 0 people in i_list and r_list

        # Test that there are no duplicates in the person id.
        # Use list comprehensions to generate list of person ids from all_list
        # [person.id for person in all_list]
        # check if there are any duplicates in this list

        s_person_ids = [p.name for p in self.minicell.s_list]
        i_person_ids = [p.name for p in self.minicell.i_list]
        r_person_ids = [p.name for p in self.minicell.r_list]
        person_ids = s_person_ids + i_person_ids + r_person_ids
        self.assertEqual(len(person_ids), len(set(person_ids)))

        # Check that all people in all_list are susceptible
        s_person_statuses = [p.status for p in self.minicell.s_list]
        i_person_statuses = [p.status for p in self.minicell.i_list]
        r_person_statuses = [p.status for p in self.minicell.r_list]
        person_statuses = s_person_statuses + i_person_statuses + r_person_statuses
        self.assertEqual(all(str(x) == 'Susceptible' for x in person_statuses), True)

    def test_handle(self):
        """
        Test the 'handle' function in minicell.py
        """
        target_person = self.minicell.s_list[0]
        fake_event = {'person': target_person, 'status': 'Infected'}
        self.minicell.handle(fake_event)
        self.assertEqual(len(self.minicell.i_list), 2)
        self.assertEqual(len(self.minicell.s_list),
                         self.minicell.population_size - 2)

        self.assertEqual(len(self.minicell.r_list), 0)
        # Check that we can move people between lists
        # Create a 'fake' event that infects the first person
        # Pass this event to handler
        # Check that person is in new list and removed from old list
        # Check that lists are otherwise unchanged - no one else moved

        # Check this for a different infection status - infected -> recovered

        target_person = self.minicell.i_list[0]
        fake_event = {'person': target_person, 'status': 'Recovered'}
        self.minicell.handle(fake_event)
        self.assertEqual(len(self.minicell.i_list), 1)
        self.assertEqual(len(self.minicell.s_list), self.minicell.population_size - 2)

        self.assertEqual(len(self.minicell.r_list), 1)

        # If you handle collisions in this method, test them
        # Put a incorrect event in to the function, and check whether it breaks
        # the function as you would expect it to
        # self.assertRaises(TypeError)

    def test_update(self):
        """
        Test the 'update' function in minicell.py
        """

        m = Minicell()
        self.assertEqual(self.minicell.current_time, 0)
        m.update(dt=1)
        m.update(dt=1)
        m.update(dt=1)
        self.assertEqual(m.current_time, 3)


if __name__ == '__main__':

    unittest.main()
