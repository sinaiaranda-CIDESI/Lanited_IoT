import serial
ser = serial.Serial("/dev/ttyS1", 9600)
while True:
     cc=str(ser.readline())
     print(cc[2:][:-5])
