from tkinter import *
from PIL import ImageTk,Image

app=Tk()
app.title("GDK Productions")
app.iconbitmap('F:\Coding\Image files\Demon_ico.ico')

#define
#r=IntVar()
#r.set("101")

toppings=[
    ("Mummy's Pasta","Mummy's Pasta"),
    ("Cheese Sandwhich","Cheese Sandwhich"),
    ("Mummy's Pizza","Mummy's Pizza"),
    ("Cake","Cake")
]
snacks=StringVar()

for text,mode in toppings:
    Radiobutton(app,text=text,value=mode,variable=snacks).pack(anchor=W)

#Functions
def clicked(value):
    label1 = Label(app,text=value)
    label1.pack()

#buttons
#Radiobutton(app,text="Option 1",variable=r,value=1,command = lambda:clicked(r.get())).pack()
#Radiobutton(app,text="Option 2",variable=r,value=2,command = lambda:clicked(r.get())).pack()
button1=Button(app,text="Click me biotch",command=lambda:clicked(snacks.get()))

#display
label1=Label(app,text=snacks.get())
label1.pack()
button1.pack()



app.mainloop()