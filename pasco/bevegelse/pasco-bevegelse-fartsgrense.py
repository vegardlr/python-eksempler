from pasco import PASCOBLEDevice
codenode = PASCOBLEDevice()
codenode.connect_by_id('354-873')

for i in range(30):
    fart = codenode.read_data('CartVelocity')
    if fart < 0.3:
        print("Din fart er OK")
    elif fart < 0.4:
        print("Du bør kanskje bremse litt...")
    else:
        print("Nå kjører du alt for fort!!")
codenode.disconnect()  