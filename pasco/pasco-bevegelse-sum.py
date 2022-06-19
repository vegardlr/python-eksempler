
from pylab import *
import time
from pasco.pasco_ble_device import PASCOBLEDevice
from pasco.code_node_device import CodeNodeDevice

smilemunn = [[0,0],[4,0],[2,1],[0,2],[1,3],[2,3],[3,3],[4,2]]

codenode  = CodeNodeDevice()
codenode.connect_by_id('354-873')
codenode.set_leds_in_array(smilemunn)

bevegelse = PASCOBLEDevice()
bevegelse.connect_by_id('943-452')

for i in range(100):
    p = codenode.read_data('CartPosition')
    a = bevegelse.read_data('Position')
    print(p,a)

codenode.disconnect()    
bevegelse.disconnect()
