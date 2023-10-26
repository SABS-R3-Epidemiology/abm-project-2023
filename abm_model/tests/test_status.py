import numpy as np
import unittest
from unittest import TestCase

from abm_model.status import Susceptible, Infected


class TestSusceptible(TestCase):

    def setUp(self) -> None:
        self.susceptible = Susceptible()

    def test__repr__(self):
        """
        Test the '__repr__' function of class Susceptible in status.py
        """
        self.assertEqual(f"{self.susceptible}", "Susceptible")


class TestInfected(TestCase):

    def setUp(self) -> None:
        self.infected = Infected()

    def test__init__(self):
        self.assertRaises(TypeError, self.infected.__init__, '1')
        self.assertRaises(ValueError, self.infected.__init__, -1)
        self.infected = Infected(threshold=2)
        self.assertEqual(self.infected.threshold, 2)
        # Need test for self.expiry_date

        np.random.seed(1)
        self.infected = Infected(recovery_period=3, current_time=1)
        np.random.seed(1)
        self.assertEqual(self.infected.expiry_date, 2 + np.random.poisson(2))
        # Check status.py current_time

    def test__repr__(self):
        self.susceptible = Susceptible()
        self.assertEqual(f"{self.susceptible}", "Susceptible")


if __name__ == '__main__':

    unittest.main()
