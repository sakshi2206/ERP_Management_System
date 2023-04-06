from tkinter import *
import sqlite3

from tkinter import messagebox
# from twilio.rest import Client
from datetime import date

from datetime import timedelta
from datetime import datetime





root = sqlite3.connect("Library_management_New.db")
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
op_label = Label(op_frame, text="***Welcome***",  width=100, height=190, bg="#edffec", font=("Lucida Calligraphy", 35))
op_label.pack(padx=1, pady=1)
op_frame.place(x=563,y=23,width=980,height=780)

# horizontal green line
canvas_hori = Canvas(base)
canvas_hori.place(x=563, y=570)
canvas_hori.config(width=1000, height=10, bg="#ddf516")


# Frame
Man_fr1=Frame(base,bg="#edffec", borderwidth=0)
Man_fr1.place(x=563,y=580,width=1000,height=250)




title = Label(base, text="~~~~~~~ L I B R A R Y ~~~~~~~", font=("Script MT Bold", 25, "bold"), bg='#4b778d', fg="white")
title.pack(side=TOP,fill=X)


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


    issue_book_label = Label(op_frame, text="*Issue Book*", font=("Imprint MT Shadow", 25, "underline"), bg="#ffd56b",
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

    save_btn = Button(op_frame, text=" ISSUE ", font=("Bell MT", 16, "bold"), bg="#9dab86",command=issue_new_book)
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


    return_book_label = Label(op_frame, text="*Return Book*", font=("Imprint MT Shadow", 25, "underline"), bg="#ffd56b", fg="black")
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


    add_student_label = Label(op_frame, text="*add new student*", font=("imprint mt shadow", 25, "underline"), bg="#ffd56b", fg="black")
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

    save_btn = Button(op_frame, text=" Remove ", font=("Bell MT", 16, "bold"), bg="#9dab86",command=delete_student)
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


    return_book_label = Label(op_frame, text="*Add Book*", font=("Imprint MT Shadow", 25, "underline"), bg="#ffd56b", fg="black")
    return_book_label.place(x=360, y=30)

    book_num = Label(op_frame, text="Book Number:", font=inside_font, bg=inside_bg_color)
    book_num.place(x=70, y=120)

    stud_name = Label(op_frame, text="Book Name:", font=inside_font, bg=inside_bg_color)
    stud_name.place(x=70, y=180)

    book_num_entry = Entry(op_frame, width=25, font=inside_font)
    book_num_entry.place(x=300, y=120, height=35)

    book_name_entry = Entry(op_frame, width=25, font=inside_font)
    book_name_entry.place(x=300, y=200, height=35)

    return_btn = Button(op_frame, text=" ADD ", font=("Bell MT", 16, "bold"), bg="#9dab86",command=add_new_book_into_db)
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


    return_book_label = Label(op_frame, text="*Remove Book*", font=("Imprint MT Shadow", 25, "underline"), bg="#ffd56b", fg="black")
    return_book_label.place(x=360, y=30)

    book_num = Label(op_frame, text="Book Number:", font=inside_font, bg=inside_bg_color)
    book_num.place(x=70, y=120)

    book_num_entry = Entry(op_frame, width=25, font=inside_font)
    book_num_entry.place(x=300, y=120, height=35)

    return_btn = Button(op_frame, text=" REMOVE", font=("Bell MT", 16, "bold"), bg="#9dab86",command=delete_book)
    return_btn.place(x=280, y=480)



def search_book():
    def search():
        s_book = book_num_entry.get()
        query = f"select Name from book_info where full outer join issue_book on issue_book.book_num,issue_book.book_name,issue_book.StudName  where book_num = {s_book}"
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
            name = Label(Man_fr1, text=f"book_num: {data[1]}", font=("Calisto MT", 14))
            name.place(x=35, y=100)
            name = Label(Man_fr1, text=f"book_name: {data[2]}", font=("Calisto MT", 14))
            name.place(x=40, y=100)
            name = Label(Man_fr1, text=f"StudName: {data[3]}", font=("Calisto MT", 14))
            name.place(x=45, y=100)







    for widget in op_frame.winfo_children():
        widget.destroy()

    for widget in Man_fr1.winfo_children():
        widget.destroy()


    return_book_label = Label(op_frame, text="*Search Book*", font=("Imprint MT Shadow", 25, "underline"), bg="#ffd56b", fg="black")
    return_book_label.place(x=360, y=30)

    book_num = Label(op_frame, text="Book Number:", font=inside_font, bg=inside_bg_color)
    book_num.place(x=70, y=120)

    book_num_entry = Entry(op_frame, width=25, font=inside_font)
    book_num_entry.place(x=300, y=120, height=35)

    return_btn = Button(op_frame, text="Search", font=("Bell MT", 16, "bold"), bg="#9dab86",command=search)
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

    return_book_label = Label(op_frame, text="*Search Student*", font=("Imprint MT Shadow", 25, "underline"), bg="#ffd56b", fg="black")
    return_book_label.place(x=360, y=30)

    book_num = Label(op_frame, text="Student Roll no:", font=inside_font, bg=inside_bg_color)
    book_num.place(x=70, y=120)

    stud_roll_entry= Entry(op_frame, width=25, font=inside_font)
    stud_roll_entry.place(x=300, y=120, height=35)

    return_btn = Button(op_frame, text="Search", font=("Bell MT", 16, "bold"), bg="#9dab86",command=search)
    return_btn.place(x=280, y=480)




def clear_all():
    for widget in op_frame.winfo_children():
        widget.destroy()

    for widget in Man_fr1.winfo_children():
        widget.destroy()

    lab = Label(op_frame, text=".....Have A Good Day Sir.....", font=("Lucida Calligraphy", 35), bg="#fcf8ec")
    lab.place(x=210, y=310)












# library button
issue_book_btn = Button(base, text="ISSUE BOOK", font=style, width=32, bg=btn_bg_color, fg="black", command=issue_book)
issue_book_btn.place(x=10, y=80)


return_book_btn = Button(base, text="RETURN BOOK", font=style, width=32, bg=btn_bg_color, fg="black", command=return_book)
return_book_btn.place(x=10, y=140)

rem_stud_btn = Button(base, text="ADD STUDENT", font=style, width=32, bg=btn_bg_color, fg="black",command=add_student)
rem_stud_btn.place(x=10, y=200)


rem_stud_btn = Button(base, text="REMOVE STUDENT", font=style, width=32, bg=btn_bg_color, fg="black",command=remove_stud)
rem_stud_btn.place(x=10, y=260)


add_book_btn = Button(base, text="ADD NEW BOOK", font=style, width=32, bg=btn_bg_color, fg="black", command=add_new_book)
add_book_btn.place(x=10, y=320)

remove_book_btn = Button(base, text="REMOVE BOOK", font=style, width=32, bg=btn_bg_color, fg="black",command=remove_book)
remove_book_btn.place(x=10, y=380)

search_book_btn = Button(base, text="SEARCH BOOK", font=style, width=32, bg=btn_bg_color, fg="black",command=search_book)
search_book_btn.place(x=10, y=440)

search_stud_btn = Button(base, text="SEARCH STUDENT", font=style, width=32, bg=btn_bg_color, fg="black",command=search_stud)
search_stud_btn.place(x=10, y=500)

ret_remainder_btn = Button(base, text="SEND REMAINDER", font=style, width=32, bg=btn_bg_color, fg="black", )
ret_remainder_btn.place(x=10, y=560)

clear_btn = Button(base, text="CLEAR", font=style, width=32, bg=btn_bg_color, fg="black",command=clear_all)
clear_btn.place(x=10, y=560)


exit_label = Label(base, text="Log_out", font=('Ink Free', 15), bg="#d2e603", fg="black")
exit_label.place(x=1110, y=10)

exit_label = Button(base, text="Dashbord", font=('Ink Free', 15), bg="#d2e603", fg="black",command=Dash)
exit_label.place(x=20, y=5)


base.mainloop()