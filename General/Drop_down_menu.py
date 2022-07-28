from tkinter import *
from PIL import Image,ImageTk

#define window
app=Tk()
app.title("Soma Senpai")
app.iconbitmap('F:\Coding\Image files\Demon_ico.ico')
app.geometry("200x200")


#define variables
clicked=StringVar()


#functions
def show():
    mylab = Label(app, text=clicked.get()).pack()

#dropdown
opts = [ "Soma","Bunny","Somya","Varun"]
clicked.set(opts[0])
drop = OptionMenu(app, clicked, *opts).pack()


#define buttons
mybutt=Button(app, text="Show Character",command=show).pack()


app.mainloop()