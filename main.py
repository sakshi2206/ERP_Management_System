from tkinter import *
import sqlite3
from tkinter import messagebox
from PIL import ImageTk,Image
from datetime import date
from datetime import timedelta
from datetime import datetime
from tkinter import ttk


base11 = Tk()
base11.state("zoomed")
base11.title("Student Manegement System")


load = Image.open("C:\\Users\\91901\\Downloads\\88.jpg")
ren= ImageTk.PhotoImage(load)
img = Label(base11,image=ren)
img.place(x=0,y=0)

def event1():


    root = sqlite3.connect("Library_management.db")
    base = Tk()
    base.title("LIBRARY")
    base.state("zoomed")
    base.configure(bg="#f1f6f9")
    style = ("Georgia", 15, 'normal')
    btn_bg_color = "#bae5e5"
    today = date.today()

    # Canvas left button rectangle box
    canvas = Canvas(base)
    canvas.place(x=0, y=10)
    canvas.config(width=550, height=800, bg="white")
    # Canvas values
    line = canvas.create_rectangle(0, 0, 1200, 1000, fill='#28b5b5', width=5)

    # vertical green line
    canvas_line = Canvas(base)
    canvas_line.place(x=551, y=10)
    canvas_line.config(width=8, height=1000, bg="#ddf516")

    # horizontal green line
    canvas_hori = Canvas(base)
    canvas_hori.place(x=551, y=50)
    canvas_hori.config(width=1000, height=10, bg="#ddf516")

    # fonts
    inside_font = ("Bell MT", 20, "normal")
    inside_fg_color = "black"
    inside_bg_color = "#f1f6f9"

    # Frame
    op_frame = Frame(base, bg="#edffec", borderwidth=0)
    op_label = Label(op_frame, text="***Welcome***", width=100, height=190, bg="#edffec",
                     font=("Lucida Calligraphy", 35))
    op_label.pack(padx=1, pady=1)
    op_frame.place(x=563, y=23, width=980, height=780)

    # horizontal green line
    canvas_hori = Canvas(base)
    canvas_hori.place(x=563, y=570)
    canvas_hori.config(width=1000, height=10, bg="#ddf516")

    # Frame
    Man_fr1 = Frame(base, bg="#edffec", borderwidth=0)
    Man_fr1.place(x=563, y=580, width=1000, height=250)

    title = Label(base, text="~~~~~~~ L I B R A R Y ~~~~~~~", font=("Script MT Bold", 25, "bold"), bg='#4b778d',
                  fg="white")
    title.pack(side=TOP, fill=X)

    def Dash():
        base.destroy()

    def issue_book():
        def issue_new_book():
            b_num = book_num_entry.get()
            b_name = book_name_entry.get()
            s_name = stud_name_entry.get()
            s_roll = stud_roll_entry.get()
            dates = date.today()
            return_date = dates + timedelta(7)
            status = "not_returned"
            query = f"select Num, Name from book_info where Num={b_num}"
            cur = root.cursor()
            cur.execute(query)
            data = cur.fetchone()
            print(data)
            root.commit()

            if data:
                query2 = f"Insert into issue_book values({b_num}, '{b_name}', '{s_name}', {s_roll}, '{dates}', '{return_date}', '{status}')"
                root.execute(query2)
                root.commit()

                messagebox.showinfo("success", "Book Issued..!!")
            if data is None:
                messagebox.showinfo("fail", "Book Not Found.!!")

        for widget in op_frame.winfo_children():
            widget.destroy()

        issue_book_label = Label(op_frame, text="*Issue Book*", font=("Imprint MT Shadow", 25, "underline"),
                                 bg="#ffd56b",
                                 fg="black")
        issue_book_label.place(x=360, y=30)

        book_num = Label(op_frame, text="Book Number:", font=inside_font, bg=inside_bg_color)
        book_num.place(x=70, y=120)

        book_name = Label(op_frame, text="Book Name:", font=inside_font, bg=inside_bg_color)
        book_name.place(x=70, y=200)

        stud_name = Label(op_frame, text="Student Name:", font=inside_font, bg=inside_bg_color)
        stud_name.place(x=70, y=280)

        stud_roll = Label(op_frame, text="Student Roll no:", font=inside_font, bg=inside_bg_color)
        stud_roll.place(x=70, y=360)

        issue_date = Label(op_frame, text="Issue Date:", font=inside_font, bg=inside_bg_color)
        issue_date.place(x=70, y=420)

        issue_dateg = Label(op_frame, text=today, font=inside_font, bg=inside_bg_color)
        issue_dateg.place(x=300, y=420)

        # entry widgets
        book_num_entry = Entry(op_frame, width=25, font=inside_font)
        book_num_entry.place(x=300, y=120, height=35)

        book_name_entry = Entry(op_frame, width=25, font=inside_font)
        book_name_entry.place(x=300, y=200, height=35)

        stud_name_entry = Entry(op_frame, width=25, font=inside_font)
        stud_name_entry.place(x=300, y=280, height=35)

        stud_roll_entry = Entry(op_frame, width=25, font=inside_font)
        stud_roll_entry.place(x=300, y=360, height=35)

        save_btn = Button(op_frame, text=" ISSUE ", font=("Bell MT", 16, "bold"), bg="#9dab86", command=issue_new_book)
        save_btn.place(x=280, y=480)

        reset_btn = Button(op_frame, text=" RESET ", font=("Bell MT", 16, "bold"), bg="#9dab86")
        reset_btn.place(x=400, y=480)

    def return_book():
        def fine_check():
            b_num = book_num_entry.get()
            new_return_date = date.today()
            query = f"select return_date from issue_book where book_num = {b_num}"
            cur = root.cursor()
            cur.execute(query)
            data = cur.fetchone()
            # root.commit()
            print(data[0], "data is")
            already_date = datetime.strptime(data[0], "%Y-%m-%d").date()

            print(already_date)
            if already_date > new_return_date:
                messagebox.showinfo("Fine", "No Fine..!")
            else:
                extra_days = new_return_date - already_date
                total_extra_days = extra_days.days
                fine = total_extra_days * 3
                messagebox.showinfo(f"pay Fine of {fine} rs")
                print(fine)

        def returned():
            b_num = book_num_entry.get()
            query = f"select book_num from issue_book where book_num = {b_num}"
            cur = root.cursor()
            cur.execute(query)
            data = cur.fetchone()
            root.commit()
            print(data)
            if data:
                b_num = book_num_entry.get()
                query2 = f"delete from issue_book where book_num = {b_num}"
                cur = root.cursor()
                cur.execute(query2)
                data = cur.fetchone()
                root.commit()
                print(data)
                messagebox.showinfo("returned", "book returned")
            else:
                messagebox.showinfo("Invalid", "Not Found.!!")

        for widget in op_frame.winfo_children():
            widget.destroy()

        return_book_label = Label(op_frame, text="*Return Book*", font=("Imprint MT Shadow", 25, "underline"),
                                  bg="#ffd56b", fg="black")
        return_book_label.place(x=360, y=30)

        book_num = Label(op_frame, text="Book Number:", font=inside_font, bg=inside_bg_color)
        book_num.place(x=70, y=120)

        stud_name = Label(op_frame, text="Student Name:", font=inside_font, bg=inside_bg_color)
        stud_name.place(x=70, y=180)

        book_num_entry = Entry(op_frame, width=25, font=inside_font)
        book_num_entry.place(x=300, y=120, height=35)

        stud_name_entry = Entry(op_frame, width=25, font=inside_font)
        stud_name_entry.place(x=300, y=200, height=35)

        return_btn = Button(op_frame, text=" Return ", font=("Bell MT", 16, "bold"), bg="#9dab86")
        return_btn.place(x=280, y=480)

        check_fine_btn = Button(op_frame, text="Check Fine", font=("Bell MT", 16, "bold"), bg="#9dab86")
        check_fine_btn.place(x=400, y=480)

    def add_student():
        for widget in op_frame.winfo_children():
            widget.destroy()

        def add_stud_into_db():
            s_roll = stud_roll_entry.get()
            s_name = stud_name_entry.get()
            s_class = stud_class_entry.get()
            s_mob = stud_mob_entry.get()

            query = f"Insert into stud_info values({s_roll}, '{s_name}', '{s_class}', {s_mob})"
            root.execute(query)
            root.commit()
            messagebox.showinfo("Success", "Data saved..!!")

        def reset():
            stud_roll_entry.delete(0, END)
            stud_name_entry.delete(0, END)
            stud_class_entry.delete(0, END)
            stud_mob_entry.delete(0, END)
            stud_roll_entry.focus()

        add_student_label = Label(op_frame, text="*add new student*", font=("imprint mt shadow", 25, "underline"),
                                  bg="#ffd56b", fg="black")
        add_student_label.place(x=360, y=30)

        stud_roll = Label(op_frame, text="Student roll no:", font=inside_font, bg=inside_bg_color)
        stud_roll.place(x=70, y=120)

        stud_name = Label(op_frame, text="Student Name:", font=inside_font, bg=inside_bg_color)
        stud_name.place(x=70, y=200)

        stud_class = Label(op_frame, text="Student Class:", font=inside_font, bg=inside_bg_color)
        stud_class.place(x=70, y=280)

        stud_mob = Label(op_frame, text="Student Contact:", font=inside_font, bg=inside_bg_color)
        stud_mob.place(x=70, y=360)

        # entry widgets
        stud_roll_entry = Entry(op_frame, width=25, font=inside_font)
        stud_roll_entry.place(x=300, y=120, height=35)

        stud_name_entry = Entry(op_frame, width=25, font=inside_font)
        stud_name_entry.place(x=300, y=200, height=35)

        stud_class_entry = Entry(op_frame, width=25, font=inside_font)
        stud_class_entry.place(x=300, y=280, height=35)

        stud_mob_entry = Entry(op_frame, width=25, font=inside_font)
        stud_mob_entry.place(x=300, y=360, height=35)

        save_btn = Button(op_frame, text=" SAVE ", font=("Bell MT", 16, "bold"), bg="#9dab86", command=add_stud_into_db)
        save_btn.place(x=160, y=420)

        reset_btn = Button(op_frame, text=" RESET ", font=("Bell MT", 16, "bold"), bg="#9dab86", command=reset)
        reset_btn.place(x=290, y=420)

    def remove_stud():
        def delete_student():
            s_roll = stud_roll_entry.get()
            query_2 = f"delete from stud_info where roll={s_roll}"
            cur = root.cursor()
            cur.execute(query_2)
            data = cur.fetchone()
            root.commit()
            print(data)
            if data is None:
                messagebox.showinfo("Deleted", "Student removed...!!")

        for widget in op_frame.winfo_children():
            widget.destroy()

        add_student_label = Label(op_frame, text="*Remove student*", font=("imprint mt shadow", 25, "underline"),
                                  bg="#ffd56b", fg="black")
        add_student_label.place(x=360, y=30)

        stud_roll = Label(op_frame, text="Student roll no:", font=inside_font, bg=inside_bg_color)
        stud_roll.place(x=70, y=120)

        stud_name = Label(op_frame, text="Student Name:", font=inside_font, bg=inside_bg_color)
        stud_name.place(x=70, y=200)

        # entry widgets
        stud_roll_entry = Entry(op_frame, width=25, font=inside_font)
        stud_roll_entry.place(x=300, y=120, height=35)

        stud_name_entry = Entry(op_frame, width=25, font=inside_font)
        stud_name_entry.place(x=300, y=200, height=35)

        save_btn = Button(op_frame, text=" Remove ", font=("Bell MT", 16, "bold"), bg="#9dab86", command=delete_student)
        save_btn.place(x=160, y=420)

    def add_new_book():
        def add_new_book_into_db():
            book_number = book_num_entry.get()
            book_namee = book_name_entry.get()

            query = f"Insert into book_info values({book_number}, '{book_namee}')"
            root.execute(query)
            root.commit()
            messagebox.showinfo("Success", "Data saved..!!")

        def reset():
            book_num_entry.delete(0, END)
            book_name_entry.delete(0, END)
            book_num_entry.focus()

        for widget in op_frame.winfo_children():
            widget.destroy()

        return_book_label = Label(op_frame, text="*Add Book*", font=("Imprint MT Shadow", 25, "underline"),
                                  bg="#ffd56b", fg="black")
        return_book_label.place(x=360, y=30)

        book_num = Label(op_frame, text="Book Number:", font=inside_font, bg=inside_bg_color)
        book_num.place(x=70, y=120)

        stud_name = Label(op_frame, text="Book Name:", font=inside_font, bg=inside_bg_color)
        stud_name.place(x=70, y=180)

        book_num_entry = Entry(op_frame, width=25, font=inside_font)
        book_num_entry.place(x=300, y=120, height=35)

        book_name_entry = Entry(op_frame, width=25, font=inside_font)
        book_name_entry.place(x=300, y=200, height=35)

        return_btn = Button(op_frame, text=" ADD ", font=("Bell MT", 16, "bold"), bg="#9dab86",
                            command=add_new_book_into_db)
        return_btn.place(x=280, y=480)

        return_btn = Button(op_frame, text=" RESET ", font=("Bell MT", 16, "bold"), bg="#9dab86",
                            command=reset)
        return_btn.place(x=380, y=480)

    def remove_book():

        def delete_book():
            b_num = book_num_entry.get()
            query_2 = f"delete from book_info where Num={b_num}"
            cur = root.cursor()
            cur.execute(query_2)
            data = cur.fetchone()
            root.commit()
            print(data)
            if data is None:
                messagebox.showinfo("Deleted", "Book removed...!!")

        for widget in op_frame.winfo_children():
            widget.destroy()

        return_book_label = Label(op_frame, text="*Remove Book*", font=("Imprint MT Shadow", 25, "underline"),
                                  bg="#ffd56b", fg="black")
        return_book_label.place(x=360, y=30)

        book_num = Label(op_frame, text="Book Number:", font=inside_font, bg=inside_bg_color)
        book_num.place(x=70, y=120)

        book_num_entry = Entry(op_frame, width=25, font=inside_font)
        book_num_entry.place(x=300, y=120, height=35)

        return_btn = Button(op_frame, text=" REMOVE", font=("Bell MT", 16, "bold"), bg="#9dab86", command=delete_book)
        return_btn.place(x=280, y=480)

    def search_book():
        def search():
            s_book = book_num_entry.get()
            query = f"select Name from book_info where Num = {s_book}"
            cur = root.cursor()
            cur.execute(query)
            data = cur.fetchone()
            root.commit()
            print(data)
            if data is None:
                messagebox.showerror("Invalid", "No such book..!!!")
            else:
                name = Label(Man_fr1, text=f"B_Name: {data[0]}", font=("Calisto MT", 14))
                name.place(x=30, y=100)

        for widget in op_frame.winfo_children():
            widget.destroy()

        for widget in Man_fr1.winfo_children():
            widget.destroy()

        return_book_label = Label(op_frame, text="*Search Book*", font=("Imprint MT Shadow", 25, "underline"),
                                  bg="#ffd56b", fg="black")
        return_book_label.place(x=360, y=30)

        book_num = Label(op_frame, text="Book Number:", font=inside_font, bg=inside_bg_color)
        book_num.place(x=70, y=120)

        book_num_entry = Entry(op_frame, width=25, font=inside_font)
        book_num_entry.place(x=300, y=120, height=35)

        return_btn = Button(op_frame, text="Search", font=("Bell MT", 16, "bold"), bg="#9dab86", command=search)
        return_btn.place(x=280, y=480)

    def search_stud():
        def search():
            s_roll = str(stud_roll_entry.get())
            query = f"select Name, Class, Contact from stud_info where roll={s_roll}"
            cur = root.cursor()
            cur.execute(query)
            root.commit()
            data = cur.fetchone()
            print(data)
            if data is None:
                messagebox.showerror("Invalid", "No such Roll Number...!!!")

            else:
                name = Label(Man_fr1, text=f"Name: {data[0]}", font=("Calisto MT", 14))
                name.place(x=40, y=50)

                classs = Label(Man_fr1, text=f"Class: {data[1]}", font=("Calisto MT", 14))
                classs.place(x=40, y=90)

                mob = Label(Man_fr1, text=f"Mobile No: {data[2]}", font=("Calisto MT", 14))
                mob.place(x=40, y=130)

        for widget in op_frame.winfo_children():
            widget.destroy()

        for widget in Man_fr1.winfo_children():
            widget.destroy()

        return_book_label = Label(op_frame, text="*Search Student*", font=("Imprint MT Shadow", 25, "underline"),
                                  bg="#ffd56b", fg="black")
        return_book_label.place(x=360, y=30)

        book_num = Label(op_frame, text="Student Roll no:", font=inside_font, bg=inside_bg_color)
        book_num.place(x=70, y=120)

        stud_roll_entry = Entry(op_frame, width=25, font=inside_font)
        stud_roll_entry.place(x=300, y=120, height=35)

        return_btn = Button(op_frame, text="Search", font=("Bell MT", 16, "bold"), bg="#9dab86", command=search)
        return_btn.place(x=280, y=480)

    def clear_all():
        for widget in op_frame.winfo_children():
            widget.destroy()

        for widget in Man_fr1.winfo_children():
            widget.destroy()

        lab = Label(op_frame, text=".....Have A Good Day Sir.....", font=("Lucida Calligraphy", 35), bg="#fcf8ec")
        lab.place(x=210, y=310)

    # library button
    issue_book_btn = Button(base, text="ISSUE BOOK", font=style, width=32, bg=btn_bg_color, fg="black",
                            command=issue_book)
    issue_book_btn.place(x=10, y=80)

    return_book_btn = Button(base, text="RETURN BOOK", font=style, width=32, bg=btn_bg_color, fg="black",
                             command=return_book)
    return_book_btn.place(x=10, y=140)

    rem_stud_btn = Button(base, text="ADD STUDENT", font=style, width=32, bg=btn_bg_color, fg="black",
                          command=add_student)
    rem_stud_btn.place(x=10, y=200)

    rem_stud_btn = Button(base, text="REMOVE STUDENT", font=style, width=32, bg=btn_bg_color, fg="black",
                          command=remove_stud)
    rem_stud_btn.place(x=10, y=260)

    add_book_btn = Button(base, text="ADD NEW BOOK", font=style, width=32, bg=btn_bg_color, fg="black",
                          command=add_new_book)
    add_book_btn.place(x=10, y=320)

    remove_book_btn = Button(base, text="REMOVE BOOK", font=style, width=32, bg=btn_bg_color, fg="black",
                             command=remove_book)
    remove_book_btn.place(x=10, y=380)

    search_book_btn = Button(base, text="SEARCH BOOK", font=style, width=32, bg=btn_bg_color, fg="black",
                             command=search_book)
    search_book_btn.place(x=10, y=440)

    search_stud_btn = Button(base, text="SEARCH STUDENT", font=style, width=32, bg=btn_bg_color, fg="black",
                             command=search_stud)
    search_stud_btn.place(x=10, y=500)

    ret_remainder_btn = Button(base, text="SEND REMAINDER", font=style, width=32, bg=btn_bg_color, fg="black", )
    ret_remainder_btn.place(x=10, y=560)

    clear_btn = Button(base, text="CLEAR", font=style, width=32, bg=btn_bg_color, fg="black", command=clear_all)
    clear_btn.place(x=10, y=560)

    exit_label = Button(base, text="Log_out", font=('Ink Free', 15), bg="#d2e603", fg="black",command=Dash)
    exit_label.place(x=1110, y=10)

    base.mainloop()






def event2():


    con = sqlite3.connect("COllge_Student_info.db")
    base = Tk()
    base.state("zoomed")
    base.title("Student Manegement System")

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

        con = sqlite3.connect("COllge_Student_info.db")
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

        con = sqlite3.connect("COllge_Student_info.db")
        q = "update Student_Data set Name='" + a + "',Email='" + c + "',Gender='" + d + "',StudentContact=" + e + ",DOB=" + f + ",PRN=" + g + ",Branch='" + h + "',CurrentYear=" + i + ",Division='" + j + "',ParentContact=" + k + ",Address='" + l + "' where Roll=" + b
        con.execute(q)
        con.commit()
        con.close()
        messagebox.showinfo("Data", "Updated Sucessfully.....")
        event2()

    def event4():
        b = str(t2.get())
        con = sqlite3.connect("COllge_Student_info.db")
        q = "delete from Student_Data where Roll=" + b
        con.execute(q)
        con.commit()
        con.close()
        messagebox.showinfo("Data", "Data deleted Sucessfully.....")
        event2()

    title = Label(base, text="Student Manegement System", bd=10, relief=GROOVE, font=("times new roman", 30, "bold"),
                  bg="Sky blue", fg="Black")
    title.pack(side=TOP, fill=X)

    Man_fr1 = Frame(base, bd=4, relief=RIDGE, bg="Sky Blue")
    Man_fr1.place(x=10, y=65, width=600, height=720)

    l = Label(Man_fr1, text="Student Data", font=("times new roman", 25, "bold"), bg="Sky Blue", fg="black")
    l.place(x=3, y=10)

    l1 = Label(Man_fr1, text="Name", font=("Calisto MT", 22), bg="Sky Blue", fg="black")
    l1.place(x=30, y=80)

    t1 = Entry(Man_fr1, font=("Calisto MT", 15), fg="black")
    t1.place(x=300, y=80, width=250)

    l2 = Label(Man_fr1, text="Roll No.", font=("Calisto MT", 22), bg="Sky Blue", fg="black")
    l2.place(x=30, y=120)

    t2 = Entry(Man_fr1, font=("Calisto MT", 15), fg="black")
    t2.place(x=300, y=120, width=250)

    l3 = Label(Man_fr1, text="Email-id", font=("Calisto MT", 22), bg="Sky Blue", fg="black")
    l3.place(x=30, y=160)

    t3 = Entry(Man_fr1, font=("Calisto MT", 15), fg="black")
    t3.place(x=300, y=160, width=250)

    l4 = Label(Man_fr1, text="Gender", font=("Calisto MT", 22), bg="Sky Blue", fg="black")
    l4.place(x=30, y=200)

    countries = ("Male", "Female", "Others")
    com = ttk.Combobox(Man_fr1, values=countries, state="read", font=("Calisto MT", 15))
    com.place(x=300, y=200, width=250)

    l5 = Label(Man_fr1, text="Student Contact No", font=("Calisto MT", 22), bg="Sky Blue", fg="black")
    l5.place(x=30, y=240)

    t5 = Entry(Man_fr1, font=("Calisto MT", 15), fg="black")
    t5.place(x=300, y=240, width=250)

    l6 = Label(Man_fr1, text="D.O.B.", font=("Calisto MT", 22), bg="Sky Blue", fg="black")
    l6.place(x=30, y=280)

    t6 = Entry(Man_fr1, font=("Calisto MT", 15), fg="black")
    t6.place(x=300, y=280, width=250)

    l7 = Label(Man_fr1, text="PRN No", font=("Calisto MT", 22), bg="Sky Blue", fg="black")
    l7.place(x=30, y=320)

    t7 = Entry(Man_fr1, font=("Calisto MT", 15), fg="black")
    t7.place(x=300, y=320, width=250)

    l8 = Label(Man_fr1, text="Branch", font=("Calisto MT", 22), bg="Sky Blue", fg="black")
    l8.place(x=30, y=360)

    t8 = Entry(Man_fr1, font=("Calisto MT", 15), fg="black")
    t8.place(x=300, y=360, width=250)

    l9 = Label(Man_fr1, text="Current Year", font=("Calisto MT", 22), bg="Sky Blue", fg="black")
    l9.place(x=30, y=400)

    t9 = Entry(Man_fr1, font=("Calisto MT", 15), fg="black")
    t9.place(x=300, y=400, width=250)

    l10 = Label(Man_fr1, text="Division", font=("Calisto MT", 22), bg="Sky Blue", fg="black")
    l10.place(x=30, y=440)

    t10 = Entry(Man_fr1, font=("Calisto MT", 15), fg="black")
    t10.place(x=300, y=440, width=250)

    l11 = Label(Man_fr1, text="Parent Contact No", font=("Calisto MT", 22), bg="Sky Blue", fg="black")
    l11.place(x=30, y=480)

    t11 = Entry(Man_fr1, font=("Calisto MT", 15), fg="black")
    t11.place(x=300, y=480, width=250)

    l12 = Label(Man_fr1, text="Address", font=("Calisto MT", 22), bg="Sky Blue", fg="black")
    l12.place(x=30, y=520)

    t12 = Entry(Man_fr1, font=("Calisto MT", 15), fg="black")
    t12.place(x=300, y=520, width=250)

    bt1 = Button(Man_fr1, text="Add", font=("times new roman", 20, "bold"), bg="Sky Blue", width="6", command=event1)
    bt1.place(x=50, y=610)

    bt2 = Button(Man_fr1, text="Update", font=("times new roman", 20, "bold"), bg="Sky Blue", width="6", command=event3)
    bt2.place(x=170, y=610)

    bt3 = Button(Man_fr1, text="Delete", font=("times new roman", 20, "bold"), bg="Sky Blue", width="6", command=event4)
    bt3.place(x=290, y=610)

    bt4 = Button(Man_fr1, text="Reset", font=("times new roman", 20, "bold"), bg="Sky Blue", width="6", command=event2)
    bt4.place(x=410, y=610)

    dt_fr1 = Frame(base, bd=4, relief=RIDGE, bg="Sky Blue")
    dt_fr1.place(x=620, y=190, width=910, height=595)

    op_label = Label(dt_fr1, text="***Welcome***", width=100, height=190, bg="Sky Blue",
                     font=("Lucida Calligraphy", 35))
    op_label.pack(padx=1, pady=1)

    dt_fr2 = Frame(base, bd=4, relief=RIDGE, bg="Sky Blue")
    dt_fr2.place(x=620, y=65, width=910, height=120)

    la1 = Label(dt_fr2, text="*Search Student*", font=("Calisto MT", 25), bg="Sky Blue", fg="black")
    la1.place(x=290, y=10)

    la2 = Label(dt_fr2, text="Search By Roll No", font=("Calisto MT", 20), bg="Sky Blue", fg="black")
    la2.place(x=50, y=60)

    ta1 = Entry(dt_fr2, font=("Calisto MT", 20))
    ta1.place(x=320, y=60)

    def reset():
        ta1.delete(0, END)
        for widget in dt_fr1.winfo_children():
            widget.destroy()

        lab = Label(dt_fr1, text=".....Have A Good Day Sir.....", font=("Lucida Calligraphy", 30), bg="Sky Blue")
        lab.place(x=200, y=200)

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
            name = Label(dt_fr1, text=f"Name: {data[0]}", font=("Calisto MT", 20), bg="Sky Blue", fg="black")
            name.place(x=70, y=10)

            Roll = Label(dt_fr1, text=f"Roll No: {data[1]}", font=("Calisto MT", 20), bg="Sky Blue", fg="black")
            Roll.place(x=70, y=50)

            Email = Label(dt_fr1, text=f"Email: {data[2]}", font=("Calisto MT", 20), bg="Sky Blue", fg="black")
            Email.place(x=70, y=90)

            Gender = Label(dt_fr1, text=f"Gender: {data[3]}", font=("Calisto MT", 20), bg="Sky Blue", fg="black")
            Gender.place(x=70, y=130)

            StudentContact = Label(dt_fr1, text=f"StudentContact: {data[4]}", font=("Calisto MT", 20), bg="Sky Blue",
                                   fg="black")
            StudentContact.place(x=70, y=170)

            DOB = Label(dt_fr1, text=f"DOB: {data[5]}", font=("Calisto MT", 20), bg="Sky Blue", fg="black")
            DOB.place(x=70, y=210)

            PRN = Label(dt_fr1, text=f"PRN: {data[6]}", font=("Calisto MT", 20), bg="Sky Blue", fg="black")
            PRN.place(x=70, y=250)

            Branch = Label(dt_fr1, text=f"Branch: {data[7]}", font=("Calisto MT", 20), bg="Sky Blue", fg="black")
            Branch.place(x=70, y=290)

            CurrentYear = Label(dt_fr1, text=f"CurrentYear: {data[8]}", font=("Calisto MT", 20), bg="Sky Blue",
                                fg="black")
            CurrentYear.place(x=70, y=330)

            Division = Label(dt_fr1, text=f"Division: {data[9]}", font=("Calisto MT", 20), bg="Sky Blue", fg="black")
            Division.place(x=70, y=370)

            ParentContact = Label(dt_fr1, text=f"ParentContact: {data[10]}", font=("Calisto MT", 20), bg="Sky Blue",
                                  fg="black")
            ParentContact.place(x=70, y=410)

            Address = Label(dt_fr1, text=f"Address: {data[11]}", font=("Calisto MT", 20), bg="Sky Blue", fg="black")
            Address.place(x=70, y=440)

    bt11 = Button(dt_fr2, text="Search", font=("times new roman", 20), command=search_Student, bg="Sky Blue",
                  fg="black")
    bt11.place(x=650, y=50)

    bt12 = Button(dt_fr2, text="Reset", font=("times new roman", 20, "bold"), command=reset, bg="Sky Blue", fg="black")
    bt12.place(x=790, y=50)

    base.mainloop()




img1=PhotoImage(file="C:\\Users\\91901\\Downloads\\button.png")
bt1 =Button(base11,image=img1,bd=0,bg="#FFFFFF",command=event1)
bt1.place(x=20,y=90)


issue_book_btn = Button(base11, text="Student Management", width=40,height="5", fg="black",bg="#B1303A", command=event2)
issue_book_btn.place(x=300, y=200)







base11.mainloop()


