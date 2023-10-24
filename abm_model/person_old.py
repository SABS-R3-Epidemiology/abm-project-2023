from abm_model.status import *

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

    .update(cell): triggers the change of status with an input of 'Microcell' object
                   for originally susceptible people: become infected with random recovery date
                   for originally infected people: check whether it is the time to recover: if yes, recover; if no, pass
                   for originally recovered people: pass
             NOTE: When a infected people is changed to a recovered status, the function will return 1 to indicate this change, 
                   otherwise None is returned
    .read_infection_history(): print out the date of infection and recovery(if exist) based on '.history' attribute
    
    '''
    def __init__(self, id: str, status: str, d = 1):

        if (type(d) != int and type(d) != float):
            raise TypeError("d needs to be in int or float data type.")
        if d <= 0:
            raise ValueError("You need to specify a positive recovery period.")
        self.id = id
        self.history = {}
        if status == "Susceptible":
            self.status = Susceptible()
        elif status == "Infected":
            self.status = Infected(d, 0)
            self.history["infected"] = 0
        else:
            raise ValueError("Please specify the correct status of a person.")
        
    def update(self, cell):

        if isinstance(self.status, Susceptible):
            self.status = Infected(cell.D, cell.current_time)
            self.history["infected"] = cell.current_time
        elif isinstance(self.status, Infected):
            if cell.current_time == self.status.expiry_date:
                self.status = Recovered()
                self.history["recovered"] = cell.current_time
                return 1
            else:
                pass
        else:
            pass

    def read_infection_history(self):

        if len(self.history) == 0:
            print(self.id + " was not infected")
        else:
            for key, value in self.history.items():
                print(self.id + " was " + key + " at day " + str(value))

    def __repr__(self):

        return f"Person(ID = '{self.id}', status = {self.status})"

