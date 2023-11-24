from tkinter import *

#home/giselle/Documents/UDEM/Ot23/python-GUI/src

#Configuring window layer
window_layer = Tk()
window_layer.title("ARDUINO - Python GUI")
window_layer.resizable(1,1)
# window_layer.iconbitmap(r"home/giselle/Documents/UDEM/Ot23/python-GUI/src/arduino_22429.ico")

#Configuring frame to setup components
frame=Frame()
frame.pack()
frame.config(width="1500", height="900")
frame.config(bd=10)
frame.config(relief="sunken")

#button cursor config
connect=Button(frame,text="Connect")
connect.place(x=180,y=200)
# xxx.config(cursor="hand2")

#Intro
# cuadroTexto=Entry(frame)
# cuadroTexto.place(x=100,y=200)

#Setting labels
Label(frame, text= "COM PORT").place(x=100,y=200)





window_layer.mainloop()
 