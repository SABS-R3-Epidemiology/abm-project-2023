import matplotlib.pylab as plt
import numpy as np
import os


def plot(title: str = ""):
    """

    :param title: An optional title for the plot_data file
    :return:
    """

    with open("plot_data_" + title + ".csv", "r") as csv_file:
        # Structure of csv file (with no whitespace in between):
        # Time,          Susceptible,     Infected,     Recovered,
        # 1,             90,              10,           0,
        # 2,             79,              20,           1,
        # ...,           ...,             ...,          ...,
        lines = csv_file.readlines()
        categories = lines[0].split(",")
        if len(lines) > 1:

            # Here we set up the different lists containing all values
            data_dict = {category: [] for category in categories}

            for line in lines[1:]:

                # We must check that the length of values_list is 4 and that each value
                # can be parsed to an int
                values_list = line.split(",")

                if values_list != 4:
                    raise ValueError("Each line in the .csv file must have 4 values")

                try:
                    values_list = [int(value) for value in values_list]

                    for value in values_list:
                        if value < 0:
                            raise ValueError("All values in the .csv file must be non-negative")

                    # This is checking that the current time step is the first one
                    if values_list[0] == 1:
                        # Here, we can infer the total number of individuals and the initial number of infected.
                        # We will use this to label the plots.
                        N = sum(values_list[1:])
                        I_0 = values_list[2]

                except ValueError:
                    raise ValueError("Each value in the .csv file must be an integer")

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

            # Here we create the plots
            plt.legend()
            plt.ylabel("Number of individuals")
            plt.xlabel("Time step")

            plt.title("Agent Based Model for " + str(N) + " individuals in a room")

            # And here we will write to a plots folder
            plot_folder = "plots"
            if not os.path.exists(plot_folder):
                os.makedirs(plot_folder)

            file_name = "total_" + str(N) + "_initial_" + str(I_0)

            destination = plot_folder + "/" + file_name + ".png"
            plt.savefig(destination)
