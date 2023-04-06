from tkinter import *
import sqlite3
from tkinter import messagebox
from PIL import ImageTk,Image
from datetime import date
from datetime import timedelta
from datetime import datetime
from tkinter import ttk



def event1():

    u=str(t.get())
    v=str(t1.get())

















base10= Tk()
base10.state("zoomed")
base10.title("Student Manegement System")



load = Image.open("C:\\Users\\91901\\Downloads\\88.jpg")
ren= ImageTk.PhotoImage(load)
img = Label(base10,image=ren)
img.place(x=0,y=0)




title=Label(base10,text="College Manegement System",bd=10,font=("times new roman", 45,"bold"),bg="#72482F",fg="White")
title.place(x=2,y=5)


Man_fr1=Frame(base10,bd=4,relief=RIDGE,bg="#000000")
Man_fr1.place(x=500,y=450,width=500,height=300)

l = Label(Man_fr1,text=" Login ",font=("times new roman", 40,"bold"),bg="#000000",fg="White")
l.pack()


l1 = Label(Man_fr1,text="Email:",font=("times new roman", 20,"bold"),bg="#000000",fg="White")
l1.place(x=10,y=70)

t = Entry(Man_fr1,font=("times new roman", 15,"bold"),bg="#000000",fg="white",width=30)
t.place(x=165,y=70,height=40)


l2 = Label(Man_fr1,text="Passward:",font=("times new roman", 20,"bold"),bg="#000000",fg="White")
l2.place(x=10,y=140)

t1 = Entry(Man_fr1,font=("times new roman", 15,"bold"),bg="#000000",fg="white",width=30)
t1.place(x=165,y=140,height=40)

b = Button(Man_fr1,text="Sign in",font=("times new roman", 15,"bold"),bg="Sky blue",fg="black",command=event1)
b.place(x=250,y=230)

b1 = Button(Man_fr1,text="Reset",font=("times new roman", 15,"bold"),bg="Sky blue",fg="black")
b1.place(x=160,y=230)


base10.mainloop()
