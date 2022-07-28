from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

app = Tk()
app.title("Soma Senpai")
app.iconbitmap('F:\Coding\Image files\Demon_ico.ico')

#define
def open():
    global image1
    app.filename=filedialog.askopenfilename(initialdir="F:\Coding\Image files",title="Chose an file :",filetype=(("JPG files","*.jpg"),("PNG files","*.png"),("All files","*.*")))
    lab=Label(app,text=app.filename)
    image1 = ImageTk.PhotoImage(Image.open(app.filename))
    imglab= Label(app,image=image1).pack()

butt=Button(app,text="Select file",command=open).pack()


#display

mainloop()