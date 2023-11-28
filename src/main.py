
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

timer = 0
# sampleTime=1

class GUIDesign:
    
    def __init__(board, root):
        board.windowLayer = root
               
        # se crea una instancia de la clase ArduinoComunication
        board.windowLayer.title("ARDUINO - Python GUI")
        board.windowLayer.resizable(1,1)
        
        board.plots= False

        #Configuring frame to setup components
        # Frame para controles y botones
        board.frame = ttk.Frame(root)
        board.frame.pack(side=tk.LEFT, fill=tk.X)
    
        board.StatusLabel = tk.Label(board.frame, text="Status:")
        board.StatusLabel.grid(row=0,column=0, sticky="w")

        board.ledConnected = tk.Canvas(board.frame, width=30, height=30, bg='#ECECEC')
        board.ledConnectedStatus = board.ledConnected.create_oval(3, 3, 15, 15, fill='red')
        board.ledConnected.grid(row=0, column=1, sticky="n")

        board.connectButton = ttk.Button(board.frame, text="Connect Port",command=board.ConnectToArduino)#, command=board.toggleConnection)
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
        board.entryFilename.grid(row=3, column=1,  sticky="w")

        board.SaveButton = ttk.Button(board.frame, text="Save")#, command=board.toggleConnection)
        board.SaveButton.grid(row=2, column=2, padx=20,sticky="n")

        board.labelSamplingTime = ttk.Label(board.frame, text="Sampling Time:")
        board.labelSamplingTime.grid(row=4, column=0, pady=5, sticky="w")    
        
        board.entrySamplingTime = ttk.Entry(board.frame)
        board.entrySamplingTime.insert(0,"1")
        board.entrySamplingTime.grid(row=4, column=1, pady=5, sticky="w")
        
        board.labelSecondsSampling = ttk.Label(board.frame, text="s")
        board.labelSecondsSampling.grid(row=4, column=2,pady=5, sticky="w") 

        board.FirstTestButton = ttk.Button(board.frame, text="Test 1", command=board.calculateFirstTest)#, command=board.toggleConnection)
        board.FirstTestButton.grid(row=5, column=1,pady=10, sticky="n")

        board.SecondTestButton = ttk.Button(board.frame, text="Test 2")#, command=board.toggleConnection)
        board.SecondTestButton.grid(row=5, column=2, pady=10,sticky="n")

        board.TestStarted = tk.Canvas(board.frame, width=35, height=35, bg='#ECECEC')
        board.TestStartedStatus = board.TestStarted.create_oval(15, 15, 30, 30, fill='red')
        board.TestStarted.grid(row=5, column=0, pady=5, sticky="n")

        board.testStatuslabel = ttk.Label(board.frame, text="Test OFF")
        board.testStatuslabel.grid(row=6, column=0, sticky="n")  

        # Configuración de Matplotlib para gráficos en tiempo real
        board.figure, board.ax = plt.subplots()
        board.ax.set_xlabel("Number of Samples", fontsize=15)   # Etiqueta para el eje X
        board.ax.set_ylabel("Temperature", fontsize=15)  # Etiqueta para el eje Y
        board.ax.set_title("Temperature vs Number of Samples", fontsize=20)
        board.line, = board.ax.plot([], [])
        board.canvas = FigureCanvasTkAgg(board.figure, master=root)
        board.canvas_widget = board.canvas.get_tk_widget()
        board.canvas_widget.config(width=1000, height=650)
        board.canvas_widget.pack(expand=False, anchor=tk.CENTER)

    def ConnectToArduino(board):
        # board.arduino = SerialCommunication('COM12', 9600)

        if not board.arduino.connected:
            board.arduino = SerialCommunication('COM12', 9600)

            if board.arduino.connected:
                board.ledConnected.itemconfig(board.ledConnectedStatus, fill='green')
            else:
                board.connected=False
                board.ledConnected.itemconfig(board.ledConnectedStatus, fill='red')

    def calculateFirstTest(board):
        """
        Se realiza la prueba 1, el usuario ingresa el numero de muestras
        """
        if not board.arduino.connected:
            try:
                numberSamples = int(board.entrySamples.get())
                sampleTime = float(board.entrySamplingTime.get())
            except ValueError:
                print("Please enter valid numbers for number of samples and sample time")
                return




        # Se convierte el tiempo de muestreo a milisegundos y se envia al arduino
        board.arduino.setSampleTime(int(sampleTime * 1000))
        # # board.status_test.itemconfig(board.status_test_circle, fill='green')

        # board.arduino.getData()
        # readThread = threading.Thread(target=board.arduino.readData, args=(sampleTime, numberSamples))
        # plotThread = threading.Thread(target=board.plotData, args=(numberSamples,))
        # readThread.start()
        # plotThread.start()
        # board.plots = True
        # board.plotData(numberSamples)

    # def plotData(board, numberSamples):
    #     """
    #     Metodo para graficar, se actualiza el vector x & y
    #     """
    #     global timer 
    #     if not board.plots:
    #         return
    #     if len(board.arduino.data) <= numberSamples:
    #         sampleTime = float(board.entrySamplingTime.get())
    #         timer = timer + sampleTime
    #         board.line.set_xdata(range(len(board.arduino.data)))
    #         board.line.set_ydata(board.arduino.data)

    #         board.ax.relim()
    #         board.ax.autoscale_view()

    #         board.canvas.draw()
    #         board.root.after(int(float(board.entrySamplingTime.get()) * 1000), lambda: board.plotData(numberSamples))
    #     else:
    #         board.plots = False
    #         board.TestStarted.itemconfig(board.TestStartedStatus, fill='red')
        
    #     board.arduino.samplesCount = len(board.arduino.data)


       

windowLayer =tk.Tk() #Configuring window layer
ide=GUIDesign(windowLayer)
windowLayer.mainloop() 


