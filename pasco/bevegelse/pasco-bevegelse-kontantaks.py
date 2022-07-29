import time
from pasco import PASCOBLEDevice
codenode = PASCOBLEDevice()
codenode.connect_by_id('354-873')

tid_start = time.time()
for i in range(30):
    tid  = time.time() - tid_start
    acc  = codenode.read_data('Accelerationy')
    tilt = codenode.read_data('TiltAngleY')
    print("Tid: %4.1fs   Acceleration: %4.1fm/s/s   Angle: %4.1fdeg "\
         % (tid,acc,tilt))
codenode.disconnect()  