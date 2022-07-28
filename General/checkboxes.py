from tkinter import *
from PIL import Image,ImageTk

#define window
app=Tk()
app.title("Soma Senpai")
app.iconbitmap('F:\Coding\Image files\Demon_ico.ico')
app.geometry("200x200")

#functions
def show():
    mylab = Label(app,text=var.get()).pack()

#variable
var = StringVar()

#buttons and Lebels
c=Checkbutton(app,text="Do you like your senpai",variable=var,onvalue="Senpai Love",offvalue="Senpai tsundere")
c.deselect()
c.pack()

butt1=Button(app,text="Show Love",command=show).pack()

#display



app.mainloop()