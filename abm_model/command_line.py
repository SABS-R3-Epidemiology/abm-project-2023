import getopt
import sys
import os
from abm_model.minicell import Minicell

population_size = 100
beta = 0.01
recovery_period = 1.0
I_0 = 1
title = "test"
path = "data"

dirname = os.path.dirname(os.path.realpath(__file__))

argv = sys.argv[1:]
try:
    options, args = getopt.getopt(argv, "hN:b:D:I:t:p:",
                                  [
                                      "help",
                                      "population-size=",
                                      "beta=",
                                      "recovery-period=",
                                      "initial-infected=",
                                      "title=",
                                      "path=",
                                  ])
except getopt.GetoptError:
    print("Error: incorrect arguments provided. Use '--help' option for help.")
    sys.exit()

names = list(zip(*options))[0]

for name, value in options:
    if name in ['-h', '--help']:
        with open(dirname + "/help.txt", "r") as file:
            text = file.read()
        sys.exit()
    elif name in ['-N', '--population-size']:
        try:
            population_size = int(value)
        except ValueError:
            print("Error: population size should be an int")
            sys.exit()
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
    elif name in ['-t', '--title']:
        title = value
    elif name in ['-p', '--path']:
        path = value

    Minicell(I0=I_0, population_size=population_size, beta=beta, recovery_period=recovery_period,
             name=title, path=path)
