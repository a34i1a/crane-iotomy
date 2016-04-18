#!/usr/bin/env python
import serial
import time
import threading

global ser
ser = serial.Serial('/dev/cu.usbmodemFD121', 9600)
print("connecting, leave me alone for a sec...")
time.sleep(7)
print("i'm back")

def read_from_arduino():
	k = 0
	while k < ser.inWaiting():
		buff = ser.readline()
		print(buff)
def write_to_arduino():
	print('-255->-1: turn motors CW; 1->255: CCW; 0->brake; 666->hard stop')
	x = input('how fast to turn motors? ')
	if x<-255 or (x>255 and x!=666):
		print('sorry, please input in range specified.')
	else:
		if x<0:
			# three digits followed by 1! for CW
			toWrite = "%03d1!" %(-x)
			ser.write(toWrite)
		else:
			# three digits followed by 0! for CCW
			toWrite = "%03d0!" %(x)
			ser.write(toWrite)
while True:
	write_to_arduino()
	read_from_arduino)()
# 	
# if __name__ == '__main__':
# 	main()
