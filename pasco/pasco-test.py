import pasco, time
device = pasco.CodeNodeDevice()
device.connect_by_id('354-873')

device.set_rgb_led(5,0,0)
device.set_sound_frequency(100)
device.set_leds_in_array([[2,2]])

datatype = 'Loudness'

time.sleep(3)
#print("Measurement list:", device.get_measurement_list())
print('Read data:',device.read_data(datatype))
time.sleep(3)

device.set_sound_frequency(0)
#device.set_rgb_led(0,0,0)
#device.set_leds_in_array([])

print('Read data:',device.read_data(datatype))
time.sleep(3)
print('Read data:',device.read_data(datatype))

for i in range(10):
    print('Read data',i,':',device.read_data(datatype))
    time.sleep(1)

device.disconnect()

