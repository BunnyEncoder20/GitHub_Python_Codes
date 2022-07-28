from tkinter import *
from PIL import ImageTk,Image

app=Tk()
app.title("GDK Productions")
app.iconbitmap('F:\Coding\Image files\Demon_ico.ico')

#define
img0=ImageTk.PhotoImage(Image.open('F:\Coding\img3.jpg'))
label0=Label(image=img0)
img1=ImageTk.PhotoImage(Image.open('F:\Coding\Kaneki.png'))
img2=ImageTk.PhotoImage(Image.open('F:\Coding\esties.jpg'))
img3=ImageTk.PhotoImage(Image.open('F:\Coding\ess.jpg'))
img4=ImageTk.PhotoImage(Image.open('F:\Coding\Imglabel1.jpg'))

#Defining buttons
bback=Button(app,text="<<",padx=90,pady=20,state=DISABLED,command=lambda:back)
bforward=Button(app,text=">>",padx=90,pady=20,command=lambda:forward(1))
exit=Button(app,text="Exit",padx=90,pady=20,command=app.quit)


image_list=[img0,img1,img2,img3,img4]; #image list!

#place on screen
label0.grid(row=0,column=0,columnspan=3)
bback.grid(row=1,column=0)
exit.grid(row=1,column=1)
bforward.grid(row=1,column=2)


#functions
def forward(img_num):
    global label0; global back ;  global forward

    label0.grid_forget()
    label0=Label(image=image_list[img_num])
    label0.grid(row=0,column=0,columnspan=3)
    bforward=Button(app,text=">>",padx=90,pady=20,command=lambda:forward(img_num+1))
    bforward.grid(row=1,column=2)
    bback=Button(app,text="<<",padx=90,pady=20,command=lambda:back(img_num-1))
    bback.grid(row=1,column=0)
    label0.grid(row=0,column=0,columnspan=3)

    if img_num==4:
        bforward=Button(app,text=">>",state=DISABLED,padx=90,pady=20)
        bforward.grid(row=1,column=2)


    count=Label(app,text="Image "+str(img_num+1)+" of "+str(len(image_list)),bd=4,relief = SUNKEN,anchor=W)
    count.grid(row=2,columnspan=3,column=0,sticky=W+E)

    return

def back(img_num):
    global label0; global back ;  global forward

    label0.grid_forget()
    label0=Label(image=image_list[img_num])
    label0.grid(row=0,column=0,columnspan=3)
    bforward=Button(app,text=">>",padx=90,pady=20,command=lambda:forward(img_num+1))
    bforward.grid(row=1,column=2)
    bback=Button(app,text="<<",padx=90,pady=20,command=lambda:back(img_num-1))
    bback.grid(row=1,column=0)
    label0.grid(row=0,column=0,columnspan=3)
    if img_num==0:
        bback=Button(app,text="<<",state=DISABLED,padx=90,pady=20)
        bback.grid(row=1,column=0)

    count=Label(app,text="Image "+str(img_num+1)+" of "+str(len(image_list)),bd=4,relief = SUNKEN,anchor=W)
    count.grid(row=2,columnspan=3,column=0,sticky=W+E)
    return




app.mainloop()