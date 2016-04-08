import serial
import time
ser = serial.Serial('/dev/cu.usbmodemFD121', 9600)
print("flushing serial...")
ser.flush()
sf=00
sfTring = "%03d" % sf
ser.write(sfTring)
while True:
	print ser.readline()
	ser.write("000")
	ser.flushOutput()
	print ser.readline()
	ser.write("123")
ser.flushInput()

# ser.write('413')
# print ser.readline()
# def read_value():
# 	totalSize = 0
# 	sf=0
# 	while True:
# 		# must send 4 digit number - 0000 to 1022 followed by !
# 		sfTring = "%04d" % sf
# 		ser.write(sfTring+"!")
# 		#time.sleep(10)
# 		
# 		#print "Send this " + str(sf)
# 		sf+=1
# 		if sf > 1022:
# 			sf = 0
# 		time.sleep(1000)
# 		bytesToRead = ser.inWaiting()
# 		print(bytesToRead)
# 		if (bytesToRead !=0):
# 			#batchAlignCheck = bytesToRead % 4
# 			if (bytesToRead>=0):
# 				totalSize+=bytesToRead
# 				print "Read this " + ser.readline()
# 		else:
# 			ser.read(bytesToRead)
# 			print("ERROR: THROW AWAY " + str(bytesToRead) + " bytes")
# 			ser.flushInput()
# def main():
# 	read_value()
# 	
# if __name__ == '__main__':
# 	main()