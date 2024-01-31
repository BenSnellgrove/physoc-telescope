import matplotlib.pyplot as plt
import numpy as np
from astropy.visualization import astropy_mpl_style, quantity_support

import astropy.units as u
from astropy.coordinates import AltAz, EarthLocation, SkyCoord
from astropy.time import Time


target = SkyCoord.from_name("Betelgeuse")

# Aberystwyth
mylocation = EarthLocation(lat=52.4144809*u.deg, lon=-4.0879405*u.deg, height=100*u.m)

timestamp = Time("2024-01-31 00:00:00")

targetaltaz = target.transform_to(AltAz(obstime=timestamp, location=mylocation))

print(f"Target alt = {targetaltaz.alt}")
print(f"Target az = {targetaltaz.az}")
