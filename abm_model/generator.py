import os
import sys
import getopt


class Generator:

    def __init__(self, help_string: str = ""):
        """

        :param help_string: The text that will be outputted if "--help" is entered
        """
        self.help_string = help_string
        # This will be called by the testing machine on GitHub which will not share
        # any similarities with the path. Therefore we are omitting it.
        self.dirname = os.path.dirname(os.path.realpath(__file__))  # pragma: no cover
        self.argv = sys.argv[1:]
        if "--unit" in self.argv:
            self.argv.remove("--unit")
        self.short_flags = ["h"]
        self.long_flags = ["help"]

    def get_options(self) -> list[tuple[str, str]]:
        """This uses the `getopt` module to parse command line options entered by the user

        :return: A list of tuples containing the flag and value that the user has entered
        """
        try:
            short_flags_string = self.short_flags[0]
            for flag in self.short_flags[1:]:
                short_flags_string += flag + ":"
            long_flags_opt = [self.long_flags[0]] + [long_flag + "=" for long_flag in self.long_flags[1:]]

            options, args = getopt.getopt(self.argv, short_flags_string, long_flags_opt)
            return options
        except getopt.GetoptError:
            print("Error: incorrect arguments provided. Use '--help' option for help.")
            sys.exit()

    def update_parameters(self):
        """This method is not implemented here!!

        :return:
        """
        raise NotImplementedError("Must call from a subclass")
