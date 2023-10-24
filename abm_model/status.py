import numpy as np

class Status:
    '''
    Parental class to group the following three status classes

    '''
    pass

    
class Susceptible(Status):
    '''
    This class indicates a susceptible status with suitable representation

    '''
    def __repr__(self):

        return f"Susceptible"


class Recovered(Status):
    '''
    This class indicates a recovered status with suitable representation

    '''
    def __repr__(self):

        return f"Recovered"



class Infected(Status):
    '''
    This class indicates a infected status with suitable representation
    ------------
    Parameters:

    d(float, int): the average recovery period
    current_time(int): should be an input from the microcell indicating the current time. In order to calculate the recovery date
    threshold(int): the maximum number of people that a person can infect in one day(avoid infect too many people with too many susceptibles)

    '''
    def __init__(self, d, current_time: int, threshold: int = 0):

        if (type(d) != int and type(d) != float):
            raise TypeError("d needs to be in int or float data type.")
        if d <= 0:
            raise ValueError("You need to specify a positive recovery period.")
        self.expiry_date = current_time + np.random.poisson(d - 1) + 1
        #This is to avoid an infected people having 0 infectious period
        self.threshold = threshold

    def __repr__(self):

        return f"Infected"

