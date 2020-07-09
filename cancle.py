from tkinter import*
import tkinter
import textx2
from tkinter import messagebox
def cancle1():
    w=tkinter.Tk()
    w.geometry('1360x1405')
    w.resizable(0,0)
    w.configure(background="#363534")
    def i():
        w.destroy()
        textx2.menu()
    def y():
        a="order cancled successfully"
        messagebox.showinfo("order status",a)
    f1=Frame(w,width=400,height=390,bg="#212120")
    f1.place(x=500,y=170)
    l0=Label(f1,text="Enter Your Order Id Here",font=("times new roman",15,"bold"),bg="#212120",fg="white")
    l0.place(x=90,y=90)
    l1=Label(f1,text="OREDR ID:",font=("times new roman",15,"bold"),bg="#212120",fg="white")
    l1.place(x=30,y=180)
    e1=Entry(f1,font=("times new roman",15,"bold"))
    e1.place(x=153,y=180)
    b1=tkinter.Button(f1,text='CANCEL',bg="green",font=("times new roman",14,"bold"),border=0,relief=RAISED,command=y)
    b1.place(x=166,y=240)
    b1=tkinter.Button(f1,text='BACK',bg="green",font=("times new roman",14,"bold"),border=0,relief=RAISED,width=8,command=i)
    b1.place(x=166,y=300)

    w.mainloop()

