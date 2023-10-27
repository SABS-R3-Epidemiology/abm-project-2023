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
from .generator import Generator # noqa
from .generate_plots import PlotGenerator # noqa
from .generate_data import DataGenerator # noqa
from .generate_gif import GifGenerator # noqa
from tests import * # noqa
