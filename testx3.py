from tkinter import*
import tkinter
import textx2
import track
import cancle
import testx4

def testx3():    
    w=tkinter.Tk()
    w.geometry('1360x1405')
    w.resizable(0,0)
    w.configure(background="white")
        
    def m():
        w.destroy()
        track.track1()
    def z():
        w.destroy()
        textx2.menu()
    def o():
        w.destroy()
        cancle.cancle1()
    def u():
        w.destroy()
        testx4.addinfo()

    f1=Frame(w,width=1360,height=1310,bg="#363534")
    f1.place(x=0,y=-40)
    l1=Label(f1,text="OUR SPECIAL",font=("times new roman",26,"bold"),bg="#363534",fg="white")
    l1.place(x=570,y=453)
    f2=Frame(f1,width=1320,height=346,bg="#212120")
    f2.place(x=20,y=106)
    f6=Frame(f1,width=250,height=250,bg="#212120")
    f6.place(x=20,y=500)
    f7=Frame(f1,width=250,height=250,bg="#212120")
    f7.place(x=300,y=500)
    f8=Frame(f1,width=250,height=250,bg="#212120")
    f8.place(x=580,y=500)
    f9=Frame(f1,width=250,height=250,bg="#212120")
    f9.place(x=860,y=500)
    ##########################################################################################################################33
    img=PhotoImage(file="p14.gif")
    l2=Label(f2,image=img,width=650,height=320)
    l2.place(x=18,y=10)
    img0=PhotoImage(file="p15.gif")
    l2=Label(f2,image=img0,width=620,height=320)
    l2.place(x=680,y=10)

    #####################################################################################################################################
    img4=PhotoImage(file="p5.gif")
    l10=Label(f6,image=img4,width=195,height=120)
    l10.place(x=26,y=10)
    l11=Label(f6,text="Mexican Green Wave",font=("time0s new roman",16,"bold"),bg="#212120",fg="white")
    l11.place(x=23,y=135)
    tkvar4 = StringVar(f6)
    choices = { 'Regular: Rs.210/-','Medium: Rs.310/-','Large: Rs.490/-'}
    tkvar4.set('Regular: Rs.210/-')
    popupMenu = OptionMenu(f6, tkvar4, *choices)
    popupMenu.place(x=60,y=170)
    b5=Button(f6,text='Order Now',bg="red",font=("times new roman",14,"bold"),fg="white",command=u)
    b5.place(x=70,y=205)
    ########################################################################################################################################
    img5=PhotoImage(file="p6.gif")
    l12=Label(f7,image=img5,width=195,height=120)
    l12.place(x=26,y=10)
    l13=Label(f7,text="Cheese Margherita",font=("times new roman",16,"bold"),bg="#212120",fg="white")
    l13.place(x=42,y=135)
    tkvar5 = StringVar(f7)
    choices = { 'Regular: Rs.201/-','Medium: Rs.305/-','Large: Rs.460/-'}
    tkvar5.set('Regular: Rs.201/-')
    popupMenu = OptionMenu(f7, tkvar5, *choices)
    popupMenu.place(x=60,y=170)
    b6=Button(f7,text='Order Now',bg="red",font=("times new roman",14,"bold"),fg="white",command=u)
    b6.place(x=70,y=205)
    #######################################################################################################################################
    img6=PhotoImage(file="p7.gif")
    l14=Label(f8,image=img6,width=195,height=120)
    l14.place(x=26,y=10)
    l15=Label(f8,text="Chicken Sausage",font=("times new roman",16,"bold"),bg="#212120",fg="white")
    l15.place(x=49,y=135)
    tkvar6 = StringVar(f8)
    choices = { 'Regular: Rs.299/-','Medium: Rs.399/-','Large: Rs.499/-'}
    tkvar6.set('Regular: Rs.299/-')
    popupMenu = OptionMenu(f8, tkvar6, *choices)
    popupMenu.place(x=60,y=170)
    b7=Button(f8,text='Order Now',bg="red",font=("times new roman",14,"bold"),fg="white",command=u)
    b7.place(x=70,y=205)
    ##########################################################################################################################################
    img7=PhotoImage(file="p8.gif")
    l16=Label(f9,image=img7,width=195,height=120)
    l16.place(x=26,y=10)
    l17=Label(f9,text="Chicken Dominator",font=("times new roman",16,"bold"),bg="#212120",fg="white")
    l17.place(x=42,y=135)
    tkvar7 = StringVar(f9)
    choices = { 'Regular: Rs.249/-','Medium: Rs.349/-','Large: Rs.449/-'}
    tkvar7.set('Regular: Rs.249/-')
    popupMenu = OptionMenu(f9, tkvar7, *choices)
    popupMenu.place(x=60,y=170)
    b8=Button(f9,text='Order Now',bg="red",font=("times new roman",14,"bold"),fg="white",command=u)
    b8.place(x=70,y=205)
    ############################################################################################################################################
    f12=Frame(w,width=1360,height=65,bg="#212120")
    f12.place(x=0,y=0)
    b2=tkinter.Button(f12,text="HOME",relief=GROOVE,height=4,width=20,bg="#212120",fg="white")
    b2.place(x=0,y=0)


    b6=tkinter.Button(f12,text="LOGOUT",relief=GROOVE,height=4,width=20,bg="#212120",fg="white")
    b6.place(x=1208,y=0)
    b11=Button(w,justify = LEFT)
    img10=PhotoImage(file="p12.gif")
    b11.config(image=img10,width="200",height="150")
    b11.place(x=1130,y=500)
    b3=tkinter.Button(f12,text="MENU",relief=GROOVE,height=4,width=20,bg="#212120",fg="white",command=z)
    b3.place(x=140,y=0)
    w.mainloop()

