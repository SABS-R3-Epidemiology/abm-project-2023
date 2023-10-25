import getopt
import sys
import os
from plot import Plotter

help_text = """

python abm_model/generate_plots.py [--help] [--csv_file_name="plot_data_test.csv"]

--help                  -h	    Print help
--csv_file_name         -f      Title of the .csv file containing the required data for plotting
"""

csv_file_name = "plot_data_test"

dirname = os.path.dirname(os.path.realpath(__file__))

argv = sys.argv[1:]
try:
    options, args = getopt.getopt(argv, "hf:",
                                  [
                                      "help",
                                      "csv_file_name=",
                                  ])
except getopt.GetoptError:
    print("Error: incorrect arguments provided. Use '--help' option for help.")
    sys.exit()

if len(options) != 1:
    print("Error: either use '--help' option for help, or '--csv_file_name' to "
          "state the file containing the data you wish to be plotted")
    sys.exit()

names = list(zip(*options))[0]

for name, value in options:
    if name in ['-h', '--help']:
        print(help_text)
        sys.exit()
    elif name in ['-f', '--csv_file_name']:
        csv_file_name = value

plotter = Plotter(csv_file_name)
plotter.plot_data()
