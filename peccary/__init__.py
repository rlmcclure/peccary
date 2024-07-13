"""
The PECCARY package
"""

# explicitly set the package variable to ensure relative import work
__package__ = "peccary"
__version__ = "0.1.0"
__author__ = "Sóley Hyman"

__all__ = ["peccary","HCplots","timeseries","examples","utils"]

# import modules and important classes
from .core import peccary
from . import HCplots
from . import timeseries
from . import examples
from . import utils