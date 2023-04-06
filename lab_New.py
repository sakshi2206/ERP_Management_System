
from tkinter import *
import sqlite3

from tkinter import messagebox
# from twilio.rest import Client
from datetime import date

from datetime import timedelta
from datetime import datetime

base = sqlite3.connect("Library_management.db")
today = date.today()
base = Tk()
base.title("LIBRARY")
base.geometry("1200x750")
# base.iconbitmap("lib.ico")
base.configure(bg="#f1f6f9")
style = ("Georgia", 15, 'normal')
btn_bg_color = "#bae5e5"

# Canvas left button rectangle box
canvas = Canvas(base)
canvas.place(x=0, y=20)
canvas.config(width=290, height=800, bg="white")
# Canvas values
line = canvas.create_rectangle(0, 0, 1200, 1000, fill='#28b5b5', width=5)

# vertical green line
canvas_line = Canvas(base)
canvas_line.place(x=285, y=10)
canvas_line.config(width=8, height=1000, bg="#ddf516")

# horizontal green line
canvas_hori = Canvas(base)
canvas_hori.place(x=285, y=50)
canvas_hori.config(width=1000, height=10, bg="#ddf516")

# vertical canvas line
canvas_mid = Canvas(base)
canvas_mid.place(x=900, y=10)
canvas_mid.config(width=4, height=1000, bg="black")

# fonts
inside_font = ("Bell MT", 20, "normal")
inside_fg_color = "black"
inside_bg_color = "#f1f6f9"

# Frame
op_frame = Frame(base, bg="#edffec", borderwidth=0)
op_label = Label(op_frame, text="***Welcome***",  width=100, height=190, bg="#edffec", font=("Lucida Calligraphy", 30))
op_label.pack(padx=1, pady=1)
op_frame.pack(pady=80, padx=320, side=RIGHT)

# frame 2
op_frame_2 = Frame(base, bg="#d2f6c5", borderwidth=5)
op_label_2 = Label(op_frame_2, width=35, height=40, bg="#d2f6c5")
op_label_2.pack(padx=1, pady=1)
op_frame_2.place(x=920, y=80)

def Dis():
    base.destroy()

# datetime.striptime
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

    for widget in op_frame_2.winfo_children():
        widget.destroy()
    issue_book_label = Label(op_frame, text="*Issue Book*", font=("Imprint MT Shadow", 25, "underline"), bg="#ffd56b", fg="black")
    issue_book_label.place(x=150, y=30)

    book_num = Label(op_frame, text="Book Number:", font=inside_font, bg=inside_bg_color)
    book_num.place(x=50, y=120)

    book_name = Label(op_frame, text="Book Name:", font=inside_font, bg=inside_bg_color)
    book_name.place(x=50, y=180)

    stud_name = Label(op_frame, text="Student Name:", font=inside_font, bg=inside_bg_color)
    stud_name.place(x=50, y=240)

    stud_roll = Label(op_frame, text="Student Roll no:", font=inside_font, bg=inside_bg_color)
    stud_roll.place(x=50, y=300)

    issue_date = Label(op_frame, text="Issue Date:", font=inside_font, bg=inside_bg_color)
    issue_date.place(x=50, y=360)

    issue_dateg = Label(op_frame, text=today, font=inside_font, bg=inside_bg_color)
    issue_dateg.place(x=260, y=360)
    # entry widgets
    book_num_entry = Entry(op_frame, width=15, font=inside_font)
    book_num_entry.place(x=260, y=125, height=25)

    book_name_entry = Entry(op_frame, width=15, font=inside_font)
    book_name_entry.place(x=260, y=185, height=25)

    stud_name_entry = Entry(op_frame, width=15, font=inside_font)
    stud_name_entry.place(x=260, y=245, height=25)

    stud_roll_entry = Entry(op_frame, width=15, font=inside_font)
    stud_roll_entry.place(x=260, y=305, height=25)

    save_btn = Button(op_frame, text=" Issue ", font=("Bell MT", 16, "bold"), bg="#9dab86", command=issue_new_book)
    save_btn.place(x=160, y=440)

    reset_btn = Button(op_frame, text=" RESET ", font=("Bell MT", 16, "bold"), bg="#9dab86")
    reset_btn.place(x=290, y=440)


def return_book():
    def fine_check():
        b_num = book_num_entry.get()
        new_return_date = date.today()
        query = f"select return_date from issue_book where book_num = {b_num}"
        cur = root.cursor()
        cur.execute(query)
        data = cur.fetchone()
        # root.commit()
        print(data[0],  "data is")
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

    for widget in op_frame_2.winfo_children():
        widget.destroy()
    return_book_label = Label(op_frame, text="*Return Book*", font=("Imprint MT Shadow", 25, "underline"), bg="#ffd56b", fg="black")
    return_book_label.place(x=150, y=30)

    book_num = Label(op_frame, text="Book Number:", font=inside_font, bg=inside_bg_color)
    book_num.place(x=50, y=120)

    stud_name = Label(op_frame, text="Student Name:", font=inside_font, bg=inside_bg_color)
    stud_name.place(x=50, y=180)

    book_num_entry = Entry(op_frame, width=15, font=inside_font)
    book_num_entry.place(x=260, y=125, height=25)

    stud_name_entry = Entry(op_frame, width=15, font=inside_font)
    stud_name_entry.place(x=260, y=185, height=25)

    return_btn = Button(op_frame, text=" Return ", font=("Bell MT", 16, "bold"), bg="#9dab86", command=returned)
    return_btn.place(x=290, y=240)

    check_fine_btn = Button(op_frame, text="Check Fine", font=("Bell MT", 16, "bold"), bg="#9dab86", command=fine_check)
    check_fine_btn.place(x=160, y=240)


def add_student():
    for widget in op_frame.winfo_children():
        widget.destroy()

    for widget in op_frame_2.winfo_children():
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

    add_student_label = Label(op_frame, text="*add new student*", font=("imprint mt shadow", 25, "underline"), bg="#ffd56b", fg="black")
    add_student_label.place(x=150, y=30)

    stud_roll = Label(op_frame, text="Student roll no:", font=inside_font, bg=inside_bg_color)
    stud_roll.place(x=50, y=120)

    stud_name = Label(op_frame, text="Student Name:", font=inside_font, bg=inside_bg_color)
    stud_name.place(x=50, y=180)

    stud_class = Label(op_frame, text="Student Class:", font=inside_font, bg=inside_bg_color)
    stud_class.place(x=50, y=240)

    stud_mob = Label(op_frame, text="Student Contact:", font=inside_font, bg=inside_bg_color)
    stud_mob.place(x=50, y=300)

    # entry widgets
    stud_roll_entry = Entry(op_frame, width=15, font=inside_font)
    stud_roll_entry.place(x=260, y=125, height=25)

    stud_name_entry = Entry(op_frame, width=15, font=inside_font)
    stud_name_entry.place(x=260, y=185, height=25)

    stud_class_entry = Entry(op_frame, width=15, font=inside_font)
    stud_class_entry.place(x=260, y=245, height=25)

    stud_mob_entry = Entry(op_frame, width=15, font=inside_font)
    stud_mob_entry.place(x=260, y=305, height=25)

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

    for widget in op_frame_2.winfo_children():
        widget.destroy()
    remove_student = Label(op_frame, text="*Remove student*", font=("imprint mt shadow", 25, "underline"), bg="#ffd56b",
                           fg="black")
    remove_student.place(x=150, y=30)

    stud_roll = Label(op_frame, text="Student roll no:", font=inside_font, bg=inside_bg_color)
    stud_roll.place(x=50, y=120)

    stud_name = Label(op_frame, text="Student Name:", font=inside_font, bg=inside_bg_color)
    stud_name.place(x=50, y=180)

    # Entry widgets
    stud_roll_entry = Entry(op_frame, width=15, font=inside_font)
    stud_roll_entry.place(x=260, y=125, height=25)

    stud_name_entry = Entry(op_frame, width=15, font=inside_font)
    stud_name_entry.place(x=260, y=185, height=25)

    # button
    remove_stud_btn = Button(op_frame, text=" REMOVE ", font=("Bell MT", 16, "bold"), bg="#9dab86", command=delete_student)
    remove_stud_btn.place(x=200, y=260)


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

    for widget in op_frame_2.winfo_children():
        widget.destroy()
    add_new_book_label = Label(op_frame, text="*Add New Book*", font=("imprint mt shadow", 25, "underline"), bg="#ffd56b",
                               fg="black")
    add_new_book_label.place(x=150, y=30)

    book_num = Label(op_frame, text="Book Number:", font=inside_font, bg=inside_bg_color)
    book_num.place(x=50, y=120)

    book_name = Label(op_frame, text="Book Name:", font=inside_font, bg=inside_bg_color)
    book_name.place(x=50, y=180)

    # Entry Widgets
    book_num_entry = Entry(op_frame, width=15, font=inside_font)
    book_num_entry.place(x=260, y=125, height=25)

    book_name_entry = Entry(op_frame, width=15, font=inside_font)
    book_name_entry.place(x=260, y=185, height=25)

    # button
    add_new_book_btn = Button(op_frame, text=" SAVE ", font=("Bell MT", 16, "bold"), bg="#9dab86", command=add_new_book_into_db)
    add_new_book_btn.place(x=220, y=320)

    reset_btn = Button(op_frame, text=" RESET ", font=("Bell MT", 16, "bold"), bg="#9dab86", command=reset)
    reset_btn.place(x=360, y=320)


def check_not_return_books():
    def not_returned():
        b_num = book_num_entry.get()
        query = f"select book_num, book_name from issue_book where book_num = {b_num}"
        cur = root.cursor()
        cur.execute(query)
        data = cur.fetchone()
        print(data)
        # root.commit()
        if data:
            labe = Label(op_frame_2, text=data[1], font=inside_font)
            labe.place(x=40, y=100)
            messagebox.showinfo("book found", "Status, Not returned..!")
        else:
            messagebox.showinfo("No Books", "No data Found..!")

    for widget in op_frame.winfo_children():
        widget.destroy()

    for widget in op_frame_2.winfo_children():
        widget.destroy()
    not_return_book = Label(op_frame, text="*Not Return Book*", font=("imprint mt shadow", 25, "underline"), bg="#ffd56b",
                            fg="black")
    not_return_book.place(x=150, y=30)

    book_num = Label(op_frame, text="Book Number:", font=inside_font, bg=inside_bg_color)
    book_num.place(x=50, y=120)

    # Entry widgets
    book_num_entry = Entry(op_frame, width=15, font=inside_font)
    book_num_entry.place(x=260, y=125, height=25)

    # Button widget
    check_btn = Button(op_frame, text=" Check ", font=("Bell MT", 16, "bold"), bg="#9dab86", command=not_returned)
    check_btn.place(x=260, y=200)


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

    for widget in op_frame_2.winfo_children():
        widget.destroy()
    remove_book_label = Label(op_frame, text="*Remove Book*", font=("imprint mt shadow", 25, "underline"), bg="#ffd56b",
                              fg="black")
    remove_book_label.place(x=150, y=30)

    book_num = Label(op_frame, text="Book Number:", font=inside_font, bg=inside_bg_color)
    book_num.place(x=50, y=120)

    # entry widgets
    book_num_entry = Entry(op_frame, width=15, font=inside_font)
    book_num_entry.place(x=260, y=125, height=25)

    # Button widget
    book_remove_btn = Button(op_frame, text=" Remove ", font=("Bell MT", 16, "bold"), bg="#9dab86", command=delete_book)
    book_remove_btn.place(x=210, y=260)


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
            name = Label(op_frame_2, text=f"B_Name: {data[0]}", font=("Calisto MT", 14))
            name.place(x=30, y=100)

    for widget in op_frame.winfo_children():
        widget.destroy()
    for widget in op_frame_2.winfo_children():
        widget.destroy()
    search_book_label = Label(op_frame, text="*Search Book*", font=("imprint mt shadow", 25, "underline"), bg="#ffd56b",
                              fg="black")
    search_book_label.place(x=150, y=30)

    book_num = Label(op_frame, text="Book Number:", font=inside_font, bg=inside_bg_color)
    book_num.place(x=50, y=120)

    # entry widgets
    book_num_entry = Entry(op_frame, width=15, font=inside_font)
    book_num_entry.place(x=260, y=125, height=25)

    # Button widget
    check_btn = Button(op_frame, text=" Search ", font=("Bell MT", 16, "bold"), bg="#9dab86", command=search)
    check_btn.place(x=210, y=240)


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
            name = Label(op_frame_2, text=f"Name: {data[0]}", font=("Calisto MT", 14))
            name.place(x=40, y=100)

            classs = Label(op_frame_2, text=f"Class: {data[1]}", font=("Calisto MT", 14))
            classs.place(x=40, y=140)

            mob = Label(op_frame_2, text=f"mob: {data[2]}", font=("Calisto MT", 14))
            mob.place(x=40, y=180)

    for widget in op_frame.winfo_children():
        widget.destroy()
    search_student_label = Label(op_frame, text="*Search Student*", font=("imprint mt shadow", 25, "underline"), bg="#ffd56b",
                                 fg="black")
    search_student_label.place(x=150, y=30)

    stud_roll_label = Label(op_frame, text="Student Roll no:", font=inside_font, bg=inside_bg_color)
    stud_roll_label.place(x=50, y=120)

    # entry widgets
    stud_roll_entry = Entry(op_frame, width=15, font=inside_font)
    stud_roll_entry.place(x=260, y=125, height=25)

    # Button widget
    check_btn = Button(op_frame, text=" Search", font=("Bell MT", 16, "bold"), bg="#9dab86", command=search)
    check_btn.place(x=220, y=240)


def return_remainder():
    for widget in op_frame.winfo_children():
        widget.destroy()

    for widget in op_frame_2.winfo_children():
        widget.destroy()
    return_remainder_label = Label(op_frame, text="*Return Remainder*", font=("imprint mt shadow", 25, "underline"), bg="#ffd56b",
                                   fg="black")
    return_remainder_label.place(x=150, y=30)

    stud_roll_label = Label(op_frame, text="Student Roll no:", font=inside_font, bg=inside_bg_color)
    stud_roll_label.place(x=50, y=120)

    # entry widgets
    stud_roll_entry = Entry(op_frame, width=15, font=inside_font)
    stud_roll_entry.place(x=260, y=125, height=25)

    # Button widget
    remainder_btn = Button(op_frame, text=" SEND ", font=("Bell MT", 16, "bold"), bg="#9dab86")
    remainder_btn.place(x=220, y=240)


def clear_all():
    for widget in op_frame.winfo_children():
        widget.destroy()

    for widget in op_frame_2.winfo_children():
        widget.destroy()
    lab = Label(op_frame, text=".....Have A Good Day Sir.....", font=("Lucida Calligraphy", 25), bg="#fcf8ec")
    lab.place(x=60, y=250)




# library label
title = Label(base, text="~~~~~~~ L I B R A R Y ~~~~~~~", font=("Script MT Bold", 19, "bold"), bg='#4b778d', fg="white", padx=400, pady=10)
title.place(x=0, y=0)

# library button
issue_book_btn = Button(base, text="ISSUE BOOK", font=style, width=22, bg=btn_bg_color, fg="black", command=issue_book)
issue_book_btn.place(x=10, y=60)

return_book_btn = Button(base, text="RETURN BOOK", font=style, width=22, bg=btn_bg_color, fg="black", command=return_book)
return_book_btn.place(x=10, y=110)

add_stud_btn = Button(base, text="ADD STUDENT", font=style, width=22, bg=btn_bg_color, fg="black", command=add_student)
add_stud_btn.place(x=10, y=160)

rem_stud_btn = Button(base, text="REMOVE STUDENT", font=style, width=22, bg=btn_bg_color, fg="black", command=remove_stud)
rem_stud_btn.place(x=10, y=210)

add_book_btn = Button(base, text="ADD NEW BOOK", font=style, width=22, bg=btn_bg_color, fg="black", command=add_new_book)
add_book_btn.place(x=10, y=260)

not_ret_book_btn = Button(base, text=" NOT RETURN BOOK", font=style, width=22, bg=btn_bg_color, fg="black", command=check_not_return_books)
not_ret_book_btn.place(x=10, y=310)

remove_book_btn = Button(base, text="REMOVE BOOK", font=style, width=22, bg=btn_bg_color, fg="black", command=remove_book)
remove_book_btn.place(x=10, y=360)

search_book_btn = Button(base, text="SEARCH BOOK", font=style, width=22, bg=btn_bg_color, fg="black", command=search_book)
search_book_btn.place(x=10, y=410)

search_stud_btn = Button(base, text="SEARCH STUDENT", font=style, width=22, bg=btn_bg_color, fg="black", command=search_stud)
search_stud_btn.place(x=10, y=460)

ret_remainder_btn = Button(base, text="SEND REMAINDER", font=style, width=22, bg=btn_bg_color, fg="black", command=return_remainder)
ret_remainder_btn.place(x=10, y=510)

clear_btn = Button(base, text="CLEAR", font=style, width=22, bg=btn_bg_color, fg="black", command=clear_all)
clear_btn.place(x=10, y=560)


exit_label = Button(base, text="Log_out", font=('Ink Free', 15), bg="#d2e603", fg="black",command=Dis)
exit_label.place(x=1110, y=10)
base.mainloop()










