import tkinter as tk
from tkinter import *




window=tk.Tk()
window.geometry("500x500")
c =Canvas(bg="white",width=400,height=400)

oval=c.create_oval(10,50,100,100,fill="red")


c.place(x=10,y=10)








window.mainloop()