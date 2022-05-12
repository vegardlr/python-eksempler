
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)

image_data = fits.getdata('horsehead.fits')
vmin = 6000
vmax = 20000

plt.imshow(image_data,cmap='Greys_r',vmin=vmin,vmax=vmax)
plt.colorbar()
plt.grid(False)
plt.show()

# Her gjør vi to utsnitt av det store bildet
def crop(data,x,y,d=10):
    return data[x-d:x+d,y-d:y+d]

star       = crop(image_data,200,277)
background = crop(image_data,130,150)

#Vis utstnitt av en stjerne
plt.imshow(star,cmap='Greys_r',vmin=vmin,vmax=vmax)
plt.colorbar()
plt.grid(False)
plt.show()

#Vis utsnitt av et mørkt område
plt.imshow(background, cmap='Greys_r',vmin=vmin,vmax=vmax)
plt.colorbar()
plt.grid(False)
plt.show()

#Finn piksel-verdier og skriv de ut
pixelareal = 20*20
flux = np.sum(star)/pixelareal
dark = np.sum(background)/pixelareal
print("Starflux / backgr.flux : ",flux/dark)
print("Star average flux      : ",flux)
print("Background average flux: ",dark)
print("Star peak flux         : ",np.max(star))
print("Background peak flux   : ",np.max(background))
