from tkinter import*
import tkinter
from tkinter import messagebox
import random
import textx2
def addinfo():
    w=tkinter.Tk()
    w.geometry('660x670')
    w.resizable(0,0)
    w.configure(background="#363534")
    def v():
        a=random.randint(10**10,10**11)
        messagebox.showinfo("order id",a)
    def x():
        w.destroy()
        textx2.menu()
    f1=Frame(w,width=400,height=590,bg="#212120")
    f1.place(x=130,y=27)
    l1=Label(f1,text="NAME:",font=("times new roman",15,"bold"),bg="#212120",fg="white")
    l1.place(x=30,y=100)
    e1=Entry(f1,font=("times new roman",15,"bold"))
    e1.place(x=153,y=100)
    l2=Label(f1,text="ADDRESS:",font=("times new roman",15,"bold"),bg="#212120",fg="white")
    l2.place(x=30,y=180)
    e2=Entry(f1,font=("times new roman",15,"bold"),show="*")
    e2.place(x=153,y=180)
    l3=Label(f1,text="PHONE NO:",font=("times new roman",15,"bold"),bg="#212120",fg="white")
    l3.place(x=30,y=260)
    e3=Entry(f1,font=("times new roman",15,"bold"),show="*")
    e3.place(x=153,y=260)
    l4=Label(f1,text="QUANTITY:",font=("times new roman",15,"bold"),bg="#212120",fg="white")
    l4.place(x=30,y=340)
    e4=Entry(f1,font=("times new roman",15,"bold"),show="*")
    e4.place(x=153,y=340)
    b1=tkinter.Button(f1,text='ORDER',bg="green",font=("times new roman",14,"bold"),border=0,relief=RAISED,command=v)
    b1.place(x=166,y=420)
    b2=tkinter.Button(f1,text='BACK',bg="green",font=("times new roman",14,"bold"),border=0,relief=RAISED,command=x)
    b2.place(x=175,y=480)

    w.mainloop()

