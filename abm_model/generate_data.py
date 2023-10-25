import getopt
import sys
import os
from minicell import run_minicell

help_text = """

python abm_model/generate_data.py [--help] [--population-size=100] [--total-time=20] [--beta=0.01] [--recovery-period=1.0]
 [--initial-infected=1] [--csv_file_name="test"] [--path="data"]

--help		    		-h	    Print help
--population-size=100   -N	    Total number of individuals in the simulation
--total-time=20         -t      Number of time steps (days) that the simulation will run for
--beta=0.01  			-b	    Effective contact rate of the disease
--recovery-period=1.0	-D		Average number of time steps of which an individual is infected
--initial-infected=1	-I	    Initial number of infected individuals
--csv_file_name="test"          -T      Title attached to the output .csv file
--path="data"	        -p	    Path to the directory containing the .csv file and the plots
"""

population_size = 100
total_time = 20
beta = 0.01
recovery_period = 1.0
I_0 = 1
title = "test"
path = "data"

dirname = os.path.dirname(os.path.realpath(__file__))

argv = sys.argv[1:]
try:
    options, args = getopt.getopt(argv, "hN:t:b:D:I:T:p:",
                                  [
                                      "help",
                                      "population-size=",
                                      "total-time=",
                                      "beta=",
                                      "recovery-period=",
                                      "initial-infected=",
                                      "csv_file_name=",
                                      "path=",
                                  ])
except getopt.GetoptError:
    print("Error: incorrect arguments provided. Use '--help' option for help.")
    sys.exit()

if len(options) >= 1:
    names = list(zip(*options))[0]

    for name, value in options:
        if name in ['-h', '--help']:
            print(help_text)
            sys.exit()
        elif name in ['-N', '--population-size']:
            try:
                population_size = int(value)
            except ValueError:
                print("Error: population size should be an int")
                sys.exit()
        elif name in ['-t', '--total-time']:
            try:
                total_time = int(value)
            except ValueError:
                print("Error: total time should be an int")
        elif name in ['-b', '--beta']:
            try:
                beta = float(value)
            except ValueError:
                print("Error: beta value should be a float or an int")
                sys.exit()
        elif name in ['-D', '--recovery-period']:
            try:
                recovery_period = float(value)
            except ValueError:
                print("Error: recovery period should be a float or an int")
                sys.exit()
        elif name in ['-I', '--initial-infected']:
            try:
                I_0 = int(value)
            except ValueError:
                print("Error: initial number of infected should be an int")
                sys.exit()
        elif name in ['-t', '--csv_file_name']:
            title = value
        elif name in ['-p', '--path']:
            path = value

    data_frame = run_minicell(I0=I_0, population_size=population_size, total_time=total_time, beta=beta,
                              recovery_period=recovery_period, name=title, path=path)
    title = "total_" + str(population_size) + "_initial_" + str(I_0)
    data_frame.to_csv(path + '/data_' + title + '.csv')
