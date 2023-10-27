import unittest
from unittest import TestCase
import os
from abm_model.generate_gif import GifGenerator
import shutil


class TestGenerateGif(TestCase):

    def setUp(self) -> None:
        self.generator = GifGenerator()

    def test__init__(self):
        """
        Test the initialisation function in generator
        """
        # Default case
        self.assertEqual(self.generator.help_string, "")

        # Non default case
        self.generator = GifGenerator("Test text")
        self.assertEqual(self.generator.population_size, 100)
        self.assertEqual(self.generator.total_time, 20)
        self.assertEqual(self.generator.beta, 0.01)
        self.assertEqual(self.generator.recovery_period, 3.0)
        self.assertEqual(self.generator.I_0, 1)
        self.assertEqual(self.generator.title, "test")
        self.assertEqual(self.generator.path, "data")
        self.assertEqual(self.generator.help_string, "Test text")
        # args = sys.argv[1:]
        # if "--unit" in args:
        #     args.remove("--unit")
        # self.assertEqual(self.generator.argv, args)
        self.assertEqual(self.generator.short_flags, ["h", "N", "t", "b", "D", "I", "T", "p"])
        self.assertEqual(self.generator.long_flags, ["help", "population-size", "total-time", "beta", "recovery-period",
                                                     "initial-infected", "title", "path"])

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

        # Correct arguments with some other values passed
        self.generator.argv += ["-N", 100, "--total-time", 30]
        self.assertEqual(self.generator.get_options(), [("-h", ""), ("-N", 100), ("--total-time", 30)])

        # Some incorrect arguments passed
        self.generator.argv += ["-j", 3]
        self.assertRaises(SystemExit, self.generator.get_options)

        # Incorrect order of arguments
        self.generator.argv = []
        self.generator.argv += [3, "-b"]
        self.assertRaises(AttributeError, self.generator.get_options)

    def test_update_parameters(self):
        # Checking help
        self.generator.argv = ["-h"]
        self.assertRaises(SystemExit, self.generator.update_parameters)

        # Checking all options (correct values)
        self.generator.argv = ["-N", 50, "-t", 30, "-b", 0.1, "-D", 50, "-I", 2, "-T", "testing",
                               "-p", "test_dir"]
        self.generator.update_parameters()
        self.assertEqual(self.generator.population_size, 50)
        self.assertEqual(self.generator.total_time, 30)
        self.assertEqual(self.generator.beta, 0.1)
        self.assertEqual(self.generator.recovery_period, 50)
        self.assertEqual(self.generator.I_0, 2)
        self.assertEqual(self.generator.title, "testing")
        self.assertEqual(self.generator.path, "test_dir")

        # Again with named flags
        self.generator.argv = ["--population-size", 5, "--total-time", 35, "--beta", 0.2,
                               "--recovery-period", 5, "--initial-infected", 3, "--title", "testing_again",
                               "--path", "test_dir_again"]
        self.generator.update_parameters()
        self.assertEqual(self.generator.population_size, 5)
        self.assertEqual(self.generator.total_time, 35)
        self.assertEqual(self.generator.beta, 0.2)
        self.assertEqual(self.generator.recovery_period, 5)
        self.assertEqual(self.generator.I_0, 3)
        self.assertEqual(self.generator.title, "testing_again")
        self.assertEqual(self.generator.path, "test_dir_again")

        # Checking all erroneous values raise errors
        self.generator.argv = ["-N", "hi"]
        self.assertRaises(SystemExit, self.generator.update_parameters)
        self.generator.argv = ["--total-time", "hi"]
        self.assertRaises(SystemExit, self.generator.update_parameters)
        self.generator.argv = ["-b", "hi"]
        self.assertRaises(SystemExit, self.generator.update_parameters)
        self.generator.argv = ["-D", "hi"]
        self.assertRaises(SystemExit, self.generator.update_parameters)
        self.generator.argv = ["--initial-infected", "hi"]
        self.assertRaises(SystemExit, self.generator.update_parameters)

    def test_create_gif(self):

        # Here we check that the path exists and the file is created. We will delete this path
        # at the end of the test
        self.generator.path = "test_path"
        self.generator.create_gif()
        self.assertEqual(os.path.exists(self.generator.path + "/gif_figure/"), True)
        self.assertEqual(os.path.exists(self.generator.path + '/gif_figure/' + self.generator.title + '.gif'), True)

        # This checks the other part of the if statement (if the path already exists)
        self.generator.create_gif()
        self.assertEqual(os.path.exists(self.generator.path + '/gif_figure/' + self.generator.title + '.gif'), True)
        shutil.rmtree("test_path")


if __name__ == '__main__':
    unittest.main()
