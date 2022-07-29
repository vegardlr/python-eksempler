#LIVE PLOTTING WITH PASCO PYTHON MODULE
#CONTACT: kontakt@pythonskole.no
#Version 15.10.2021

# Documentation: https://pypi.org/project/pasco/
import time
from pasco.code_node_device import CodeNodeDevice

codenode = CodeNodeDevice()
print(codenode.scan())
codenode.connect_by_id('354-873')
smilemunn = [[0,0],[4,0],
            [2,1],
            [0,2],[4,2],
            [1,3],[2,3],[3,3]]
codenode.set_leds_in_array(smilemunn)

m = 0.1

for i in range(10):
    ay = codenode.read_data('Accelerationy')
    ty = codenode.read_data('TiltAngleY')
    print("Friksjonskraft",ay,"Vinkel",ty)
    time.sleep(1)

codenode.disconnect()


