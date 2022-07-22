import tkinter as tk
from tkinter import *
#Rectangle = dörtgen demek p
# Polygon =çogen demek



window=tk.Tk()
window.geometry("500x500")
c =Canvas(bg="white",width=400,height=400)

rectangle= c.create_rectangle(10,10,100,180,fill="blue") # Dörtgenler için

point =[200,200,250,290,350,350]
polygon=c.create_polygon(point,outline="red",fill="yellow")


c.place(x=10,y=10)

window.mainloop()