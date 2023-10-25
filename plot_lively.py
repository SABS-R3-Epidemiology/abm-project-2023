import matplotlib.pyplot as plt
import numpy as np
import math
from abm_model.person import Person
from abm_model.status import *
from matplotlib.animation import FuncAnimation

class Point:

    def __init__(self, position, data = None, history = None):

        self.position = position
        self.data = data
        self.history = history


def plot_lively(cell):

    # Setup the points position
    N = cell.population_size

    boundary_x = [0, 4, 4, 0, 0]
    boundary_y = [0, 0, 4, 4, 0]

    x_min = 0.1
    x_max = 3.9
    y_min = 0.125
    y_max = 3.875

    point_number_onedim = math.ceil(np.sqrt(N))

    x_values = np.linspace(x_min, x_max, point_number_onedim)
    y_values = np.linspace(y_min, y_max, point_number_onedim)

    x_mesh, y_mesh = np.meshgrid(x_values, y_values)

    x_corrds = x_mesh.flatten()
    y_corrds = y_mesh.flatten()

    # Import the points data and information from the model
    point_list = []

    for i in range(point_number_onedim ** 2):
        point_list.append(Point(x_corrds[i], y_corrds[i]))

    all_list = cell.s_list + cell.i_list + cell.r_list

    for j in len(all_list):
        point_list[j].data = all_list[j]
        if isinstance(point_list[j].data.status, Infected):
            try:
                point_list[j].history = cell.parent_record[point_list[j].data.name]
            except:
                point_list[j].history = [None, 0]
        elif isinstance(point_list[j].data.status, Susceptible):
            point_list[j].history = [None, 'Susceptible']
        else:
            try:
                point_list[j].history = cell.parent_record[point_list[j].data.name] + ['Recovered']
            except:
                point_list[j].history = [None, 0, 'Recovered']

    point_list = [point for point in point_list if isinstance(point.data, Person)]

    # Setup the .gif figure
    fig, ax = plt.subplot()
    num_frames = cell.current_time + 1

    def update(point_list, time):
        ax.clear()
        ax.plot(boundary_x, boundary_y, linestyle='-')
        a = 
        ax.scatter(a, b, marker='o')
        plt.xlim(0, 4)
        plt.ylim(0, 4)

    # Create a plot
    plt.plot(boundary_x, boundary_y, linestyle='-')
    plt.scatter(a, b, marker='o')

    # Set axis limits to fit the box
    plt.xlim(0, 4)
    plt.ylim(0, 4)

    # Add labels and title (optional)


    # Show the plot
    plt.axis('off')




