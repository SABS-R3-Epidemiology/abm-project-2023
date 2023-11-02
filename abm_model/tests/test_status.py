import numpy as np
import unittest
from unittest import TestCase
from abm_model.status import Susceptible, Infected, Recovered
import copy


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
        with self.assertRaises(TypeError):
            Infected('1')
        with self.assertRaises(ValueError):
            Infected(-1)
        self.infected = Infected(threshold=2)
        self.assertEqual(self.infected.threshold, 2)
        # Need test for self.expiry_date

        np.random.seed(1)
        self.infected = Infected(recovery_period=3, current_time=1)
        np.random.seed(1)
        self.assertEqual(self.infected.expiry_date, 2 + np.random.poisson(2))
        # Check status.py current_time

    def test__repr__(self):
        """
        Test the '__repr__' function of class Infected in status.py
        """
        self.assertEqual(f"{self.infected}", "Infected")

    def test__eq__(self):
        '''
        Test the '__eq__' function of class Infected in status.py
        '''
        test1 = Infected(recovery_period=1, current_time=0, threshold=3)
        test2 = Infected(recovery_period=1, current_time=0, threshold=5)
        self.assertEqual(test1 == test2, False)

        test1 = Infected(recovery_period=1, current_time=0, threshold=3)
        test2 = copy.deepcopy(test1)
        test1.expiry_date += 1
        self.assertEqual(test1 == test2, False)


class TestRecovered(TestCase):

    def setUp(self) -> None:
        self.recovered = Recovered()

    def test__repr__(self):
        """
        Test the '__repr__' function of class Recovered in status.py
        """
        self.assertEqual(f"{self.recovered}", "Recovered")


if __name__ == '__main__':

    unittest.main()
