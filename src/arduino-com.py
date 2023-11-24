import serial, time

ard = serial.Serial('COM3',9600)
datos=ard.readline()
while 1:
    print(datos)
    time.sleep(3)