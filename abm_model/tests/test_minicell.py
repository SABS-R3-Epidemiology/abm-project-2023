import sys
import unittest
from unittest import TestCase

#import abm_model as abmm
import minicell as mc


class TestMinicell(TestCase):

    def setUp(self) -> None:
        self.minicell = mc.Minicell()

    def test__init__(self):
        """
        Test the initialisation function in minicell.py
        """
        self.minicell = mc.Minicell(N=56, P=0.66, D=0)
        self.assertEqual(self.minicell.N, 56)
        self.assertEqual(self.minicell.P, 0.66)
        self.assertEqual(self.minicell.D, 0)

        self.minicell = mc.Minicell()
        self.assertEqual(self.minicell.current_time, 0)
        self.assertEqual(self.minicell.name, 'test')
        self.assertEqual(self.minicell.i_list, [])
        self.assertEqual(self.minicell.r_list, [])
        self.assertEqual(self.minicell.all_list, [])

        self.assertEqual(len(self.minicell.all_list), self.N)
        self.assertEqual(len(self.minicell.s_list), self.N)

        # Test that there are 0 people in i_list and r_list

        # Test that there are no duplicates in the person id.
            # Use list comprehensions to generate a list of person ids from all_list
            # [person.id for person in all_list]
            # check if there are any duplicates in this list

        person_ids = [person.id for person in self.minicell.all_list]
        self.assertEqual(len(person_ids), len(set(person_ids)))

        # Check that all people in all_list are susceptible
        person_statuses = [person.status for person in self.minicell.all_list]
        self.assertEqual(all(x == 'Susceptible' for x in person_statuses), True)

    def test_handle(self):
        """
        Test the 'handle' function in minicell.py
        """
        target_person = self.minicell.s_list[0]
        fake_event = {'person': target_person, 'status': 'Infected'}
        self.minicell.handle(fake_event)
        self.assertEqual(len(self.minicell.i_list), 1)
        self.assertEqual(len(self.minicell.s_list), self.N - 1)
        self.assertEqual(len(self.minicell.all_list), self.N)
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
        self.assertEqual(len(self.minicell.i_list), 0)
        self.assertEqual(len(self.minicell.s_list), self.N - 1)
        self.assertEqual(len(self.minicell.all_list), self.N)
        self.assertEqual(len(self.minicell.r_list), 1)



        # If you handle collisions in this method, test them
        # Put a incorrect event in to the function, and check whether it breaks
        # the function as you would expect it to
        # self.assertRaises(TypeError)


    def test_update(self):
        """
        Test the 'update' function in minicell.py
        """
        self.assertEqual(self.microcell.current_time, 0)
        self.microcell.update(2.0)
        self.assertEqual(self.microcell.current_time, 2.0)

    def test_write_csv(self):
        """
        Test the 'write_csv' function in minicell.py
        """

        # wait until this code is written
        # test that this method writes the right data in the right format

        # Tests should never change the system
        # Instead of creating an actual file, and writing to it, we will use mocks
        # 

if __name__ == '__main__':
    unittest.main()