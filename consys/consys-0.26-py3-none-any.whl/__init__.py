"""
Initializing the Python package
"""

from .model import Attribute
from .main import make_base


__version__ = '0.26'

__all__ = (
    '__version__',
    'Attribute',
    'make_base',
)
