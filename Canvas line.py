import tkinter as tk
from tkinter import *




window=tk.Tk()

c=Canvas(bg="white",width=300,height=300)

line=c.create_line(0,0,150,150,fill="red",width=3)
line2=c.create_line(55,50,100,250,fill="blue",width=13)
line3=c.create_line(40,40,15,15,fill="green",width=5)


c.place(x=10,y=10)






window.mainloop()