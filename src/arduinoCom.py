import serial, time
from tkinter import *


class SerialCommunication():

    def __init__(board, port, baudrate): #Here we use board to refer too the instance of the specific board in use
       
        board.port = port
        board.baudrate = baudrate
        board.data = []
        board.connection = None
        board.connected = False
        board.gettingData = False #isReading
        board.samplesCount = 0
        sampleTime=1

        try:
            board.connection = serial.Serial(port, baudrate)
            print(f"Connected")
            board.connected = True
        except:
            print(f"Error connecting to Arduino:")
            board.connected = False

   
    def setSampleTime(board, sampleTime):
        """
        Envía el tiempo de muestreo al Arduino.
        """
        if board.connected:
            board.connection.write(str(sampleTime).encode())
            board.connection.write(b'\n')
    
    def getData(board):
        board.gettingData=True
        board.data=[]


    def readData(board, samplingTime, numberSamples):
        """
        Mientras este activa la bandera de leer y el arduino, además 
        que el numero de datos recolectados hasta el momento sea menor al numeros de muestras
        seguira capturando muestras
        """
        while board.gettingData and board.connected and len(board.data) < numberSamples:
            try:
                recoveredData = float(board.connection.readline().strip())
                board.data.append(recoveredData)
            except ValueError:
                pass
            time.sleep(samplingTime)
            
    def stopData(board):
        board.gettingData=False
        

            



#    https://www.youtube.com/watch?v=nZF9SwhmPRo&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=46 
# https://www.youtube.com/watch?v=fCuFDW1RoxI