
import numpy as np


class Status:
    pass

    
class Susceptible(Status):
    pass


class Recovered(Status):
    pass



class Infected(Status):

    def __init__(self, d, current_time):
        self.expiry_date = current_time + np.random.poisson(d - 1) + 1    #This is to avoid an initially infected people having 0 infectious period

