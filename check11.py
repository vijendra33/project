import sqlite3
from tkinter import*
root=Tk()
username=StringVar()
password=StringVar()
e1=Entry(root,font=("times new roman",15,"bold"),textvariable=username)
e1.pack()
e2=Entry(root,font=("times new roman",15,"bold"),textvariable=password).pack()
username1=username.get()
password1=password.get()
conn=sqlite3.connect("base2.db")
c=conn.cursor()
c.execute('create table IF NOT EXISTS base3(username TEXT NOT NULL,password TEXT NOT NULL);')
c.execute("insert into base3(username,password) values(?,?)",(username1,password1))
conn.commit()
c.close()
conn.close()
root.mainloop()
