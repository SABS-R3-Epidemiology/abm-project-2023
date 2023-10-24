import numpy as np
from .status import *

class Person:
    '''
    This class contains information for each agent.
    --------------
    Parameters:

    id(str): a unique id/name for each agent
    status(str): has to be either "Susceptible" or "Infected" indicating the initial status of a person
    d(float, int, Optional): should be an input from the model, indicating the average recovery period for initially infected people

    Attributes:

    .id(str): same as above
    .status(status object): use composition with status class, indicating the status for each person
    .history(dic): a dictionary containing the date of infection and date of recovery

    Methods:

    .update(cell): triggers the change of status with an input of 'Minicell' object
                   for originally susceptible people: become infected with random recovery date by triggering '.events' of 'Minicell'
                   for originally infected people: check whether it is the time to recover: if yes, recove by similar method; if no, pass
                   for originally recovered people: pass
    .read_infection_history(): print out the date of infection and recovery(if exist) based on '.history' attribute
    
    '''
    def __init__(self, id: str, initial_status):

        self.id = id
        self.history = {}
        self.status = initial_status
    
    def __eq__(self, other):
        return self.id == other.id

    def update(self, cell, dt):

        if isinstance(self.status, Susceptible):
            pass
        elif isinstance(self.status, Infected):
            if cell.current_time == self.status.expiry_date:
                self.history["recovered"] = cell.current_time
                cell.events.append({"person": self, "status": Recovered()})
            elif cell.s_list != []:
                number_of_infections = np.random.poisson(min(cell.P * dt * len(cell.s_list), self.status.threshold))
                next_infections = np.random.choice(cell.s_list, size = number_of_infections)
                for next_infection in next_infections:
                    cell.events.append({"person": next_infection, "status": Infected(cell.D, cell.current_time, threshold = self.status.threshold)})
                    next_infection.history["infected"] = cell.current_time
        elif isinstance(self.status, Recovered):
            pass

    def read_infection_history(self):

        if len(self.history) == 0:
            print(self.id + " was not infected")
        else:
            for key, value in self.history.items():
                print(self.id + " was " + key + " at day " + str(value))

    def __repr__(self):

        return f"Person(ID = '{self.id}', status = {self.status})"

