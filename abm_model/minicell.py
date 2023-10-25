import os
from status import Susceptible, Infected
import pandas as pd
from person import Person


class Minicell:
    """
    A box where all people are tracked:
        parameters:
            population_size: the number of people in the minicell
            beta: the average number of contacts per person per time
            recovery_period: average time into the infected status
            initial: a dictionary that specify initial infected and recovered in the minicell
            name: the name of the minicell
            path: the path where datas are being saved


        attributes:
            events: the list of transitions that has to be handled at the end of the time step (shall we call it queue?)
            s_list: the list of susceptible people
            i_list: the list of infectious people
            r_list: the list of recovered people
            all_list: a list containing people ordered by names
            current_time: the current time of the simulation
            name: the name of the minicell
            path: the path where dats are stored
        methods:
            update(dt): changes the status of each pearson into the minicell coherently with the model
                inputs: dt: the time lenght of the step to update
                output: None
            write_csv(path): upload the hystory on the file path.csv
                inputs: path: the path of the file where the hystory is being transcribed
                output: None
            handle(event): update the evets that are to be handled at the end of the time step
                inputs: event: the event to handle
                output: None
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
        
        self.data._set_value(index=self.current_time, col='Susceptible', value=len(self.s_list))
        self.data._set_value(index=self.current_time, col='Infected', value=len(self.i_list))
        self.data._set_value(index=self.current_time, col='Recovered', value=len(self.r_list))

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

    def handle(self, event):

        """
        an event is a dictionary with keys:
            'person': the target of the event
            'status': the new status specified
        ACHTUNG0:
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

        # ACHTUNG1: if self.all_list is modified, the .csv file will not be reliable
        
    def update(self, dt: float = 1):

        self.current_time += dt
        
        # update each person's status, persons eventually raise events during this process

        for some_list in [self.s_list, self.i_list, self.r_list]:
            for subject in some_list: subject.update(self, dt)

        # handle each event raised in the updating loop above
        # (e.g. with) cell.events.append({'person':target,'status':Infected})
        # ACHTUNG2: read achtung0 above

        for event in self.events: self.handle(event)
        self.events = []
        self.data._set_value(index=self.current_time, col='Susceptible', value=len(self.s_list))
        self.data._set_value(index=self.current_time, col='Infected', value=len(self.i_list))
        self.data._set_value(index=self.current_time, col='Recovered', value=len(self.r_list))


def run_minicell(I0: int = 1, population_size: int = 100, beta: float = 0.01, recovery_period: float = 1, name: str = 'test', path: str = 'data', threshold: int = 5, total_time: int = 10):

    cell = Minicell(I0, population_size, beta, recovery_period, name, path, threshold)

    for i in range(total_time):
        cell.update(1)

    return cell.data
