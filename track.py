from tkinter import*
import tkinter
import textx2
from tkinter import messagebox
def track1():
    w=tkinter.Tk()
    w.geometry('1360x1405')
    w.resizable(0,0)
    w.configure(background="#363534")
    def p():
        w.destroy()
        textx2.menu()
    def t():
        a="on the way"
        messagebox.showinfo("order status",a)
    f0=Frame(w,width=400,height=390,bg="#212120")
    f0.place(x=500,y=170)
    l10=Label(f0,text="Enter Your Order Id Here",font=("times new roman",15,"bold"),bg="#212120",fg="white")
    l10.place(x=90,y=90)
    l01=Label(f0,text="OREDR ID:",font=("times new roman",15,"bold"),bg="#212120",fg="white")
    l01.place(x=30,y=180)
    e11=Entry(f0,font=("times new roman",15,"bold"))
    e11.place(x=153,y=180)
    b11=tkinter.Button(f0,text='TRACK',bg="green",font=("times new roman",14,"bold"),border=0,relief=RAISED,command=t)
    b11.place(x=166,y=240)
    b12=tkinter.Button(f0,text='BACK',bg="green",font=("times new roman",14,"bold"),border=0,relief=RAISED,width=7,command=p)
    b12.place(x=166,y=300)
    w.mainloop()

