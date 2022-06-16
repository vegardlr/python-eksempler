from pasco.code_node_device import CodeNodeDevice

smilemunn = [[0,0],[4,0],[2,1],[0,2],[1,3],[2,3],[3,3],[4,2]]

codenode = CodeNodeDevice()
codenode.connect_by_id('123-405')

posisjon = codenode.read_data('CartPosition')
while posisjon < 2:
    if posisjon > 1:
        print("Forsvarlig avstand")
        codenode.set_rgb_led(0, 255, 0)
    else:
        print("Risikabel atferd!")
        codenode.set_rgb_led(255, 0, 0)
    posisjon = codenode.read_data('CartPosition')

print("Faren over!")
codenode.set_leds_in_array(smilemunn)
codenode.disconnect()    
