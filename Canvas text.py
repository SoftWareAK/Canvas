import tkinter as tk
from tkinter import *




window=tk.Tk()
window.geometry("500x500")
c =Canvas(bg="white",width=400,height=400)

texr=c.create_text(150,100,text="BU BİR CANVAS YAZISIDIR",font="Ariel 16 bold")

c.place(x=10,y=10)
window.mainloop()