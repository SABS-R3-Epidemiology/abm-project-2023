import sys
from abm_model.plot import Plotter
from abm_model.generator import Generator


class PlotGenerator(Generator):

    def __init__(self, help_string: str = ""):
        super().__init__(help_string)

        # The default values
        self.csv_file_name = "default.csv"
        self.short_flags += ["f"]
        self.long_flags += ["csv-file-name"]

    def update_parameters(self):
        options = self.get_options()

        if len(options) != 1:
            print("Error: either use '--help' option for help, or '--csv-file-name' to "
                  "state the file containing the data you wish to be plotted")
            # sys.exit()

        for name, value in options:
            if name in ['-h', '--help']:
                print(self.help_string)
                sys.exit()
            elif name in ['-f', '--csv-file-name']:
                self.csv_file_name = value

    def create_plots(self):
        plotter = Plotter(self.csv_file_name)
        plotter.plot_data()


if __name__ == "__main__":
    # The next few lines will be called by the user from the command line
    help_text = """
    
    python abm_model/generate_plots.py [--help] [--csv_file_name="plot_data_test.csv"]
    
    --help                  -h	    Print help
    --csv_file_name         -f      Title of the .csv file containing the required data for plotting
    """  # pragma: no cover
    generator = PlotGenerator(help_text)  # pragma: no cover
    generator.update_parameters()  # pragma: no cover
    generator.create_plots()  # pragma: no cover
