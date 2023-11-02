import os
from abm_model.minicell import run_minicell
from abm_model.generator import Generator


class DataGenerator(Generator):
    """
    This class inherits from Generator, and is run by the user from a command line terminal to
    generate data for the given parameters and will write to a .csv file.

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
        The list of short flags that the user can enter, without the "-". The acceptable options are
        "h", "N", "t", "b", "D", "I", "T" and "p".
    long_flags:
        The list of long flags that the user can enter, without the "--". The acceptable options are
        "help", "population-size", "total-time", "beta", "recovery-period", "initial-infected", "title"
        and "path".
    population_size:
        This is the total number of individuals for the simulation.
    total_time:
        This is the number of time steps (hours) that the simulation will run for.
    beta:
        This is the effective contact rate of the disease.
    recovery_period:
        This is the average number of days (passed to a Poisson random variable) that an infected
        individual stays infected for.
    I_0:
        This is the number of individuals infected at the beginning of the simulation.
    title:
        This is the title of the .csv file. However, this will normally default to a title
        involving population_size and I_0.
    path:
        This is the path in which the .csv file will be stored. This will normally default
        to abm-project-2023/data/csv_files.
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
        """
        This method searches through the user inputted flags from options and will
        print out the help_string if "-h" or "--help" is entered. Otherwise, it will
        use the user inputted flags and values to replace the defaults.

        Return:
        ----------
        None
        """
        options = self.get_options()

        if len(options) >= 1:
            for name, value in options:
                if name in ['-h', '--help']:
                    print(self.help_string)
                    self.help_string = "printed"
                    break
                elif name in ['-N', '--population-size']:
                    try:
                        self.population_size = int(value)
                    except ValueError:
                        raise RuntimeError("Error: population size should be an int")
                elif name in ['-t', '--total-time']:
                    try:
                        self.total_time = int(value)
                    except ValueError:
                        raise RuntimeError("Error: total time should be an int")
                elif name in ['-b', '--beta']:
                    try:
                        self.beta = float(value)
                    except ValueError:
                        raise RuntimeError("Error: beta value should be a float or an int")
                elif name in ['-D', '--recovery-period']:
                    try:
                        self.recovery_period = float(value)
                    except ValueError:
                        raise RuntimeError("Error: recovery period should be a float or an int")
                elif name in ['-I', '--initial-infected']:
                    try:
                        self.I_0 = int(value)
                    except ValueError:
                        raise RuntimeError("Error: initial number of infected should be an int")
                elif name in ['-T', '--title']:
                    self.title = value
                elif name in ['-p', '--path']:
                    self.path = value

    def create_csv(self):
        """
        This method takes all the provided parameters to invoke the run_minicell method from minicell. This
        method produces a pandas data_frame, which can then be converted into a .csv file as described
        in the method.
        Return:
        ----------
        None
        """

        data_frame = run_minicell(I0=self.I_0, population_size=self.population_size, total_time=self.total_time,
                                  beta=self.beta, recovery_period=self.recovery_period, name=self.title, path=self.path)

        self.title = "total_" + str(self.population_size) + "_initial_" + str(self.I_0)
        if not os.path.exists(self.path + "/csv_files/"):
            os.makedirs(self.path + "/csv_files/")
        data_frame.to_csv(self.path + '/csv_files/' + self.title + '.csv')


# The next few lines will be run by the command line
help_text = """

python abm_model/generate_data.py [--help] [--population-size=100] [--total-time=20]
 [--beta=0.01] [--recovery-period=3.0]
 [--initial-infected=1] [--title="test"] [--path="data"]

--help                  -h      Print help
--population-size=100   -N      Total number of individuals in the simulation
--total-time=20         -t      Number of time steps (days) that the simulation will run for
--beta=0.01             -b      Effective contact rate of the disease
--recovery-period=3.0   -D      Average number of time steps for which an individual is infected
--initial-infected=1    -I      Initial number of infected individuals
--title="test"          -T      Title attached to the output .csv file
--path="data"           -p      Path to the directory containing the .csv file and the plots
"""

if __name__ == "__main__":
    generator = DataGenerator(help_text)
    generator.update_parameters()
    if generator.help_string != "printed":
        generator.create_csv()
