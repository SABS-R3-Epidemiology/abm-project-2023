from abm_model.plot import Plotter
from abm_model.generator import Generator


class PlotGenerator(Generator):
    """
    This class inherits from Generator, and is run by the user from a command line terminal to
    generate plots from an existing .csv file containing data from a simulation.

    Parameters:
    ----------

    help_string:
        The text to be outputted to the user if "-h" or "--help" flags are appended

    Arguments:
    ----------
    argv:
        The list of all arguments that the user enters as flags. E.g. if the user has specified
        the help flag then argv = ["-h"] or ["--help"]. Note that this is inherited from the base
        class.
    short_flags:
        The list of short flags that the user can enter, without the "-". The only options for this
        class are "h" and "f".
    long_flags:
        The list of long flags that the user can enter, without the "--". The only options for this
        class are "help" and "csv-file-name".
    csv_file_name:
        This is the name of the file containing the data that the user wishes to plot.
    """

    def __init__(self, help_string: str = ""):
        """

        Parameters:
        ----------
        help_string:
            The text to be outputted to the user if "-h" or "--help" flags are appended
        """
        super().__init__(help_string)

        # The default values
        self.csv_file_name = "default.csv"
        self.short_flags += ["f"]
        self.long_flags += ["csv-file-name"]

    def update_parameters(self):
        """
        This method searches through the user inputted flags from options and will
        print out the help_string if "-h" or "--help" is entered. If a csv_file_name is
        specified then it will use this as the required data file.

        Return:
        ----------
        None
        """
        options = self.get_options()

        if len(options) > 1:
            raise RuntimeError("Error: either use '--help' option for help, or '--csv-file-name' to "
                  "state the file containing the data you wish to be plotted")

        for name, value in options:
            if name in ['-h', '--help']:
                print(self.help_string)
                self.help_string = "printed"
                break
            elif name in ['-f', '--csv-file-name']:
                self.csv_file_name = value

    def create_plots(self):
        """
        This method simply instantiates a Plotter instance with the desired csv_file_name
        and will then plot the data from this csv_file if it exists.
        Return:
        ----------
        None
        """
        if self.csv_file_name != "default.csv":
            Plotter(self.csv_file_name).plot_data()


# The next few lines will be called by the user from the command line
help_text = """

python abm_model/generate_plots.py [--help] [--csv_file_name="plot_data_test.csv"]

--help                  -h	    Print help
--csv_file_name         -f      Title of the .csv file containing the required data for plotting
"""
generator = PlotGenerator(help_text)
generator.update_parameters()
if generator.help_string != "printed":
    generator.create_plots()
