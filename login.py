from tkinter import *
import tkinter
from testx3 import *
from signup import *
import sqlite3
import vendorlogin



def verify():
    c = sqlite3.connect("pizza.db")
    usern = c.execute("select username from signup")
    pswd = c.execute("select password from signup")
    
    for i,j in zip(usern,pswd):
        print(i[0],j[0])
        if i[0] == euser.get() and j[0] == epwd.get():
            testx3()

def n():
    w.destroy()
    vendorlogin.vendor1()
def m():
    w.destroy()
    signing()
    
w=tkinter.Tk()
w.geometry('1360x1405')
w.resizable(0,0)
w.configure(background="#ffe39f")
f1=Frame(w,width=400,height=400,bg="#EE7621")
f1.place(x=780,y=150)
l1=Label(f1,text="USERNAME:",font=("times new roman",15,"bold"),bg="#EE7621",fg="blue")
l1.place(x=30,y=100)
euser=Entry(f1,font=("times new roman",15,"bold"))
euser.place(x=153,y=100)
l2=Label(f1,text="PASSWORD:",font=("times new roman",15,"bold"),bg="#EE7621",fg="blue")
l2.place(x=30,y=180)
epwd=Entry(f1,font=("times new roman",15,"bold"),show="*")
epwd.place(x=153,y=180)
b1=tkinter.Button(f1,text='LOGIN',bg="green",font=("times new roman",14,"bold"),border=0,relief=RAISED,command=verify)
b1.place(x=166,y=250)
l3=Label(f1,text="Don't have an account? sign'up here",font=("times new roman",10),bg="#EE7621",fg="black")
l3.place(x=72,y=305)
b2=tkinter.Button(f1,text='sign up',bg="green",font=("times new roman",10),border=0,relief=RAISED,command=m)
b2.place(x=275,y=305)
img=PhotoImage(file="20.png")
l4=tkinter.Label(w,image=img,border=0,relief=FLAT)
l4.place(x=110,y=60)
b2=tkinter.Button(f1,text='vendor',bg="green",font=("times new roman",10),border=0,relief=RAISED, command=n)
b2.place(x=182,y=355)
w.mainloop()
