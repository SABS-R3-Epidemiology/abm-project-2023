import unittest
from unittest import TestCase

from status import Status, Susceptible, Infected, Recovered

class TestSusceptible(TestCase):

    def setUp(self) -> None:
        self.susceptible = Susceptible()

    def test__repr__(self):
        """
        
        """
        self.susceptible = Susceptible()
        self.assertEqual(f"Susceptible", "Susceptible")


class TestInfected(TestCase):

    def setUp(self) -> None:
        self.infected = Infected()

    def test__init__(self):
        self.assertRaises(TypeError, self.infected.__init__, '1')
        self.assertRaises(ValueError, self.infected.__init__, -1)
        self.infected = Infected(threshold=2)
        self.assertEqual(self.infected.threshold, 2)


if __name__ == '__main__':
    unittest.main()