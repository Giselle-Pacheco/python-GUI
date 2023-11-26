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

        try:
            board.connection = serial.Serial(port, baudrate)
            board.connected = True
        except:
            print(f"Error connecting to Arduino:")
            board.connected = False

            



#    https://www.youtube.com/watch?v=nZF9SwhmPRo&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=46 
# https://www.youtube.com/watch?v=fCuFDW1RoxI