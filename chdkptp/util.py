import os
import sys

from chdkptp.lua import global_lua


def str_to_bytes(x, enc='latin-1'):
    if sys.version_info[0] > 2:
        return x.encode(enc)
    else:
        return bytes(x)

def iso_to_sv96(iso):
    return global_lua.globals.exposure.iso_to_sv96(iso)


def shutter_to_tv96(shutter_speed):
    return global_lua.globals.exposure.shutter_to_tv96(shutter_speed)


def aperture_to_av96(aperture):
    return global_lua.globals.exposure.f_to_av96(aperture)


def apex_to_apex96(apex):
    x = apex*96
    return round(x) if x > 0 else -round(x)


def to_camerapath(path):
    if not path.lower().startswith("a/"):
        path = os.path.join("A", path)
    return path
