import matplotlib.pyplot as plt
import numpy as np
import math
from abm_model.person import Person
from abm_model.status import Infected, Susceptible, Recovered
from abm_model.minicell import Minicell
from matplotlib.animation import FuncAnimation
from functools import partial


class Point:

    def __init__(self, position, data=None, history=None):

        self.position = position
        self.data = data
        self.history = history

    def __repr__(self):
        return f"Point(position = {self.position}, data = {self.data}, history = {self.history})"


class gif_plotter:

    def __init__(self, cell):
        if isinstance(cell, Minicell):
            self.cell = cell
            self.point_list = None
        else:
            raise TypeError("Please input a 'Minicell' object.")

    def points_manipulation(self):

        # Setup the points position
        all_list = self.cell.s_list + self.cell.i_list + self.cell.r_list

        N = len(all_list)

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
            point_list.append(Point([x_corrds[i], y_corrds[i]]))

        for j in range(len(all_list)):
            point_list[j].data = all_list[j]
            if isinstance(point_list[j].data.status, Infected):
                try:
                    point_list[j].history = self.cell.parent_record[point_list[j].data.name]
                except:
                    point_list[j].history = [None, 0]
            elif isinstance(point_list[j].data.status, Susceptible):
                point_list[j].history = [None, 'Susceptible']
            elif isinstance(point_list[j].data.status, Recovered):
                try:
                    point_list[j].history = self.cell.parent_record[point_list[j].data.name] + [point_list[j].data.recovery_time]
                except:
                    point_list[j].history = [None, 0, point_list[j].data.recovery_time]

        point_list = [point for point in point_list if isinstance(point.data, Person)]
        self.point_list = point_list

    def gif_plotter(self):
        if self.point_list == None:
            raise KeyError("You need to run '.points_manipulation()' method firstly, or run '.plot()' method directly.")
        # Setup the .gif figure
        point_list = self.point_list
        cell = self.cell
        fig, ax = plt.subplots()
        num_frames = (cell.current_time + 1) * 2

        def update(time, point_list):
            ax.clear()
            boundary_x = [0, 4, 4, 0, 0]
            boundary_y = [0, 0, 4, 4, 0]
            ax.plot(boundary_x, boundary_y, linestyle='-')
            if time % 2 == 0:
                time = int(time / 2)
                infected_this_step = []
                for point in point_list:
                    if point.history[1] == 'Susceptible':
                        ax.scatter(point.position[0], point.position[1], c='b', marker='o')
                    elif point.history[1] > time:
                        ax.scatter(point.position[0], point.position[1], c='b', marker='o')
                    elif point.history[1] == time:
                        ax.scatter(point.position[0], point.position[1], c='r', marker='o')
                        infected_this_step.append(point)
                    elif point.history[1] < time:
                        if len(point.history) == 2:
                            ax.scatter(point.position[0], point.position[1], c='r', marker='o')
                        elif point.history[2] > time:
                            ax.scatter(point.position[0], point.position[1], c='r', marker='o')
                        else:
                            ax.scatter(point.position[0], point.position[1], c='g', marker='o')
                    plt.xlim(0, 4)
                    plt.ylim(0, 4)
                    plt.axis('off')
                    if time != 0:
                        for point in infected_this_step:
                            for all_point in point_list:
                                if all_point.data.name == point.history[0]:
                                    starting_point = all_point.position
                            dx = point.position[0] - starting_point[0]
                            dy = point.position[1] - starting_point[1]
                            ax.arrow(starting_point[0], starting_point[1], dx, dy, color='red', width=0.01, head_width=0.07, length_includes_head=True)
                ax.set_title('Day ' + str(time))
            else:
                time = int((time - 1) / 2)
                for point in point_list:
                    if point.history[1] == 'Susceptible':
                        ax.scatter(point.position[0], point.position[1], c='b', marker='o')
                    elif point.history[1] > time:
                        ax.scatter(point.position[0], point.position[1], c='b', marker='o')
                    elif point.history[1] == time:
                        ax.scatter(point.position[0], point.position[1], c='r', marker='o')
                    elif point.history[1] < time:
                        if len(point.history) == 2:
                            ax.scatter(point.position[0], point.position[1], c='r', marker='o')
                        elif point.history[2] > time:
                            ax.scatter(point.position[0], point.position[1], c='r', marker='o')
                        else:
                            ax.scatter(point.position[0], point.position[1], c='g', marker='o')
                    plt.xlim(0, 4)
                    plt.ylim(0, 4)
                    plt.axis('off')
                ax.set_title('Day ' + str(time))
            # ax.text(2, 18, 'Population = ' + str(N) + ', Beta = ' + str(cell.beta) + ', Recovery Period = ' + str(cell.recovery_period))

        # Create an animation
        anim = FuncAnimation(fig, partial(update, point_list=point_list), frames=num_frames, repeat=True)

        # Save the animation as a GIF
        anim.save('output.gif', writer='pillow', fps=1)

    def plot(self):
        self.points_manipulation()
        self.gif_plotter()

