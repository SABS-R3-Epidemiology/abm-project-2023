"""abm_model is an Agent Based Modelling library.

It contains functionality for creating, solving, and visualising the solution
of an SIR model for n individuals in a room.

"""
# Import version info
from .version_info import VERSION_INT, VERSION  # noqa

# Import main classes
from .person import Person # noqa
from .status import * # noqa
from .minicell import Minicell # noqa
from .gif_plot import *
