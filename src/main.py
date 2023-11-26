
import tkinter as tk
#ttk isstlye the widgets
from tkinter import ttk
import serial, time
#Conversion para arhivo csv
import csv
import matplotlib.pyplot as plt
# Librería para la grafica en tiempo real
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
#un hilo hace a la par un programa
import threading
from arduinoCom import SerialCommunication
global led

class GUIDesign:
    
    def __init__(board, root):
        board.windowLayer = root
       
        # se crea una instancia de la clase ArduinoComunication
        board.windowLayer.title("ARDUINO - Python GUI")
        # board.windowLayer.resizable(1,1)

        #Configuring frame to setup components
        # Frame para controles y botones
        board.frame = ttk.Frame(root)
        board.frame.pack(side=tk.LEFT, fill=tk.X)

        # board.arduino = SerialCommunication(port='COM3', baudrate=9600)

    
        board.StatusLabel = tk.Label(board.frame, text="Status:")
        board.StatusLabel.grid(row=0,column=0, sticky="w")

        board.ledConnected = tk.Canvas(board.frame, width=30, height=30, bg='#ECECEC')
        board.ledConnectedStatus = board.ledConnected.create_oval(3, 3, 15, 15, fill='red')
        board.ledConnected.grid(row=0, column=1, sticky="n")

        board.connectButton = ttk.Button(board.frame, text="Connect Port")#, command=board.toggleConnection)
        board.connectButton.grid(row=0, column=2, sticky="n")

        # Segunda columna - Prueba 1
        board.labelSamples = ttk.Label(board.frame, text="Number of Samples:")
        board.labelSamples.grid(row=1, column=0, pady=5,sticky="w")    
        
        board.entrySamples = ttk.Entry(board.frame)
        board.entrySamples.grid(row=1, column=1, pady=5,sticky="w")

        board.labelTime = ttk.Label(board.frame, text="Time:")
        board.labelTime.grid(row=2, column=0,pady=5, sticky="w")    
        
        board.entryTime = ttk.Entry(board.frame)
        board.entryTime.grid(row=2, column=1, pady=5,sticky="w")
        
        board.labelSeconds = ttk.Label(board.frame, text="s")
        board.labelSeconds.grid(row=2, column=2,pady=5, sticky="w") 

        board.labelFilename = ttk.Label(board.frame, text="CSV Filename:")
        board.labelFilename.grid(row=3, column=0, pady=5, sticky="w")    
        
        board.entryFilename = ttk.Entry(board.frame)
        board.entryFilename.grid(row=3, column=1, pady=5, sticky="w")

        board.SaveButton = ttk.Button(board.frame, text="Save")#, command=board.toggleConnection)
        board.SaveButton.grid(row=3, column=2, pady=5,sticky="n")

        board.labelSamplingTime = ttk.Label(board.frame, text="Sampling Time:")
        board.labelSamplingTime.grid(row=4, column=0, pady=5, sticky="w")    
        
        board.entrySamplingTime = ttk.Entry(board.frame)
        board.entrySamplingTime.grid(row=4, column=1, pady=5, sticky="w")
        
        board.labelSecondsSampling = ttk.Label(board.frame, text="s")
        board.labelSecondsSampling.grid(row=4, column=2,pady=5, sticky="w") 

        board.FirstTestutton = ttk.Button(board.frame, text="Test 1")#, command=board.toggleConnection)
        board.SaveButton.grid(row=5, column=1,pady=10, sticky="n")

        board.SecondTestButton = ttk.Button(board.frame, text="Test 2")#, command=board.toggleConnection)
        board.SaveButton.grid(row=5, column=2, pady=10,sticky="n")

        board.TestStarted = tk.Canvas(board.frame, width=35, height=35, bg='#ECECEC')
        board.TestStartedStatus = board.TestStarted.create_oval(15, 15, 30, 30, fill='red')
        board.TestStarted.grid(row=5, column=0, pady=5, sticky="n")

        board.testStatuslabel = ttk.Label(board.frame, text="Test ON")
        board.testStatuslabel.grid(row=6, column=0, sticky="n")  

       

windowLayer =tk.Tk() #Configuring window layer
ide=GUIDesign(windowLayer)
windowLayer.mainloop() 


