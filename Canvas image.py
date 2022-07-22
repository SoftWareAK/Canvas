import tkinter as tk
from tkinter import *




window=tk.Tk()
window.geometry("650x650")
c =Canvas(bg="white",width=520,height=520)

file=PhotoImage(file="bahçe.gif")

image=c.create_image(20,20,anchor=NW,image=file) # anchor=SW   sourth west felan


c.place(x=10,y=10)
window.mainloop()