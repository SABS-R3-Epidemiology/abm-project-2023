import unittest
from unittest import TestCase
from abm_model.generate_plots import PlotGenerator


class TestGeneratePlots(TestCase):

    def setUp(self) -> None:
        self.generator = PlotGenerator()

    def test__init__(self):
        """
        Test the initialisation function in generator
        """
        # Default case
        self.assertEqual(self.generator.help_string, "")

        # Non default case
        self.generator = PlotGenerator("Test text")
        self.assertEqual(self.generator.csv_file_name, "default.csv")
        self.assertEqual(self.generator.help_string, "Test text")
        # args = sys.argv[1:]
        # if "--unit" in args:
        #     args.remove("--unit")
        # self.assertEqual(self.generator.argv, args)
        self.assertEqual(self.generator.short_flags, ["h", "f"])
        self.assertEqual(self.generator.long_flags, ["help", "csv-file-name"])

    def test_get_options(self):
        """
        Test the get_options function in generator
        """

        # This is to reset argv to an empty list, as this is the default user input
        self.generator.argv = []
        # Default test for no flags
        correct_opts = self.generator.get_options()
        self.assertEqual([], correct_opts)

        # Correct arguments test for just the help flag
        self.generator.argv += ["-h"]
        self.assertEqual(self.generator.get_options(), [("-h", "")])

        # Correct arguments with some other values passed
        self.generator.argv += ["-f", "testing.csv"]
        self.assertEqual(self.generator.get_options(), [("-h", ""), ("-f", "testing.csv")])

        # Some incorrect arguments passed
        self.generator.argv += ["-j", 3]
        self.assertRaises(SystemExit, self.generator.get_options)

        # Incorrect flag
        self.generator.argv = []
        self.generator.argv += [3, "-f"]
        self.assertRaises(AttributeError, self.generator.get_options)

    def test_update_parameters(self):
        # Checking help
        self.generator.argv = ["-h"]
        self.assertRaises(SystemExit, self.generator.update_parameters)

        # Checking options (correct values)
        self.generator.argv = ["-f", "testing.csv"]
        self.generator.update_parameters()
        self.assertEqual(self.generator.csv_file_name, "testing.csv")

        # Checking long options (correct values)
        self.generator.argv = ["--csv-file-name", "testing.csv"]
        self.generator.update_parameters()
        self.assertEqual(self.generator.csv_file_name, "testing.csv")

    def test_create_plots(self):

        # Here we check that a FileNotFoundError is raised, as the .csv file is incorrect
        self.assertRaises(FileNotFoundError, self.generator.create_plots)


if __name__ == '__main__':
    unittest.main()
