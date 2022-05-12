from pasco.pasco_ble_device import PASCOBLEDevice
device = PASCOBLEDevice()
device.connect_by_id('940-072')  #Endre ID til din sensor
print("Measurement list:", device.get_measurement_list())

