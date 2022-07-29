from pasco import PASCOBLEDevice
codenode  = PASCOBLEDevice()
codenode.connect_by_id('354-873')
bevegelse = PASCOBLEDevice()
bevegelse.connect_by_id('943-452')

for i in range(30):
    strekning = codenode.read_data('CartPosition')
    avstand = bevegelse.read_data('Position')
    print("Sum = %fm" % strekning+avstand)
codenode.disconnect()    
bevegelse.disconnect()
