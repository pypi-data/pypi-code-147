# This file is automatically generated, DO NOT EDIT
# fmt: off

from os.path import abspath, join, dirname, exists
_root = abspath(dirname(__file__))

# runtime dependencies
import wpiutil._init_wpiutil
from ctypes import cdll

try:
    _lib = cdll.LoadLibrary(join(_root, "lib", "libwpinet.so"))
except FileNotFoundError:
    if not exists(join(_root, "lib", "libwpinet.so")):
        raise FileNotFoundError("libwpinet.so was not found on your system. Is this package correctly installed?")
    raise FileNotFoundError("libwpinet.so could not be loaded. There is a missing dependency.")

