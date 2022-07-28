from tkinter import *
from PIL import ImageTk,Image

app = Tk()
app.title("Soma Senpai")
app.iconbitmap('F:\Coding\Image files\Demon_ico.ico')

#functions
def open():
    global my_img
    top = Toplevel()
    top.title("Cutie Soma Senpai")
    top.iconbitmap('F:\Coding\Image files\Demon_ico.ico')
    my_img = ImageTk.PhotoImage(Image.open("F:\Coding\Image files\esties.JPG"))
    label=Label(top, image=my_img).pack()
    butt2=Button(top,text="Close senpai",command=top.destroy).pack()





#buttons
butt=Button(app,text="Wanna see a cute senpai?",command=open).pack()





mainloop()