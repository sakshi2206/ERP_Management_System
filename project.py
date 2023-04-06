from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk

con = sqlite3.connect("COllge_Student_info_New.db")
base = Tk()
base.state("zoomed")
base.title("Student Management System")


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
    j = str(t10.get())
    k = str(t11.get())
    l = str(t12.get())

    con = sqlite3.connect("COllge_Student_info_New.db")
    q = "insert into Student_Data values('" + a + "'," + b + ",'" + c + "','" + d + "'," + e + "," + f + "," + g + ",'" + h + "','" + i + "','" + j + "'," + k + ",'" + l + "')"
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
    t10.delete(0, END)
    t11.delete(0, END)
    t12.delete(0, END)


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
    j = str(t10.get())
    k = str(t11.get())
    l = str(t12.get())

    con = sqlite3.connect("COllge_Student_info_New.db")
    q = "update Student_Data set Name='" + a + "',Email='" + c + "',Gender='" + d + "',StudentContact=" + e + ",DOB=" + f + ",PRN=" + g + ",Branch='" + h + "',CurrentYear=" + i + ",Division='" + j + "',ParentContact=" + k + ",Address='" + l + "' where Roll=" + b
    con.execute(q)
    con.commit()
    con.close()
    messagebox.showinfo("Data", "Updated Sucessfully.....")
    event2()


def event4():
    b = str(t2.get())
    con = sqlite3.connect("COllge_Student_info_New.db")
    q = "delete from Student_Data where Roll=" + b
    con.execute(q)
    con.commit()
    con.close()
    messagebox.showinfo("Data", "Data deleted Sucessfully.....")
    event2()


title = Label(base, text="Student Management System", bd=10, relief=GROOVE, font=("times new roman", 30, "bold"),
              bg="#4B778D", fg="White")
title.pack(side=TOP, fill=X)

Man_fr1 = Frame(base, bd=4, relief=RIDGE, bg="#28B5B5")
Man_fr1.place(x=10, y=65, width=600, height=720)

l = Label(Man_fr1, text="Student Data", font=("times new roman", 25, "bold"), bg="#28B5B5", fg="black")
l.place(x=3, y=10)

l1 = Label(Man_fr1, text="Name", font=("Calisto MT", 22), bg="#28B5B5", fg="black")
l1.place(x=30, y=80)

t1 = Entry(Man_fr1, font=("Calisto MT", 15), fg="black")
t1.place(x=300, y=80, width=250)

l2 = Label(Man_fr1, text="Roll No.", font=("Calisto MT", 22), bg="#28B5B5", fg="black")
l2.place(x=30, y=120)

t2 = Entry(Man_fr1, font=("Calisto MT", 15), fg="black")
t2.place(x=300, y=120, width=250)

l3 = Label(Man_fr1, text="Email-id", font=("Calisto MT", 22), bg="#28B5B5", fg="black")
l3.place(x=30, y=160)

t3 = Entry(Man_fr1, font=("Calisto MT", 15), fg="black")
t3.place(x=300, y=160, width=250)

l4 = Label(Man_fr1, text="Gender", font=("Calisto MT", 22), bg="#28B5B5", fg="black")
l4.place(x=30, y=200)

countries = ("Male", "Female", "Others")
com = ttk.Combobox(Man_fr1, values=countries, state="read", font=("Calisto MT", 15))
com.place(x=300, y=200, width=250)

l5 = Label(Man_fr1, text="Student Contact No", font=("Calisto MT", 22), bg="#28B5B5", fg="black")
l5.place(x=30, y=240)

t5 = Entry(Man_fr1, font=("Calisto MT", 15), fg="black")
t5.place(x=300, y=240, width=250)

l6 = Label(Man_fr1, text="D.O.B.", font=("Calisto MT", 22), bg="#28B5B5", fg="black")
l6.place(x=30, y=280)

t6 = Entry(Man_fr1, font=("Calisto MT", 15), fg="black")
t6.place(x=300, y=280, width=250)

l7 = Label(Man_fr1, text="PRN No", font=("Calisto MT", 22), bg="#28B5B5", fg="black")
l7.place(x=30, y=320)

t7 = Entry(Man_fr1, font=("Calisto MT", 15), fg="black")
t7.place(x=300, y=320, width=250)

l8 = Label(Man_fr1, text="Branch", font=("Calisto MT", 22), bg="#28B5B5", fg="black")
l8.place(x=30, y=360)

t8 = Entry(Man_fr1, font=("Calisto MT", 15), fg="black")
t8.place(x=300, y=360, width=250)

l9 = Label(Man_fr1, text="Current Year", font=("Calisto MT", 22), bg="#28B5B5", fg="black")
l9.place(x=30, y=400)

t9 = Entry(Man_fr1, font=("Calisto MT", 15), fg="black")
t9.place(x=300, y=400, width=250)

l10 = Label(Man_fr1, text="Division", font=("Calisto MT", 22), bg="#28B5B5", fg="black")
l10.place(x=30, y=440)

t10 = Entry(Man_fr1, font=("Calisto MT", 15), fg="black")
t10.place(x=300, y=440, width=250)

l11 = Label(Man_fr1, text="Parent Contact No", font=("Calisto MT", 22), bg="#28B5B5", fg="black")
l11.place(x=30, y=480)

t11 = Entry(Man_fr1, font=("Calisto MT", 15), fg="black")
t11.place(x=300, y=480, width=250)

l12 = Label(Man_fr1, text="Address", font=("Calisto MT", 22), bg="#28B5B5", fg="black")
l12.place(x=30, y=520)

t12 = Entry(Man_fr1, font=("Calisto MT", 15), fg="black")
t12.place(x=300, y=520, width=250)

bt1 = Button(Man_fr1, text="Add", font=("times new roman", 20, "bold"), bg="#D2E603", width="6", command=event1)
bt1.place(x=50, y=610)

bt2 = Button(Man_fr1, text="Update", font=("times new roman", 20, "bold"), bg="#D2E603", width="6", command=event3)
bt2.place(x=170, y=610)

bt3 = Button(Man_fr1, text="Delete", font=("times new roman", 20, "bold"), bg="#D2E603", width="6", command=event4)
bt3.place(x=290, y=610)

bt4 = Button(Man_fr1, text="Reset", font=("times new roman", 20, "bold"), bg="#D2E603", width="6", command=event2)
bt4.place(x=410, y=610)

dt_fr1 = Frame(base, bd=4, relief=RIDGE, bg="#EDFFEC")
dt_fr1.place(x=620, y=190, width=910, height=595)

op_label = Label(dt_fr1, text="***Welcome***", width=100, height=190, bg="#EDFFEC",
                 font=("Lucida Calligraphy", 35))
op_label.pack(padx=1, pady=1)

dt_fr2 = Frame(base, bd=4, relief=RIDGE, bg="#EDFFEC")
dt_fr2.place(x=620, y=65, width=910, height=120)

la1 = Label(dt_fr2, text="*Search Student*", font=("Calisto MT", 25), bg="#EDFFEC", fg="black")
la1.place(x=290, y=10)

la2 = Label(dt_fr2, text="Search By Roll No", font=("Calisto MT", 20), bg="#EDFFEC", fg="black")
la2.place(x=50, y=60)

ta1 = Entry(dt_fr2, font=("Calisto MT", 20))
ta1.place(x=320, y=60)


def reset():
    ta1.delete(0, END)
    for widget in dt_fr1.winfo_children():
        widget.destroy()

    lab = Label(dt_fr1, text=".....Have A Good Day Sir.....", font=("Lucida Calligraphy", 30), bg="#EDFFEC")
    lab.place(x=200, y=200)

def Exit():
    base.destroy()
def search_Student():
    for widget in dt_fr1.winfo_children():
        widget.destroy()
    s_roll = str(ta1.get())
    query = f"select Name,Roll,Email,Gender,StudentContact,DOB,PRN,Branch,CurrentYear,Division,ParentContact,Address from Student_Data where Roll={s_roll}"
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    data = cur.fetchone()
    print(data)
    if data is None:
        messagebox.showerror("Invalid", "No such Roll Number...!!!")

    else:
        name = Label(dt_fr1, text=f"Name: {data[0]}", font=("Calisto MT", 20), bg="#EDFFEC", fg="black")
        name.place(x=70, y=10)

        Roll = Label(dt_fr1, text=f"Roll No: {data[1]}", font=("Calisto MT", 20), bg="#EDFFEC", fg="black")
        Roll.place(x=70, y=50)

        Email = Label(dt_fr1, text=f"Email: {data[2]}", font=("Calisto MT", 20), bg="#EDFFEC", fg="black")
        Email.place(x=70, y=90)

        Gender = Label(dt_fr1, text=f"Gender: {data[3]}", font=("Calisto MT", 20), bg="#EDFFEC", fg="black")
        Gender.place(x=70, y=130)

        StudentContact = Label(dt_fr1, text=f"StudentContact: {data[4]}", font=("Calisto MT", 20), bg="#EDFFEC",
                               fg="black")
        StudentContact.place(x=70, y=170)

        DOB = Label(dt_fr1, text=f"DOB: {data[5]}", font=("Calisto MT", 20), bg="#EDFFEC", fg="black")
        DOB.place(x=70, y=210)

        PRN = Label(dt_fr1, text=f"PRN: {data[6]}", font=("Calisto MT", 20), bg="#EDFFEC", fg="black")
        PRN.place(x=70, y=250)

        Branch = Label(dt_fr1, text=f"Branch: {data[7]}", font=("Calisto MT", 20), bg="#EDFFEC", fg="black")
        Branch.place(x=70, y=290)

        CurrentYear = Label(dt_fr1, text=f"CurrentYear: {data[8]}", font=("Calisto MT", 20), bg="#EDFFEC",
                            fg="black")
        CurrentYear.place(x=70, y=330)

        Division = Label(dt_fr1, text=f"Division: {data[9]}", font=("Calisto MT", 20), bg="#EDFFEC", fg="black")
        Division.place(x=70, y=370)

        ParentContact = Label(dt_fr1, text=f"ParentContact: {data[10]}", font=("Calisto MT", 20), bg="#EDFFEC",
                              fg="black")
        ParentContact.place(x=70, y=410)

        Address = Label(dt_fr1, text=f"Address: {data[11]}", font=("Calisto MT", 20), bg="#EDFFEC", fg="black")
        Address.place(x=70, y=440)


bt11 = Button(dt_fr2, text="Search", font=("times new roman", 20), command=search_Student, bg="#D2E603",
              fg="black")
bt11.place(x=650, y=50)

bt12 = Button(dt_fr2, text="Reset", font=("times new roman", 20, "bold"), command=reset, bg="#D2E603", fg="black")
bt12.place(x=790, y=50)
exit_label = Button(base, text="Dashbord", font=('Ink Free', 15), bg="#d2e603", fg="black",command=Exit)
exit_label.place(x=20, y=5)


base.mainloop()
