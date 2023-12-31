import unittest
from unittest import TestCase
from generator import Generator


class TestGenerator(TestCase):

    def setUp(self) -> None:
        self.generator = Generator()

    def test__init__(self):
        """
        Test the initialisation function in generator
        """
        # Default case
        self.assertEqual(self.generator.help_string, "")

        # Non default case
        self.generator = Generator("Test text")
        self.assertEqual(self.generator.help_string, "Test text")
        self.assertEqual(self.generator.short_flags, ["h"])
        self.assertEqual(self.generator.short_flags_string, "")
        self.assertEqual(self.generator.long_flags, ["help"])

    def test_get_options(self):
        """
        Test the get_options function in generator
        """

        # This is to reset argv to an empty list, as this is the default user input
        self.generator.argv = []
        # Correct arguments test for no flags
        correct_opts = self.generator.get_options()
        self.assertEqual([], correct_opts)

        # Correct arguments test for just the help flag
        self.generator.argv += ["-h"]
        self.assertEqual(self.generator.get_options(), [("-h", "")])

        # Incorrect arguments test for just the generator class (add other flags)
        self.generator.argv += ["-N", 100]
        self.assertRaises(RuntimeError, self.generator.get_options)

        # Test the short_flags_string
        self.generator.argv = ["-h"]
        self.generator.get_options()
        self.assertEqual(self.generator.short_flags_string, "h")

    def test_update_parameters(self):
        # This method is not implemented in this class
        self.assertRaises(NotImplementedError, self.generator.update_parameters)


if __name__ == '__main__':
    unittest.main()
