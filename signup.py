import tkinter
from tkinter import *
from database import *


def signing():
    def callit():
        regdat(e1.get(),e2.get(),e3.get(),e4.get(),e7.get())

        
    w=tkinter.Tk()
    w.geometry('1360x1405')
    w.resizable(0,0)
    w.configure(background="#ffe39f")

    f1=Frame(w,width=420,height=500,bg="#EE7621",border=0)
    f1.place(x=790,y=105)

    l1=Label(f1,text="FIRSTNAME:",font=("times new roman",15,"bold"),bg="#EE7621",fg="blue")
    l1.place(x=20,y=40)
    e1=Entry(f1,font=("times new roman",15,"bold"))
    e1.place(x=153,y=40)

    l2=Label(f1,text="LASTNAME:",font=("times new roman",15,"bold"),bg="#EE7621",fg="blue")
    l2.place(x=20,y=80)
    e2=Entry(f1,font=("times new roman",15,"bold"))
    e2.place(x=153,y=80)

    l3=Label(f1,text="USERNAME:",font=("times new roman",15,"bold"),bg="#EE7621",fg="blue")
    l3.place(x=20,y=120)
    e3=Entry(f1,font=("times new roman",15,"bold"))
    e3.place(x=153,y=120)

    l4=Label(f1,text="MOBILE NO:",font=("times new roman",15,"bold"),bg="#EE7621",fg="blue")
    l4.place(x=20,y=160)
    e4=Entry(f1,font=("times new roman",15,"bold"))
    e4.place(x=153,y=160)

    l4=Label(f1,text="DATE OF BIRTH:",font=("times new roman",15,"bold"),bg="#EE7621",fg="blue")
    l4.place(x=120,y=205)
    tkvar = StringVar(f1)
    choices = { '01','02','03'}
    tkvar.set('01')
    popupMenu = OptionMenu(f1, tkvar, *choices)
    l5=Label(f1,text="DAY:",font=("times new roman",15,"bold"),bg="#EE7621",fg="blue")
    l5.place(x=60,y=240)
    popupMenu.place(x=60,y=270)

    tkvar1 = StringVar(f1)
    choices = { '01','02','03'}
    tkvar1.set('01')
    popupMenu = OptionMenu(f1, tkvar1, *choices)
    l6=Label(f1,text="MONTH:",font=("times new roman",15,"bold"),bg="#EE7621",fg="blue")
    l6.place(x=160,y=240)
    popupMenu.place(x=160,y=270)

    tkvar2 = StringVar(f1)
    choices = { '1999','2000','2001'}
    tkvar2.set('1999')
    popupMenu = OptionMenu(f1, tkvar2, *choices)
    l6=Label(f1,text="YEAR:",font=("times new roman",15,"bold"),bg="#EE7621",fg="blue")
    l6.place(x=280,y=240)
    popupMenu.place(x=280,y=270)
    l7=Label(f1,text="PASSWORD:",font=("times new roman",15,"bold"),bg="#EE7621",fg="blue")
    l7.place(x=20,y=330)
    e7=Entry(f1,font=("times new roman",15,"bold",),show="*")
    e7.place(x=153,y=330)

    var = IntVar()
    b2=Radiobutton(f1,text='MALE', variable = var, value = 1,bg="#EE7621",fg="blue",font=("times new roman",15,"bold"))
    b2.place(x=60,y=380)
    b3=Radiobutton(f1,text='FEMALE', variable = var, value = 2,bg="#EE7621",fg="blue",font=("times new roman",15,"bold"))
    b3.place(x=240,y=380)
     
    b1=Button(f1,text='SIGN UP',bg="green",font=("times new roman",14,"bold"),border=0, command=callit)
    b1.place(x=155,y=425)
    img=PhotoImage(file="20.png")
    l4=tkinter.Label(w,image=img,border=0,relief=FLAT)
    l4.place(x=90,y=69)

    w.mainloop()
