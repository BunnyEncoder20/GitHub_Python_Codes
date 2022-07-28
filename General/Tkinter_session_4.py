from tkinter import *
from PIL import ImageTk,Image
from  tkinter import messagebox

app = Tk()
app.title("Soma Senpai")
app.iconbitmap('F:\Coding\Image files\Demon_ico.ico')

#define
#different kinda message boxes : showinfo,showwarning,showerror,askquestion,askokcancel,askyesno
def popup():
    reponce=messagebox.askquestion("Fill in the blank :","___ , I am gay")
    #Label(app,text=reponce).pack()
    if reponce == "yes":
        Label(app,text="Yes , you're gay!").pack()
    else:
        Label(app,text="No , you're gay!").pack()



#Button
Button(app, text="Pop up",command=popup).pack()


#display


app.mainloop()