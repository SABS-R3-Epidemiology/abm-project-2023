
from abm_model.status import *


class Person:

    def __init__(self, id, status, d = 0):
        self.id = id
        self.history = {}
        if status == "Susceptible" or "susceptible":
            self.status = Susceptible()
        elif status == "Infected" or "infected":
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
            print()
        else:
            for key, value in self.history:
                print(self.id + " was " + key + " at day " + str(value))