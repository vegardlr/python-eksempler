#THIS DOES NOT WORK
import pasco 
codenode1 = pasco.CodeNodeDevice()
codenode1.connect_by_id('354-873')
led_list = [[4,4], [0,4], [2,2]]
codenode1.set_leds_in_array(led_list, 128)
print("CodeNodeDevice ay:",codenode1.read_data('Accelerationy'))
print("CodeNodeDevice ax:",codenode1.read_data('Accelerationx'))
codenode1.disconnect()

#THIS WORKS
codenode2 = pasco.PASCOBLEDevice()
codenode2.connect_by_id('354-873')
print("PASCOBLEDevice ay:",codenode2.read_data('Accelerationy'))
print("PASCOBLEDevice ax:",codenode2.read_data('Accelerationx'))
codenode2.disconnect()
