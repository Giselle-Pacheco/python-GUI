import serial, time

ard = serial.Serial('COM3',9600)
datos=ard.readline()
while 1:
    print(datos)
    time.sleep(3)

#    https://www.youtube.com/watch?v=nZF9SwhmPRo&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=46 
# https://www.youtube.com/watch?v=fCuFDW1RoxI