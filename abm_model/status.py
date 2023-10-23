
import numpy as np


class Status:
    pass

    
class Susceptible(Status):

    def __repr__(self):
        return f"Susceptible"


class Recovered(Status):
    
    def __repr__(self):
        return f"Recovered"



class Infected(Status):

    def __init__(self, d, current_time):
        self.expiry_date = current_time + np.random.poisson(d - 1) + 1    
        #This is to avoid an initially infected people having 0 infectious period

    def __repr__(self):
        return f"Infected with recovery date on day {self.expiry_date}"

