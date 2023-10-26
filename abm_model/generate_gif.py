import sys
import os
from abm_model.generator import Generator
from abm_model.minicell import Minicell
from abm_model.gif_plot import gif_plotter


class GifGenerator(Generator):

    def __init__(self, help_string: str = ""):
        super().__init__(help_string)

        # The default values
        self.population_size = 100
        self.total_time = 20
        self.beta = 0.01
        self.recovery_period = 3.0
        self.I_0 = 1
        self.title = "test"
        self.path = "data"
        self.short_flags += ["N", "t", "b", "D", "I", "T", "p"]
        self.long_flags += ["population-size", "total-time", "beta", "recovery-period",
                            "initial-infected", "title", "path"]

    def update_parameters(self):
        options = self.get_options()

        if len(options) >= 1:
            for name, value in options:
                if name in ['-h', '--help']:
                    print(self.help_string)
                    sys.exit()
                elif name in ['-N', '--population-size']:
                    try:
                        self.population_size = int(value)
                    except ValueError:
                        print("Error: population size should be an int")
                        sys.exit()
                elif name in ['-t', '--total-time']:
                    try:
                        self.total_time = int(value)
                    except ValueError:
                        print("Error: total time should be an int")
                        sys.exit()
                elif name in ['-b', '--beta']:
                    try:
                        self.beta = float(value)
                    except ValueError:
                        print("Error: beta value should be a float or an int")
                        sys.exit()
                elif name in ['-D', '--recovery-period']:
                    try:
                        self.recovery_period = float(value)
                    except ValueError:
                        print("Error: recovery period should be a float or an int")
                        sys.exit()
                elif name in ['-I', '--initial-infected']:
                    try:
                        self.I_0 = int(value)
                    except ValueError:
                        print("Error: initial number of infected should be an int")
                        sys.exit()
                elif name in ['-T', '--title']:
                    self.title = value
                elif name in ['-p', '--path']:
                    self.path = value

    def create_gif(self):

        cell = Minicell(I0=self.I_0, population_size=self.population_size,
                        beta=self.beta, recovery_period=self.recovery_period, name=self.title, path=self.path)
        for i in range(self.total_time):
            cell.update(1)

        gif = gif_plotter(cell)

        self.title = "total_" + str(self.population_size) + "_initial_" + str(self.I_0)
        if not os.path.exists(self.path + "/gif_figure/"):
            os.makedirs(self.path + "/gif_figure/")
        gif.plot(path=self.path + '/gif_figure/', name=self.title)


# The next few lines will be run by the command line
help_text = """

python abm_model/generate_gif.py [--help] [--population-size=100] [--total-time=20]
 [--beta=0.01] [--recovery-period=3.0]
 [--initial-infected=1] [--title="test"] [--path="data"]

--help                  -h      Print help
--population-size=100   -N      Total number of individuals in the simulation
--total-time=20         -t      Number of time steps (days) that the simulation will run for
--beta=0.01             -b      Effective contact rate of the disease
--recovery-period=3.0   -D      Average number of time steps for which an individual is infected
--initial-infected=1    -I      Initial number of infected individuals
--title="test"          -T      Title attached to the output .gif file
--path="data"           -p      Path to the directory containing the .gif file and the plots
"""  # pragma: no cover
generator = GifGenerator(help_text)  # pragma: no cover
generator.update_parameters()  # pragma: no cover
generator.create_gif()  # pragma: no cover
