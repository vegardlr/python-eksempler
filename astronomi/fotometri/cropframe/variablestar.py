from os import listdir
from os.path import isfile, join

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

from astropy.io import fits
from astropy.visualization import astropy_mpl_style
from astropy.utils.data import get_pkg_data_filename
plt.style.use(astropy_mpl_style)
from astro_cropframe import Frame

path = 'CPVel-Vband'
fitsfiles = [join(path,f) for f in listdir(path) if isfile(join(path, f))]

for fits_file in fitsfiles:

    image_data = fits.getdata(fits_file,ext=0)
    star = Frame(658,685,10,'Star')
    star_image = star.crop(image_data)
    star_flux = star.flux(image_data)
    star_peak = star.peak(image_data)
    dark = Frame(700,520,10,'Dark')
    dark_image = dark.crop(image_data)
    dark_flux = dark.flux(image_data)
    dark_peak = dark.peak(image_data)
    rel_flux = star_flux-dark_flux

    print("Fits file:",fits_file)
    print("Pixels   :",image_data.shape)
    print("Range    : (",np.min(image_data),",",np.max(image_data),")")
    print("Star flux: ",star_flux)
    print("Star peak: ",star_peak)
    print("Dark flux: ",dark_flux)
    print("Dark peak: ",dark_peak)
    print("Rel. flux: ",rel_flux)
    print("SN ratio : ",rel_flux / dark_flux)
    print()

    #vmax = input("Set max (white level): ")
    #vmin = input("Set min (black level): ")
    vmax = 1000
    vmin = 10

    #plt.imshow(image_data,cmap='gray',norm=LogNorm())
    plt.imshow(image_data,cmap='gray',vmin=vmin,vmax=vmax)
    plt.plot(star.xframe,star.yframe,'b-')
    plt.plot(dark.xframe,dark.yframe,'r-')
    plt.title("Image")
    plt.grid(False)
    plt.colorbar()
    plt.show()

    #plt.imshow(star_image,cmap='gray',norm=LogNorm())
    plt.imshow(star_image,cmap='gray',vmin=vmin,vmax=vmax)
    plt.title("Star")
    plt.grid(False)
    plt.colorbar()
    plt.show()

    #plt.imshow(dark_image,cmap='gray',norm=LogNorm())
    plt.imshow(dark_image,cmap='gray',vmin=vmin,vmax=vmax)
    plt.title("Dark (background)")
    plt.grid(False)
    plt.colorbar()
    plt.show()

    #break
    a = input("Done?")


#LIbrary: https://stak-notebooks.readthedocs.io/_/downloads/en/latest/pdf/
#Image analysis: OpenCV
