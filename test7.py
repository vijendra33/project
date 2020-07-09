from tkinter import*
import tkinter
w=tkinter.Tk()
w.geometry('1360x1405')
w.resizable(0,0)
w.configure(background="#ffe39f")
f1=Frame(w,width=1360,height=50,bg="#ff3333")
f1.place(x=0,y=0)
b2=tkinter.Button(f1,text="MENU",relief=GROOVE,height=3,width=20,bg="#ff3333",fg="blue")
b2.place(x=0,y=0)
b3=tkinter.Button(f1,text="TRACK ORDER",relief=GROOVE,height=3,width=20,bg="#ff3333",fg="blue")
b3.place(x=140,y=0)

w.mainloop()
