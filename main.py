
import os
import tkinter as tk
from tkinter import *


def traffic():
    new.destroy()
    os.system('python gui.py')

def driver():
    new.destroy()
    os.system('python Drowsiness_Detection.py')

def weather():
    new.destroy()
    os.system('python weather.py')

global new
new=tk.Tk()
new.geometry('1080x700')
new.title('ZEKA')
new.configure(background='#CDCDCD')
label=Label(new,background='#CDCDCD', font=('arial',15,'bold'))
sign_image = Label(new)
dr=Button(new,text="Driver Drowziness",padx=10,pady=5)
dr.pack(side=LEFT,pady=10,padx=5)
tf=Button(new,text="Traffic Sign Classifier",command=traffic,padx=10,pady=5)
tf.pack(side=RIGHT,pady=30,padx=5)
we=Button(new,text="Weather",padx=10,pady=5)
we.pack(side=LEFT,pady=10,padx=5)
mq=Button(new,text="MQTT Protocol",padx=10,pady=5)
mq.pack(side=RIGHT,pady=30,padx=5)
heading = Label(new, text="Please Choose One of the Options",pady=20, font=('arial',20,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack(side=TOP,pady=20)
new.mainloop()
