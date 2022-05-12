#https://stackoverflow.com/questions/45913007/finding-sunspots-on-fits-image-via-cv2
import cv2

from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

img_l = fits.open('hmi.Ic_45s.20170605_000000_TAI.2.continuum.fits')
img = img_l\[0\].data

plt.imshow(img) #Showing Image in matplotlib
cv2.imshow('',img) #The image is white round with black background

image = np.array(img/255, dtype = np.uint8) #Converting float32 to uint8
cv2.imshow('', image) #Getting converted image
