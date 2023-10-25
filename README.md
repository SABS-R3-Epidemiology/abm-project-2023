# Agent Based Model Mini-Project 2023

This project consists of an SIR model for N indidivuals in a closed room. The simulation begins with I_0 individuals with Infected Status and updates discretely each time step.

## Installation

To install a copy of the solver, open a terminal and run:

	git clone git@github.com:SABS-R3-Epidemiology/abm-project-2023.git

To make sure all dependencies are installed, in the current directory run:

	pip install ./abm-project-2023

## Class Overview

 Here is a UML class diagram for our project:

## Produce data files
Move to the abm-project-2023 directory. In the command line, run

	python abm_model/generate_data.py

This will run the simulation with pre-set parameter values, producing a .csv file containing the results of the simulation in the directory data/csv_files.

In order to change these parameter values, you will need to use commands within abm-project-2023 (see below).

## generate_data.py commands
Entering commands in the terminal will allow you to set-up a specific simulation.

A comprehensive list of the commands is provided below:


|Command|Command Shortcut|Description|
| --- | --- | --- |
|`--help`|`-h`|Print help|
|`--population-size=100`|`-N`|Total number of individuals in the simulation|
|`--total-time=20`|`-t`|Number of time steps [days] that the simulation will run for|
|`--beta=0.01`|`-b`|Effective contact rate of the disease|
|`--recovery-period=3.0`|`-D`|Average number of time steps for which an individual is infected|
|`--initial-infected=1`|`-I`|Initial number of infected individuals|
|`--title="test"`|`-T`|Title attached to the output .csv file|
|`--path="data"`|`-p`|Path to the directory containing the .csv file and the plots|


## Plotting a data file
Still within the abm-project-2023 directory, run the following command to plot the data within a given .csv file

	python abm_model/generate_plots.py -f "<file_name>.csv"

 This will produce plots for the given SIR data, which will end up in the directory data/plots. You must either specify the file_name or enter "-h" or "--help" for help.

## generate_plots.py commands
Here is a table of commands for generate_plots.py:


|Command|Command Shortcut|Description|
| --- | --- | --- |
|`--help`|`-h`|Print help|
|`--csv-file-name`|`-f`|The chosen .csv file containing the data of a simulation|


## Parameter Definitions

