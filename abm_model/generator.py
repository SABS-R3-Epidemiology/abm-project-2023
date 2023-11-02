# import sys
# import getopt
#
#
# class Generator:
#     """
#     The base class for classes to be run from the command line given user input flags.
#
#     Parameters:
#     ----------
#
#     help_string:
#         The text to be outputted to the user if "-h" or "--help" flags are appended
#
#     Attributes:
#     ----------
#
#     argv:
#         The list of all arguments that the user enters as flags. E.g. if the user has specified
#         the help flag then argv = ["-h"] or ["--help"]
#     short_flags:
#         The list of short flags that the user can enter, without the "-". For the base class,
#         this is only "h".
#     long_flags:
#         The list of long flags that the user can enter, without the "--". For the base class,
#         this is only "help".
#     """
#
#     def __init__(self, help_string: str = ""):
#         """
#
#         :param help_string: The text that will be outputted if "--help" is entered
#         Parameters:
#         ----------
#
#         help_string:
#             The text that will be outputted if "--help" is entered
#
#         """
#         self.help_string = help_string
#         args = sys.argv[1:]
#         self.argv = args.copy()
#         if "--unit" in self.argv:
#             self.argv.remove("--unit")
#         self.short_flags = ["h"]
#         self.long_flags = ["help"]
#
#     def get_options(self) -> list[tuple[str, str]]:
#         """This uses the `getopt` module to parse command line options entered by the user
#
#         Return:
#         ------
#
#         A list of tuples containing the flag and value that the user has entered
#         """
#         try:
#             short_flags_string = self.short_flags[0]
#             for flag in self.short_flags[1:]:
#                 short_flags_string += flag + ":"
#             long_flags_opt = [self.long_flags[0]] + [long_flag + "=" for long_flag in self.long_flags[1:]]
#
#             options, args = getopt.getopt(self.argv, short_flags_string, long_flags_opt)
#             return options
#         except getopt.GetoptError:
#             raise RuntimeError("Error: incorrect arguments provided. Use '--help' option for help.")
#
#     def update_parameters(self):
#         """
#         Raises an error when called
#         """
#         raise NotImplementedError("Must call from a subclass")
