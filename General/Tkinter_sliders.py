from tkinter import *
from PIL import Image,ImageTk

#intro
app = Tk()
app.title("Soma Senpai")
app.iconbitmap('F:\Coding\Image files\Demon_ico.ico')
app.geometry("200x200")

#functions
def update():
    #slider1 = Label(app,text=hori.get()).pack()
    app.geometry(str(hori.get()) + "x" + str(vert.get()))

#widgets
vert = Scale(app, from_=200,to=1000)
vert.pack()
hori = Scale(app, from_=200,to=1000,orient=HORIZONTAL)
hori.pack()

butt=Button(app,text="Update",command=update).pack()

mainloop()