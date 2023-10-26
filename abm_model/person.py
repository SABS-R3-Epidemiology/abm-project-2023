from uu import Error
import numpy as np

from abm_model.status import Susceptible, Infected, Recovered


class Person:
    """
    This class contains information for each agent.
    --------------
    Parameters:

    name(str): a unique id/name for each agent
    initial_status: a 'status' object indicating the initial status of the person
    d(float, int, Optional): should be an input from the model,
    indicating the average recovery period for initially infected people

    Attributes:

    .name(str): same as above
    .status(status object): use composition with status class, indicating the status for each person
    .history(dic): a dictionary containing the date of infection and date of recovery

    Methods:

    .update(cell): triggers the change of status with an input of 'Minicell' object
                   for originally susceptible people: pass
                   for originally infected people: check whether it is the time to recover:
                   if yes, recover by adding to '.events' to be handled by '.handle()';
                   if no, generate list of susceptible people to be infected
                   for originally recovered people: pass
    .read_infection_history(): print out the date of infection and recovery(if exist) based on '.history' attribute

    """
    def __init__(self, name: str, initial_status):

        self.name = name
        self.history = {}
        self.status = initial_status

    def __eq__(self, other):
        if self.name == other.name:
            if self.status == other.status:
                return True
            else:
                raise Error('Two people shall not have the same name!')
        else:
            return False

    def update(self, cell, dt):

        if isinstance(self.status, Susceptible):
            pass
        elif isinstance(self.status, Infected):
            if cell.current_time >= self.status.expiry_date:
                self.history["recovered"] = cell.current_time
                cell.events.append({"person": self, "status": Recovered()})
                self.recovery_time = cell.current_time
            elif cell.s_list:
                number_of_infections = np.random.poisson(min(cell.beta * dt * len(cell.s_list), self.status.threshold))
                next_infections = np.random.choice(cell.s_list, size=number_of_infections)
                child_record = []
                for next_infection in next_infections:
                    cell.events.append({"person": next_infection,
                                        "status": Infected(cell.recovery_period, cell.current_time,
                                                           threshold=self.status.threshold)})
                    next_infection.history["infected"] = cell.current_time
                    child_record.append(next_infection.name)
                return child_record
        elif isinstance(self.status, Recovered):
            pass

    def read_infection_history(self):

        if len(self.history) == 0:
            print(self.name + " was not infected")
        else:
            for key, value in self.history.items():
                print(self.name + " was " + key + " at day " + str(value))

    def __repr__(self):

        return f"Person(ID = '{self.name}', status = {self.status})"
