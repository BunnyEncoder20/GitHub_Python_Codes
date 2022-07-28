from tkinter import *
from typing import Counter



def click(number):
    
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def add():
    global f_num
    global func
    func="add"
    first=e.get()
    f_num=int(first)
    e.delete(0,END)

def subs():
    global f_num
    global func
    func="subs"
    first=e.get()
    f_num=int(first)
    e.delete(0,END)


def multi():
    global f_num
    global func
    func="multi"
    first=e.get()
    f_num=int(first)
    e.delete(0,END)


def divi():
    global f_num
    global func
    func="divi"
    first=e.get()
    f_num=int(first)
    e.delete(0,END)

def equal():
    second=e.get()
    e.delete(0,END)

    if func=="add":
        e.insert(0, f_num + int(second))
    elif func=="subs":
        e.insert(0, f_num - int(second))
    elif func=="multi":
        e.insert(0, f_num * int(second))
    elif func=="divi":
        e.insert(0, f_num / int(second))

def clear():
    e.delete(0,END)


app = Tk()
app.title("Soma Senpai Says")
e=Entry(app,borderwidth=10,bg="black",fg="white",)
e.grid(row=0,column=0,columnspan=4,ipadx=70)
e.insert(0,"0")


button_1=Button(app,padx=40,pady=20,text="1",command=lambda:click(1))
button_2=Button(app,padx=40,pady=20,text="2",command=lambda:click(2))
button_3=Button(app,padx=40,pady=20,text="3",command=lambda:click(3))
button_4=Button(app,padx=40,pady=20,text="4",command=lambda:click(4))
button_5=Button(app,padx=40,pady=20,text="5",command=lambda:click(5))
button_6=Button(app,padx=40,pady=20,text="6",command=lambda:click(6))
button_7=Button(app,padx=40,pady=20,text="7",command=lambda:click(7))
button_8=Button(app,padx=40,pady=20,text="8",command=lambda:click(8))
button_9=Button(app,padx=40,pady=20,text="9",command=lambda:click(9))
button_0=Button(app,padx=40,pady=20,text="0",command=lambda:click(0))
button_add=Button(app,padx=40,pady=55,text="+",command=add)
button_subs=Button(app,padx=40,pady=20,text="-",command=subs)
button_multi=Button(app,padx=40,pady=20,text="x",command=multi)
button_divi=Button(app,padx=40,pady=20,text="/",command=divi)
button_equal=Button(app,padx=40,pady=20,text="=",command=equal)
button_clear=Button(app,padx=40,pady=40,text="AC",command=clear)
button_dot=Button(app,padx=40,pady=20,text=".",command=lambda:click())


button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_0.grid(row=4,column=0)
button_add.grid(row=4,column=2,rowspan=2)
button_equal.grid(row=4,column=1)
button_clear.grid(row=5,column=1)
button_dot.grid(row=5,column=0)
button_subs.grid(row=6,column=0)
button_multi.grid(row=6,column=1)
button_divi.grid(row=6,column=2)


app.mainloop() 




