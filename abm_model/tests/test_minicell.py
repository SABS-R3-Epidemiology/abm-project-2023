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
        self.assertEqual(self.minicell.P, self.P)
        self.assertEqual(self.minicell.D, self.D)
        self.assertEqual(self.minicell.current_time, 0)
        self.assertEqual(self.minicell.name, 'test')

    def test_handle(self):
        """
        Test the 'handle' function in minicell.py
        """


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

if __name__ == '__main__':
    unittest.main()