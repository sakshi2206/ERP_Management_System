from tkinter import *
import sqlite3

from tkinter import messagebox
# from twilio.rest import Client
from datetime import date

from datetime import timedelta
from datetime import datetime








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

def issue_book():
    def issue():
        b_num = str(book_num_entry.get())
        b_name = str(book_name_entry.get())
        s_name = str(stud_name_entry.get())
        s_roll = str(stud_roll_entry.get())
        dates = str(date.today())
        status = "not_returned"

        con = sqlite3.connect("COllge_Student_info.db")
        q = "insert into issue_book values(" + b_num + ", '" + b_name + "', '" + s_name + "', " + s_roll+","+dates+",'"+status+"')"
        con.execute(q)
        con.commit()
        con.close()
        messagebox.showinfo("Data", "Data Saved Sucessfully.....")








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

    save_btn = Button(op_frame, text=" ISSUE ", font=("Bell MT", 16, "bold"), bg="#9dab86",command=issue)
    save_btn.place(x=280, y=480)

    reset_btn = Button(op_frame, text=" RESET ", font=("Bell MT", 16, "bold"), bg="#9dab86")
    reset_btn.place(x=400, y=480)


def return_book():
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
        s_name = str(stud_name_entry.get())
        s_roll = str(stud_roll_entry.get())
        s_class = str(stud_class_entry.get())
        s_mob = str(stud_mob_entry.get())

        con = sqlite3.connect("COllge_Student_info.db")
        q = "insert into Stud_info values('" + s_name + "',"+ s_roll +",'"+ s_class + "'," + s_mob + ")"
        con.execute(q)
        con.commit()
        con.close()
        messagebox.showinfo("Data", "Data Saved Sucessfully.....")
        reset()

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
        s_roll = str(stud_roll_entry.get())

        con = sqlite3.connect("COllge_Student_info.db")
        q = "delete from Stud_info where Roll="+s_roll
        con.execute(q)
        con.commit()
        con.close()
        messagebox.showinfo("Data", "Data Saved Sucessfully.....")


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
        book_number = str(book_num_entry.get())
        book_namee = str(stud_name_entry.get())

        con = sqlite3.connect("COllge_Student_info.db")
        q = "insert into book_info values(" +book_number+ ",'" + book_namee  + "')"
        con.execute(q)
        con.commit()
        con.close()
        messagebox.showinfo("Data", "Data Saved Sucessfully.....")
        reset()

    def reset():
        book_num_entry.delete(0, END)
        stud_name_entry.delete(0, END)
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

    stud_name_entry = Entry(op_frame, width=25, font=inside_font)
    stud_name_entry.place(x=300, y=200, height=35)

    return_btn = Button(op_frame, text=" ADD ", font=("Bell MT", 16, "bold"), bg="#9dab86",command=add_new_book_into_db)
    return_btn.place(x=280, y=480)

    return_btn = Button(op_frame, text=" RESET ", font=("Bell MT", 16, "bold"), bg="#9dab86",
                        command=reset)
    return_btn.place(x=380, y=480)




def remove_book():

    def delete_book():
        b_num = book_num_entry.get()
        con = sqlite3.connect("COllge_Student_info.db")
        q = "delete from book_info where BookNo="+b_num
        cur = con.cursor()
        cur.execute(q)
        data = cur.fetchone()
        con.commit()
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
        s_book = str(book_num_entry.get())
        con = sqlite3.connect("COllge_Student_info.db")
        q= "select BookName from book_info where BookNo ="+s_book
        cur = con.cursor()
        cur.execute(q)
        data = cur.fetchone()
        con.commit()

        if data is None:
            messagebox.showerror("Invalid", "No such book..!!!")
        else:
            name = Label(Man_fr1, text=f"Book Name: {data[0]}", font=("Calisto MT", 14))
            name.place(x=30, y=100)


        con.close()



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
        s_roll = str(book_num_entry.get())
        con = sqlite3.connect("COllge_Student_info.db")
        q= "select Name,Class,MobileNo from Stud_info where Roll ="+s_roll
        cur = con.cursor()
        cur.execute(q)
        data = cur.fetchone()
        con.commit()

        if data is None:
            messagebox.showerror("Invalid", "No such book..!!!")
        else:


            name = Label(Man_fr1, text=f"Name: {data[0]}", font=("Calisto MT", 14))
            name.place(x=40, y=50)

            classs = Label(Man_fr1, text=f"Class: {data[1]}", font=("Calisto MT", 14))
            classs.place(x=40, y=90)

            mob = Label(Man_fr1, text=f"Mobile No: {data[2]}", font=("Calisto MT", 14))
            mob.place(x=40, y=130)

        con.close()


    for widget in op_frame.winfo_children():
        widget.destroy()

    for widget in Man_fr1.winfo_children():
        widget.destroy()

    return_book_label = Label(op_frame, text="*Search Student*", font=("Imprint MT Shadow", 25, "underline"), bg="#ffd56b", fg="black")
    return_book_label.place(x=360, y=30)

    book_num = Label(op_frame, text="Student Roll no:", font=inside_font, bg=inside_bg_color)
    book_num.place(x=70, y=120)

    book_num_entry = Entry(op_frame, width=25, font=inside_font)
    book_num_entry.place(x=300, y=120, height=35)

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

base.mainloop()