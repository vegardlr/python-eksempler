

hours = np.timedelta64(tid[1]-tid[0],'h').astype(float)
seconds = np.timedelta64(tid[1]-tid[0],'s').astype(float)

#N    = len(mag)
#tid_sec = #TODO gjør om tid til en array med sekunder siden start
#tid2 = np.linspace(seconds,len(mag))
#mag2 = np.interp(tid2,tid,mag)


#plt.plot(tid2,mag2,'-')
#plt.show()


#ps = np.abs(np.fft.fft(mag))**2
#time_step = 1 / 30
#freqs = np.fft.fftfreq(data.size, time_step)
#idx = np.argsort(freqs)
#plt.plot(ps)
#plt.show()
