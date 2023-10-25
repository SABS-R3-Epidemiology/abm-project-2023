import sys
from plot import Plotter
from generator import Generator


class PlotGenerator(Generator):

    def __init__(self, help_string: str):
        super().__init__(help_string)

        # The default values
        self.csv_file_name = "plot_data_test"
        self.short_flags += ["f"]
        self.long_flags += ["csv-file-name"]

    def update_parameters(self):
        options = self.get_options()

        if len(options) != 1:
            print("Error: either use '--help' option for help, or '--csv_file_name' to "
                  "state the file containing the data you wish to be plotted")
            sys.exit()

        for name, value in options:
            if name in ['-h', '--help']:
                print(help_text)
                sys.exit()
            elif name in ['-f', '--csv-file-name']:
                self.csv_file_name = value

    def create_plots(self):
        plotter = Plotter(self.csv_file_name)
        plotter.plot_data()


help_text = """

python abm_model/generate_plots.py [--help] [--csv_file_name="plot_data_test.csv"]

--help                  -h	    Print help
--csv_file_name         -f      Title of the .csv file containing the required data for plotting
"""
generator = PlotGenerator(help_text)
generator.update_parameters()
generator.create_plots()
