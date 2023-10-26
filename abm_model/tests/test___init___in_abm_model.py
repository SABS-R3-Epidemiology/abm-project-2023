import unittest
import abm_model


class TestInitAbm(unittest.TestCase):

    def test_version_info(self):
        '''
        Test the version info is successfully loaded
        '''
        self.assertIsNotNone(abm_model.VERSION_INT)
        self.assertIsNotNone(abm_model.VERSION)

    def test_minicell(self):
        '''
        Test the minicell is successfully loaded
        '''
        a = abm_model.Minicell()
        self.assertEqual(type(a), abm_model.minicell.Minicell)

    def test_person(self):
        '''
        Test the person is successfully loaded
        '''
        a = abm_model.Person('0', abm_model.Susceptible())
        self.assertEqual(type(a), abm_model.person.Person)
