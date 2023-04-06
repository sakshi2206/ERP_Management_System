from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk

con = sqlite3.connect("Faculty_Management_Data_New.db")
base = Tk()
base.state("zoomed")
base.title("Faculty Manegement System")

def event1():
    a = str(t1.get())
    b = str(t2.get())
    c = str(t3.get())
    d = str(com.get())
    e = str(t5.get())
    f = str(t6.get())
    g = str(t7.get())
    h = str(t8.get())
    i = str(t9.get())


    con = sqlite3.connect("Faculty_Manegement_Data_New.db")
    q = "insert into faculty_Data values('" + a + "'," + b + ",'" + c + "','" + d + "',"+ e +"," + f +",'" + g+ "',"+ h +",'"+i+"')"
    con.execute(q)
    con.commit()
    con.close()
    messagebox.showinfo("Data", "Data Saved Sucessfully.....")

    event2()


def event2():
    t1.delete(0, END)
    t2.delete(0, END)
    t3.delete(0, END)
    com.delete(0, END)
    t5.delete(0, END)
    t6.delete(0, END)
    t7.delete(0, END)
    t8.delete(0, END)
    t9.delete(0, END)



def event3():
    a = str(t1.get())
    b = str(t2.get())
    c = str(t3.get())
    d = str(com.get())
    e = str(t5.get())
    f = str(t6.get())
    g = str(t7.get())
    h = str(t8.get())
    i = str(t9.get())


    con = sqlite3.connect("Faculty_Manegement_Data_New.db")
    q = "update faculty_Data set faculty_name='" + a + "',email_id='" + c + "',gender='" + d + "',contact_no="+e+",date_of_birth="+f+",department='"+g+"',joining_date="+h+",address='"+i+"' where faculty_id=" + b
    con.execute(q)
    con.commit()
    con.close()
    messagebox.showinfo("Data", "Updated Sucessfully.....")
    event2()

def event4():
          b = str(t2.get())
          con = sqlite3.connect("Faculty_Manegement_Data_New.db")
          q ="delete from faculty_Data where faculty_id="+b
          con.execute(q)
          con.commit()
          con.close()
          messagebox.showinfo("Data", "Data deleted Sucessfully.....")
          event2()



title=Label(base,text="Faculty Management System",bd=10,relief=GROOVE,font=("times new roman", 30,"bold"),bg="#4B778D",fg="Black")
title.pack(side=TOP,fill=X)

Man_fr1=Frame(base,bd=4,relief=RIDGE,bg="#28B5B5")
Man_fr1.place(x=10,y=65,width=600,height=720)

l = Label(Man_fr1,text="Faculty Data",font=("times new roman", 25,"bold"),bg="#28B5B5",fg="Black")
l.place(x=3,y=10)

l1 = Label(Man_fr1,text="Name",font=("Calisto MT", 22),bg="#28B5B5",fg="Black")
l1.place(x=30,y=80)

t1 = Entry(Man_fr1,font=("Calisto MT", 15),fg="black")
t1.place(x=300,y=80,width=250)


l2 = Label(Man_fr1,text="Faculty Id.",font=("Calisto MT", 22),bg="#28B5B5",fg="Black")
l2.place(x=30,y=120)


t2 = Entry(Man_fr1,font=("Calisto MT", 15),fg="black")
t2.place(x=300,y=120,width=250)


l3 = Label(Man_fr1,text="Email-id",font=("Calisto MT", 22),bg="#28B5B5",fg="Black")
l3.place(x=30,y=160)

t3 = Entry(Man_fr1,font=("Calisto MT", 15),fg="black")
t3.place(x=300,y=160,width=250)


l4 = Label(Man_fr1,text="Gender",font=("Calisto MT", 22),bg="#28B5B5",fg="Black")
l4.place(x=30,y=200)




countries = ("Male", "Female")
com = ttk.Combobox(Man_fr1, values=countries, state="read",font=("Calisto MT", 15))
com.place(x=300,y=200,width=250)




l5 = Label(Man_fr1,text="Faculty Contact No",font=("Calisto MT", 22),bg="#28B5B5",fg="Black")
l5.place(x=30,y=240)

t5 = Entry(Man_fr1,font=("Calisto MT", 15),fg="black")
t5.place(x=300,y=240,width=250)




l6 = Label(Man_fr1,text="D.O.B.",font=("Calisto MT", 22),bg="#28B5B5",fg="Black")
l6.place(x=30,y=280)

t6 = Entry(Man_fr1,font=("Calisto MT", 15),fg="black")
t6.place(x=300,y=280,width=250)


l7 = Label(Man_fr1,text="Department",font=("Calisto MT", 22),bg="#28B5B5",fg="Black")
l7.place(x=30,y=320)

t7= Entry(Man_fr1,font=("Calisto MT", 15),fg="black")
t7.place(x=300,y=320,width=250)


l8 = Label(Man_fr1,text="Date of Joinnig",font=("Calisto MT", 22),bg="#28B5B5",fg="Black")
l8.place(x=30,y=360)

t8= Entry(Man_fr1,font=("Calisto MT", 15),fg="black")
t8.place(x=300,y=360,width=250)

l9 = Label(Man_fr1,text="Address",font=("Calisto MT", 22),bg="#28B5B5",fg="Black")
l9.place(x=30,y=400)

t9= Entry(Man_fr1,font=("Calisto MT", 15),fg="black")
t9.place(x=300,y=400,width=250)





bt1 = Button(Man_fr1,text="Add",font=("times new roman", 20,"bold"),bg="#D2E603",fg="Black",width="6",command=event1)
bt1.place(x=50,y=610)

bt2 = Button(Man_fr1,text="Update",font=("times new roman", 20,"bold"),bg="#D2E603",fg="Black",width="6",command=event3)
bt2.place(x=170,y=610)

bt3 = Button(Man_fr1,text="Delete",font=("times new roman", 20,"bold"),bg="#D2E603",fg="Black",width="6",command=event4)
bt3.place(x=290,y=610)

bt4 = Button(Man_fr1,text="Reset",font=("times new roman", 20,"bold"),bg="#D2E603",fg="Black",width="6",command=event2)
bt4.place(x=410,y=610)



dt_fr1=Frame(base,bd=4,relief=RIDGE,bg="#EDFFEC")
dt_fr1.place(x=620,y=190,width=910,height=595)

op_label = Label(dt_fr1, text="***Welcome***",  width=100, height=190, bg="#EDFFEC", font=("Lucida Calligraphy", 35))
op_label.pack(padx=1, pady=1)

dt_fr2=Frame(base,bd=4,relief=RIDGE,bg="#EDFFEC")
dt_fr2.place(x=620,y=65,width=910,height=120)

la1 = Label(dt_fr2,text="*Search Faculty*",font=("Calisto MT", 25),bg="#EDFFEC",fg="Black")
la1.place(x=290,y=10)


la2= Label(dt_fr2,text="Search By Faculty Id",font=("Calisto MT", 20),bg="#EDFFEC",fg="Black")
la2.place(x=50,y=60)

ta1 = Entry(dt_fr2,font=("Calisto MT", 20))
ta1.place(x=320,y=60)


def Exit():
    base.destroy()
def reset():
    ta1.delete(0,END)
    for widget in dt_fr1.winfo_children():
        widget.destroy()

    lab = Label(dt_fr1, text=".....Have A Good Day Sir.....", font=("Lucida Calligraphy", 30), bg="#EDFFEC")
    lab.place(x=200, y=200)



def search_Student():
    for widget in dt_fr1.winfo_children():
        widget.destroy()
    s_roll = str(ta1.get())
    q = f"select faculty_name,faculty_id,email_id,gender,contact_no,date_of_birth,department,joining_date,address from faculty_Data where faculty_id={s_roll}"
    cur = con.cursor()
    cur.execute(q)
    con.commit()

    data = cur.fetchone()
    print(data)
    con.close()
    if data is None:
        messagebox.showerror("Invalid", "No such faculty Id Number...!!!")

    else:
        name = Label(dt_fr1, text=f"faculty_name: {data[0]}", font=("Calisto MT", 20),bg="#EDFFEC",fg="black")
        name.place(x=70, y=10)

        faculty_id = Label(dt_fr1, text=f"faculty_id: {data[1]}", font=("Calisto MT", 20),bg="#EDFFEC",fg="black")
        faculty_id.place(x=70, y=50)

        email = Label(dt_fr1, text=f"email_id: {data[2]}", font=("Calisto MT", 20), bg="#EDFFEC", fg="black")
        email.place(x=70, y=90)

        gender = Label(dt_fr1, text=f"gender: {data[3]}", font=("Calisto MT", 20),bg="#EDFFEC",fg="black")
        gender.place(x=70, y=130)

        contact_no = Label(dt_fr1, text=f"contact_no: {data[4]}", font=("Calisto MT", 20),bg="#EDFFEC",fg="black")
        contact_no.place(x=70, y=170)

        date_of_birth = Label(dt_fr1, text=f"date_of_birth: {data[5]}", font=("Calisto MT", 20),bg="#EDFFEC",fg="black")
        date_of_birth.place(x=70, y=210)

        department = Label(dt_fr1, text=f"department: {data[6]}", font=("Calisto MT", 20),bg="#EDFFEC",fg="black")
        department.place(x=70, y=250)

        joining_date = Label(dt_fr1, text=f"joining_date: {data[7]}", font=("Calisto MT", 20),bg="#EDFFEC",fg="black")
        joining_date.place(x=70, y=290)

        address = Label(dt_fr1, text=f"address: {data[8]}", font=("Calisto MT", 20),bg="#EDFFEC",fg="black")
        address.place(x=70, y=330)




bt11= Button(dt_fr2,text="Search",font=("times new roman", 20),command=search_Student,bg="#D2E603",fg="Black")
bt11.place(x=650,y=50)

bt12= Button(dt_fr2,text="Reset",font=("times new roman", 20,"bold"),command=reset,bg="#D2E603",fg="Black")
bt12.place(x=790,y=50)
exit_label = Button(base, text="Dashbord", font=('Ink Free', 15), bg="#d2e603", fg="black",command=Exit)
exit_label.place(x=20, y=5)

base.mainloop()