from unittest import TestCase
from generator import Generator
import getopt
from unittest.mock import patch

class TestGenerator(TestCase):

    def setUp(self) -> None:
        self.generator = Generator(help_string='help string')

    def test__init__(self):
        self.generator = Generator(help_string='help')
        self.assertEqual(self.generator.help_string, 'help')

    @patch('builtins.print')
    def test_get_options(self, mock_print):
        try:
            self.assertEqual(self.generator.short_flags[0], 'h')
        except getopt.GetoptError:
            Generator.get_options()
            mock_print.assert_called_with("Error: incorrect arguments provided. Use '--help' option for help.")
            with self.assertRaises(SystemExit):
                Generator.get_options()

    def test_update_parameters(self):
        self.assertRaises(NotImplementedError, self.generator.update_parameters)