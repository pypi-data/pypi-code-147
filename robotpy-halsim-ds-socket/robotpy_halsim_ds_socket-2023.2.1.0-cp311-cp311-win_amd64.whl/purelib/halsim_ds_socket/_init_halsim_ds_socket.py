# This file is automatically generated, DO NOT EDIT
# fmt: off

from os.path import abspath, join, dirname, exists
_root = abspath(dirname(__file__))

# runtime dependencies
import hal._init_wpiHal
import wpinet._init_wpinet
from ctypes import cdll

try:
    _lib = cdll.LoadLibrary(join(_root, "lib", "halsim_ds_socket.dll"))
except FileNotFoundError:
    if not exists(join(_root, "lib", "halsim_ds_socket.dll")):
        raise FileNotFoundError("halsim_ds_socket.dll was not found on your system. Is this package correctly installed?")
    raise Exception("halsim_ds_socket.dll could not be loaded. Do you have Visual Studio C++ Redistributible 2019 installed?")

