import numpy as np


class Status:
    """
    Parental class to group the following three status classes

    """
    pass


class Susceptible(Status):
    """
    This class indicates a susceptible status with suitable representation

    """
    def __repr__(self):

        return "Susceptible"


class Recovered(Status):
    """
    This class indicates a recovered status with suitable representation

    """
    def __repr__(self):

        return "Recovered"


class Infected(Status):
    """
    This class indicates a infected status with suitable representation
    ------------
    Parameters:

    d(float, int): the average recovery period
    current_time(int): should be an input from the microcell indicating the current time.
    In order to calculate the recovery date

    """
    def __init__(self, recovery_period: float = 1, current_time: int = 0, threshold: float = 0):

        if type(recovery_period) is not int and type(recovery_period) is not float:
            raise TypeError("recovery_period needs to be in int or float data type.")
        if recovery_period <= 0:
            raise ValueError("You need to specify a positive recovery period.")
        self.expiry_date = current_time + np.random.poisson(recovery_period - 1) + 1

        #This is to avoid an infected people having 0 infectious period
        self.threshold = threshold

    def __repr__(self):

        return "Infected"

