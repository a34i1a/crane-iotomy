import serial
import time
ser = serial.Serial('/dev/cu.usbmodemFD121', 9600)
ser.write("Hi")
time.sleep(10)
ser.flush()
# ser.write('413')
# print ser.readline()
while True:
	# must send 4 digit number - 0000 to 1022 followed by !
	ser.write("0024!")
	print ser.readline()
	