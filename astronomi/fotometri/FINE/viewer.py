#!/usr/bin/env python3
from os import listdir
from os.path import isfile, join

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

from astropy.io import fits
from astropy.visualization import astropy_mpl_style
from astropy.utils.data import get_pkg_data_filename
from astropy import units as u
from astropy.coordinates import SkyCoord
plt.style.use(astropy_mpl_style)


fixed_minmax = True
vmin = 100
vmax = 10000

path = 'CPVel-Vband'
fitsfiles = [join(path,f) for f in listdir(path) if isfile(join(path, f))]

for fits_file in fitsfiles:
    hdul = fits.open(fits_file)
    hdr  = hdul[0].header
    data = hdul[0].data
    hdul.close()
    print(hdr)
    print("OBSERVATION")
    print("Object:  ",hdr['object'])
    print("R.A.:    ",hdr['ra'])
    print("Dec.:    ",hdr['dec'])
    print("Filter:  ",hdr['filter'])
    print("Site:    ",hdr['site'])
    print("Date:    ",hdr['date-obs'])
    print()
    print("DATA")
    print("Fits:    ",fits_file)
    print("Size:    ",data.shape)
    print("Min:     ",np.min(data))
    print("Max:     ",np.max(data))
    print("Avg:     ",np.mean(data))
    print("Std:     ",np.std(data))

    pixscale = hdr['PIXSCALE']
    pixscale = hdr['SECPIX'] #arcsec/pixel

    c= SkyCoord(hdr['ra'],hdr['dec'],unit=(u.hourangle, u.deg))
    try:
        c0
    except NameError:
        c0=c

    print(c.dec.arcsec)
    print("Coordinate shift: ")
    print("Coord      :",c)
    print("Coord_first:",c0)
    radiff  = c.ra.arcsec-c0.ra.arcsec
    decdiff = c.dec.arcsec-c0.dec.arcsec
    print("Diff (arcsec):",radiff, decdiff)
    print("Diff (pixels):",radiff/pixscale,decdiff/pixscale)


    if False:
        plt.hist(data.flatten(),bins='auto')
        plt.show()

    if not fixed_minmax:
        answer = input("Set vmin/vmax [y/n]?")
        if answer == 'y' or answer == 'Y':
            vmin = float(input("Vmin="))
            vmax = float(input("Vmax="))
        else:
            vmin = None
            vmax = None
    if True:
        plt.imshow(data,cmap='gray',norm=LogNorm(vmin=vmin,vmax=vmax))
        plt.colorbar()
        plt.show()

