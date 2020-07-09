from tkinter import*
import tkinter
w=tkinter.Tk()
w.geometry('1360x1405')
w.resizable(0,0)
w.configure(background="#363534")
f1=Frame(w,width=400,height=450,bg="#212120")
f1.place(x=480,y=130)
b1=tkinter.Button(f1,text='ORDERS',bg="green",font=("times new roman",24,"bold"),bd=0,width=15,relief=RAISED)
b1.place(x=55,y=70)
b2=tkinter.Button(f1,text='DELIVERED ORDER',bg="green",font=("times new roman",16,"bold"),border=0,width=24,height=2,relief=RAISED)
b2.place(x=55,y=150)
b3=tkinter.Button(f1,text='CANCELED ORDER',bg="green",font=("times new roman",16,"bold"),border=0,width=24,height=2,relief=RAISED)
b3.place(x=55,y=230)
b4=tkinter.Button(f1,text='LOGOUT',bg="green",font=("times new roman",16,"bold"),border=0,width=24,height=2,relief=RAISED)
b4.place(x=55,y=310)
w.mainloop()

