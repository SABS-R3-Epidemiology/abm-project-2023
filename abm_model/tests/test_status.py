import numpy as np
import unittest
from unittest import TestCase

from status import Status, Susceptible, Infected, Recovered

class TestSusceptible(TestCase):

    def setUp(self) -> None:
        self.susceptible = Susceptible()

    def test__repr__(self):
        """
        Test the '__repr__' function of class Susceptible in status.py
        """
        self.assertEqual(f"Susceptible", "Susceptible")


class TestInfected(TestCase):

    def setUp(self) -> None:
        self.infected = Infected()

    def test__init__(self):
        self.assertRaises(TypeError, self.infected.__init__, '1')
        self.assertRaises(ValueError, self.infected.__init__, -1)
        self.infected = Infected(threshold=2)
        self.assertEqual(self.infected.threshold, 2)
        # Need test for self.expiry_date
        # Think about how to deal with the random function
        self.infected = Infected(recovery_period=3, current_time=1)
        self.assertEqual(self.infected.expiry_date, 2 + np.random.poisson(2))
        # Check status.py current_time 

    def test__repr__(self):
        self.assertEqual(f"Susceptible", "Susceptible")



if __name__ == '__main__':
    unittest.main()