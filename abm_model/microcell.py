from abm_model.person import Person
import numpy as np
import csv

class Microcell:
    
    def __init__(self, p, d, N, I0):
        self.p = p
        self.D = d
        self.N = N
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
                p_rand = np.random.poisson(self.p)
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

    def write_csv(file_name, *args):
        res = [["S", "I", "R"]]
        for arg in args:
            res += arg
        with open(file_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(res)



                


