from sqlite3.dbapi2 import Row
from tkinter import *
from PIL import Image,ImageTk
import sqlite3

#define window
app=Tk()
app.title("Soma")
app.iconbitmap('F:\Coding\Image files\Demon_ico.ico')
app.geometry("730x600")

#creating database
conn= sqlite3.connect('addressbook.db') #this is the connect handle to connect database to the python file just like a fil handle name
c = conn.cursor()   #cursors vaiable to fetch data changes

#making tables in the db
'''
c.execute("""CREATE TABLE addr(
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
)
""")
'''
# Text boxes
fname = Entry(app, width=30)
fname.grid(row=0,column=1,padx=20)
lname = Entry(app, width=30)
lname.grid(row=0,column=3,padx=20)
address = Entry(app, width=30)
address.grid(row=1,column=1,padx=20)
city = Entry(app, width=30)
city.grid(row=2,column=1,padx=20)
state = Entry(app, width=30)
state.grid(row=2,column=3,padx=20)
zippy = Entry(app, width=30)
zippy.grid(row=3,column=1,padx=20)
zippy = Entry(app, width=30)
zippy.grid(row=3,column=1,padx=20)
deleter = Entry(app, width=10)
deleter.grid(row=6,column=2,padx=20,pady=10)


#creating text box's labels:
fnamelab = Label(app,text="First name")
fnamelab.grid(row=0,column=0,padx=20,pady=(20,10))

lnamelab = Label(app,text="Last name")
lnamelab.grid(row=0,column=2,padx=20,pady=(20,10))

addresslab = Label(app,text="Address")
addresslab.grid(row=1,column=0,padx=20,pady=(10,10))

citylab = Label(app,text="City")
citylab.grid(row=2,column=0,padx=20,pady=(10,10))

statelab = Label(app,text="State")
statelab.grid(row=2,column=2,padx=20,pady=(10,10))

zippylab = Label(app,text="Zipcode")
zippylab.grid(row=3,column=0,padx=20,pady=(10,10))

deletelab = Label(app,text="Enter id to be deleted :")
deletelab.grid(row=6,column=1,padx=20,pady=(10,10))

#submissions
def submit():
    #gonna do it gain in the function
    conn= sqlite3.connect('addressbook.db')
    c=conn.cursor()

    #inserting into the table :
    c.execute("insert into addr values (:fname, :lname, :address, :city, :state, :zippy)",
        {
            'fname': fname.get(),
            'lname': lname.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zippy': zippy.get()
        }
    )
    conn.commit()
    conn.close()

    #clear the text boxes for new entries:
    fname.delete(0,END)
    lname.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zippy.delete(0,END)


def display():
    conn = sqlite3.connect('addressbook.db')
    c=conn.cursor()
    c.execute("select * , oid from addr")
    records = c.fetchall()
    print(records)

    print_records=" "
    for r in records:
        print_records+= str(r[6])+ " " + str(r[0]) + " " + str(r[1])+ "\n"


    plabel = Label(app, text=print_records)
    plabel.grid(row=7,column=0,columnspan=3)
    conn.commit()
    conn.close()

def delete():
    conn=sqlite3.connect("addressbook.db")
    c=conn.cursor()

    c.execute("DELETE from addr where oid=" + "" + deleter.get())
    deleter.delete(0,END)

    conn.commit()
    conn.close()


but1 = Button(app, text="Submit",command=submit)
but1.grid(row=4,column=3,columnspan=2,padx=10,pady=10,ipadx=80)
qbut = Button(app, text="Display", command=display)
qbut.grid(row=5,column=3,columnspan=2,padx=10,pady=10,ipadx=80)
dbut = Button(app, text="Delete Records",command=delete)
dbut.grid(row=6,column=3,columnspan=2,padx=10,pady=10,ipadx=56)

conn.commit()   #to execute all the sql queries to make changes in the data base

conn.close()    #closing the connection to the database





app.mainloop()