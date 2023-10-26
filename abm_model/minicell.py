import os
import pandas as pd
from abm_model.status import Susceptible, Infected
from abm_model.person import Person


class Minicell:
    """
    A box where all people are tracked.

    Parameters:
    ----------

    population_size:
        The size of the total population within the cell
    beta:
    recovery_period:
        The number of time steps it takes for someone to go from the infected
        class to the recovered class
    initial:
    name:
        The name of the minicell
    path:
        The path where ... are stored

    Attributes:
    ----------

    events:
        The list of transitions that has to be handled at the end of the time step
        (shall we call it queue?)
    s_list:
        The list of susceptible people
    i_list:
        The list of infectious people
    r_list:
        The list of recovered people
    all_list:
        A list containing people ordered by names
    current_time:
        The current time of the simulation
    """
    def __init__(self, I0: int = 1, population_size: int = 100, beta: float = 0.01, recovery_period: float = 1,
                 name: str = 'test', path: str = 'data', threshold: int = 5):

        cur_dir = '.'
        for other_dir in path.rsplit(sep='/'):
            cur_dir += '/' + other_dir
            if not os.path.exists(cur_dir):
                os.mkdir(cur_dir)

        # setting the epistemic parameters

        if type(beta) is not float and type(beta) is not int:
            raise TypeError("Beta must be a float")
        self.beta = beta

        if type(recovery_period) is not float and type(recovery_period) is not int:
            raise TypeError("Recovery period must be a float")
        self.recovery_period = recovery_period

        if type(I0) is not int or type(threshold) is not int:
            raise TypeError("Initial infected and thresholds must be ints")

        initial = {}
        for i in range(I0):
            initial[i] = Infected(recovery_period, 0, threshold)

        if type(population_size) is not int:
            raise TypeError("Population size must be an int")
        if population_size < I0:
            raise ValueError("Population size must be greater than I0.")
        self.population_size = population_size
        self.current_time = 0
        self.events = []
        self.s_list = []
        self.i_list = []
        self.r_list = []
        self.all_list = []
        self.name = name
        self.path = path
        self.data = pd.DataFrame(columns=('Susceptible',
                                          'Infected',
                                          'Recovered'))
        self.parent_record = {}

        # initializing each pearson in the minicell as susceptible

        statuses = {'Susceptible': self.s_list,
                    'Infected': self.i_list,
                    'Recovered': self.r_list}
        
        for name in range(population_size):
            if name in initial:
                my_person = Person(str(name), initial[name])
                statuses[str(initial[name])].append(my_person)
            else:
                my_person = Person(str(name), Susceptible())
                self.s_list.append(my_person)

        self.data._set_value(index=self.current_time, col='Susceptible', value=len(self.s_list))
        self.data._set_value(index=self.current_time, col='Infected', value=len(self.i_list))
        self.data._set_value(index=self.current_time, col='Recovered', value=len(self.r_list))

    def handle(self, event):

        """
        Update the events that are to be handled at the end of the time step

        An event is a dictionary with keys:
            'person': the target of the event

            'status': the new status specified

        Parameters:
        ----------

        event:
            The event to handle

        ACHTUNG0:
        --------

        THIS MAY CAUSE COLLISIONS IF ONE PERSON IS INFECTED
        WE SUGGEST ADDING AN HANDLE METHOD TO THE STATUS CLASS THAT TO BE CALLED BY A MINICELL
        (e.g. with) event['person'].status.handle(event['status'])
        WE SUGGEST ADDING A RAISING METHOD TO THE MINICELL CLASS THAT CAN BE CALLED BY A PERSON
        (e.g. with) cell.rising(event)
        IN THIS WAY COLLISIONS CAN BE HANDLED TOGETHER
        """

        statuses = {'Susceptible': self.s_list, 'Infected': self.i_list, 'Recovered': self.r_list}
        statuses[str(event['person'].status)].remove(event['person'])
        event['person'].status = event['status']
        statuses[str(event['person'].status)].append(event['person'])

    def update(self, dt: float = 1):

        self.current_time += dt

        """
        Changes the status of each pearson into the minicell coherently with the model
        """

        parent_record = {}
        for subject in self.i_list:
            child = subject.update(self, dt)
            if child:
                for child in child:
                    parent_record[child] = [subject.name, self.current_time]

        # handle each event raised in the updating loop above
        # (e.g. with) cell.events.append({'person':target,'status':Infected})
        # ACHTUNG2: read achtung0 above

        for event in self.events:
            self.handle(event)
        self.events = []
        self.parent_record.update(parent_record)
        self.data._set_value(index=self.current_time, col='Susceptible', value=len(self.s_list))
        self.data._set_value(index=self.current_time, col='Infected', value=len(self.i_list))
        self.data._set_value(index=self.current_time, col='Recovered', value=len(self.r_list))


def run_minicell(I0: int = 1, population_size: int = 100, beta: float = 0.01, recovery_period: float = 1, name: str = 'test', path: str = 'data', threshold: int = 5, total_time: int = 10):

    cell = Minicell(I0, population_size, beta, recovery_period, name, path, threshold)

    for i in range(total_time):
        cell.update(1)

    return cell.data
