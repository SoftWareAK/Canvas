import tkinter as tk
from tkinter import *

#arc yay demek


window=tk.Tk()
window.geometry("500x500")




c=Canvas(bg="pink",width=300,height=300)



coord=0,0,200,200
arc=c.create_arc(coord,start=0,extent=180,fill="blue")







c.place(x=10,y=10)









window.mainloop()