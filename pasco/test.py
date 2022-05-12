
from pasco import PASCOBLEDevice

device = PASCOBLEDevice()
device_list = device.scan()
print(device_list)
#device.disconnect()
