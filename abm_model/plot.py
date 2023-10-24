import matplotlib.pylab as plt
import numpy as np
import os
import csv


def plot_data(title: str = ""):
    """

    :param title: An optional title for the plot_data file
    :return:
    """

    with open("data/plot_data_" + title + ".csv", "r") as csv_file:
        # Structure of csv file (with no whitespace in between):
        # Time,          Susceptible,     Infected,     Recovered,
        # 1,             90,              10,           0,
        # 2,             79,              20,           1,
        # ...,           ...,             ...,          ...,
        lines = [line[0:4] for line in csv.reader(csv_file)]
        categories = lines[0]

        # We will exit this method if there are 0 or 1 lines only in the file as
        # there is nothing to plot

        if len(lines) <= 1:
            return

        # Here we set up the different lists containing all values
        data_dict = {category: [] for category in categories}

        for line in lines[1:]:

            # We must check that the length of str_values_list is 4 and that each value
            # can be parsed to an int
            str_values_list = line

            values_list = check_validity(str_values_list)

            # This is checking that the current time step is the first one
            if values_list[0] == 0:
                # Here, we can infer the total number of individuals and the initial number of infected.
                # We will use this to label the plots.
                total_people = sum(values_list[1:])
                initial_infected = values_list[2]

            for i, category in enumerate(categories):

                # This line will add a value to the correct category. E.g. if there is a 90
                # in the Susceptible column, then here we add 90 to the Susceptible list inside
                # the data_dict
                data_dict[category].append(values_list[i])

        # Now we can create the numpy arrays and plots for each category
        time_array = np.array(data_dict["Time"])
        for status in categories[1:]:

            # This will be a numpy array of one of the statuses (Susceptible, Infected or Recovered)
            status_array = np.array(data_dict[status])
            plt.plot(time_array, status_array, label=status)

        # Here we create the plot legends
        create_plot_legend(total_people)

        # And here we will write to a plots folder
        plot_path = "data/plots"
        create_plot_files(plot_path, total_people, initial_infected)


def check_validity(str_values_list: list[str]):

    """This method checks that `str_values_list` is of the correct length and that
    the internal values are valid. If this is not the case, then errors will be raised.

    :param str_values_list: A inputted list of strings
    :return: The list of strings converted into ints (if they are valid)
    """
    if len(str_values_list) != 4:
        raise ValueError("Each line in the .csv file must have 4 values")

    try:
        values_list = [int(value) for value in str_values_list]

        for value in values_list:
            if value < 0:
                raise ValueError("All values in the .csv file must be non-negative")

        return values_list

    except ValueError:
        raise ValueError("Each value in the .csv file must be an integer")


def create_plot_files(plot_path: str, total_people: int, initial_infected: int):
    """This will send the files to the correct location

    :param plot_path: The path pointing to the directory we wish to write into
    :param total_people: Total number of people in the model
    :param initial_infected: Initial number of people infected
    :return:
    """
    if not os.path.exists(plot_path):
        os.makedirs(plot_path)

    file_name = "total_" + str(total_people) + "_initial_" + str(initial_infected)

    destination = plot_path + "/" + file_name + ".png"
    plt.savefig(destination)


def create_plot_legend(total_people: int):
    """We create the plot legend and title here

    :param total_people: Total number of people in the model
    :return:
    """
    plt.legend()
    plt.ylabel("Number of individuals")
    plt.xlabel("Time step")

    plt.title("Agent Based Model for " + str(total_people) + " individuals in a room")


plot_data("test")
