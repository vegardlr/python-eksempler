import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)

image_data = fits.getdata('M42-V-30sec.fits.fz')
vmin = 100
vmax = 7000

#Prøv med forskjellige farger (se utvalg i presentasjonen)
plt.imshow(image_data,cmap='Greys_r',vmin=vmin,vmax=vmax)
#plt.imshow(image_data,cmap='Greys_r')
plt.colorbar()
plt.grid(False)
plt.show()

