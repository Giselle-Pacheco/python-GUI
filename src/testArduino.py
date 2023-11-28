import serial, time
from arduinoCom import connectPort

ard=connectPort('COM12',9600)

# ard=serial.Serial('COM12',9600)
datos=ard.readline()

while 1:
    print(datos.decode('utf-8'))
    time.sleep(3)

