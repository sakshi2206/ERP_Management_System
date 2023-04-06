from tkinter import *
import tkinter.messagebox
import os
import sqlite3
from tkinter import messagebox
from PIL import ImageTk,Image
from datetime import date
from datetime import timedelta
from datetime import datetime
from tkinter import ttk




def main():

    base = Tk()
    load = Image.open("D:\\Vaibhav\\Final Year project\\88.jpg")
    ren = ImageTk.PhotoImage(load)
    img = Label(base, image=ren)
    img.place(x=0, y=0)
    base.state("zoomed")
    title = Label(base, text="College Management System", bd=10, font=("times new roman", 45, "bold"),
                  bg="#72482F", fg="White")
    title.place(x=2, y=5)
    app = Screen_Window_1(base)



    base.mainloop()


class Screen_Window_1:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Window")
        self.master.geometry('1350x750')
        self.master.config(bg='Black')
        self.Frame = Frame(self.master, bg='Black')
        self.Frame.place(x=500,y=400)



        self.u_name = StringVar()  # x = StringVar()  Holds a string; default value is " "
        self.u_password = StringVar()

        self.Lbl_Title_Login = Label(self.Frame, text='Login ', font=('arial', 30, 'bold'), bg='Black',
                                     fg='White')
        self.Lbl_Title_Login.grid(row=0, column=0, columnspan=3, pady=10)

        self.Log_Frame_1 = LabelFrame(self.Frame, width=1350, height=600, relief='ridge', bg='Black', bd=15,
                                      font=('arial', 20, 'bold'))
        self.Log_Frame_1.grid(row=1, column=0)
        self.Log_Frame_2 = LabelFrame(self.Frame, width=1000, height=600, relief='ridge', bg='Black', bd=15,
                                      font=('arial', 20, 'bold'))
        self.Log_Frame_2.grid(row=2, column=0)

        # ===================================================LABEL and ENTRIES=======================================================================
        self.lbl_uname = Label(self.Log_Frame_1, text='Username', font=('arial', 20, 'bold'), bg='Black', fg='White', bd=20)
        self.lbl_uname.grid(row=0, column=0)
        self.txt_uname = Entry(self.Log_Frame_1, font=('arial', 20, 'bold'), textvariable=self.u_name)
        self.txt_uname.grid(row=0, column=1, padx=50)

        self.lbl_pass = Label(self.Log_Frame_1, text='Password', font=('arial', 20, 'bold'), bg='Black', fg='White', bd=20)
        self.lbl_pass.grid(row=1, column=0)
        self.txt_pass = Entry(self.Log_Frame_1, font=('arial', 20, 'bold'), show='*', textvariable=self.u_password)
        self.txt_pass.grid(row=1, column=1)

        # =============================================================BUTTONS=======================================================================
        self.login_button = Button(self.Log_Frame_2, text='Login', width=10, font=('airia', 15, 'bold'),
                                   command=self.Login)
        self.login_button.grid(row=3, column=0, padx=8, pady=20)

        self.reset_button = Button(self.Log_Frame_2, text='Reset', width=10, font=('airia', 15, 'bold'),
                                   command=self.Reset)
        self.reset_button.grid(row=3, column=1, padx=8, pady=20)

        self.exit_button = Button(self.Log_Frame_2, text='Exit', width=10, font=('airia', 15, 'bold'),
                                  command=self.Exit)
        self.exit_button.grid(row=3, column=2, padx=8, pady=20)

        # ======================================================Code for Login Button==================================================================

    def Login(self):
        u = (self.u_name.get())
        p = (self.u_password.get())

        if (u == str('DEOGIRI') and p == str(123)):
            tkinter.messagebox.askyesno("Login Successfully !")

            self.__menu__()


        else:
            tkinter.messagebox.askyesno("Login", "Error : Wrong Password")
            self.u_name.set("")
            self.u_password.set("")
            # self.text_Username.focus()

        # ======================================================Code for Reset Button==================================================================

    def Reset(self):
        self.u_name.set("")
        self.u_password.set("")
        self.txt_uname.focus()

    # ======================================================Code for Exit Button==================================================================

    def Exit(self):
        self.Exit = tkinter.messagebox.askokcancel("Login System", "Confirm if you want to Exit")
        if self.Exit > 0:
            self.master.destroy()
            return

    def __menu__(self):

        import Dashboard
        import College_Marksheet_Frontend

    '''def new_window(self):
        self.new_Window = Toplevel(self.master)
        self.app = Window_2(self.new_Window)'''







if __name__ == '__main__':
    main()


