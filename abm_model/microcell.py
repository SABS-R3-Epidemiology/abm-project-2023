from abm_model.person import Person
import numpy as np
import csv

class Microcell:
    '''
    This class contains information of a microcell.
    --------------
    Parameters:

    p(float, int): average transmission number
    d(float, int): recovery period
    N(int): total population
    I0(int): initial infected people

    Attributes:

    .P: same as p above
    .D: same as d above
    .N: same as N above
    .I0: same as I0 above
    .s_list: list of current 'Person' objects with 'Susceptible' status
    .i_list: list of current 'Person' objects with 'Infected' status
    .r_list: list of current 'Person' objects with 'Recovered' status
    .current_time: the current time

    Methods:

    .update(dt): triggers an update of 'dt' more time steps
                 This method will: make each infected people infect random number of people, 
                                   update all above lists, 
                                   print a message after each time step,
                                   print the current time step after all 'dt' steps,
                                   return a list of lists of S I R numbers after each time step,
                                   e.g. data = [[13, 27, 60], [5, 25, 70]]
    .write_csv(file_name, *args): write the data from the previous file as a .csv file, with given file name
                            NOTE: There can be many 'data' input, since we may have many update for different times

    '''
    def __init__(self, p, d, N: int, I0: int):

        if (type(d) != int and type(d) != float):
            raise TypeError("d needs to be in int or float data type.")
        if (type(p) != int and type(p) != float):
            raise TypeError("p needs to be in int or float data type.")
        if d <= 0:
            raise ValueError("You need to specify a positive recovery period.")
        if p <= 0:
            raise ValueError("You need to specify a positive average transmission number.")
        if I0 <= 0:
            raise ValueError("You need to specify a positive I0.")
        if N < I0:
            raise ValueError("Population must be greater than I0.")
        self.P = p
        self.D = d
        self.N = N
        self.I0 = I0
        self.i_list = []
        for i in range(I0):
            id = str(i).zfill(5)
            self.i_list.append(Person(id, "Infected", d = d))
        self.s_list = []
        for i in range(I0, N):
            id = str(i).zfill(5)
            self.s_list.append(Person(id, "Susceptible", d = d))
        self.r_list = []
        self.current_time = 0
        print("Now is day " + str(self.current_time))

    def update(self, dt):

        data = []
        for i in range(self.current_time, self.current_time + dt):
            self.current_time += 1
            infected = set()
            for j in range(len(self.i_list)):
                p_rand = np.random.poisson(self.P)
                if p_rand < len(self.s_list):
                    index = np.random.randint(0, len(self.s_list) - 1, size = p_rand)
                    infected_j = []
                    for ind in index:
                        infected_j.append(self.s_list[ind])
                else:
                    infected_j = self.s_list
                infected = infected.union(set(infected_j))
            for s_person in infected:
                s_person.update(self)
            for i_person in self.i_list:
                res = i_person.update(self)
                if res == 1:
                    self.r_list.append(i_person)
            self.s_list = list(set(self.s_list).difference(infected))
            self.i_list = list(set(self.i_list).difference(self.r_list)) + list(infected)
            print("Day " + str(self.current_time) + " is updated")
            data.append([len(self.s_list), len(self.i_list), len(self.r_list)])
        print("Now is day " + str(self.current_time))
        return data

    def write_csv(self, file_name, *args):

        # Not tested yet !!!!!!!!!!

        res = [["S", "I", "R"], [self.N - self.I0, self.I0, 0]]
        for arg in args:
            res += arg
        with open(file_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(res)



                


