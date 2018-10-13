import serial
import time

xb=serial.Serial("/dev/ttyUSB1",9600,timeout=1)

xb.write("+++")
while True:
	
	cmd=raw_input("enter ur command\n")
	xb.write(cmd+"\r\n")
