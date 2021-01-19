from tkinter import *
import tkinter as tk
from tkinter import messagebox

import AfterLogin

import mysql.connector
# from AfterLogin import Profile
import RegisterPage

db=mysql.connector.connect(host="localhost", user="rootuser", passwd="root", database="myskillhub")
class Login:
    success =0
    def getVar(self):
        return self.success

    def Database(self):
        mycursor = db.cursor()
        mycursor.execute(
            "CREATE TABLE IF NOT EXISTS Users (Fname varchar(30), Password varchar(30));")
        mycursor.execute("SELECT * FROM Users WHERE Fname = 'admin' AND Password = 'admin'")
        if mycursor.fetchone() is None:
            mycursor.execute("INSERT INTO Users (Fname, Password) VALUES('admin', 'admin')")
        mycursor.close()

    def __init__(self, root):

        self.root=root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)
        #=====Background Image=====
        self.bg=PhotoImage(file="images/Login3.png")
        self.bg_image=Label(self.root,image=self.bg)
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #===Login Frame=====
        Frame_Login=Frame(self.root,bg="white").place(x=150,y=150,height=340,width=500)

        #===Labels=====
        title=Label(Frame_Login,text="Login Here",font=("Impact",35,"bold",),fg="#d77337",bg="White").place(x=230,y=150)
        desc = Label(Frame_Login, text="User Login Area", font=("Goudy old style", 15, "bold",), fg="#d25d17", bg="White").place(
            x=230, y=220)
        lbl_user=Label(Frame_Login,text="Username",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=230,y=270)
        self.txt_user=Entry(Frame_Login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=370,y=270)

        lbl_passwd = Label(Frame_Login, text="Password", font=("Goudy old style", 15, "bold"), fg="gray",
                         bg="white").place(x=230, y=320)
        self.txt_passwd = Entry(Frame_Login, show="*" ,font=("times new roman", 15),bg="light gray")
        self.txt_passwd.place(x=370, y=320)

        self.login_btn=Button(root,text="Login",bd=0,font=("Goudy old style", 15, "bold"),fg="white",
                         bg="orange",activebackground="white",command=self.login_function).place(x=250,y=470,width=120)
        forget=Button(Frame_Login,text="Click to Register",bd=0,bg="white",fg="#d77337",font=("goudy old style",15),command=self.loadRegister).place(x=230,y=370)

    def login_function(self):
        self.Database()
        mycursor = db.cursor()
        password=self.txt_passwd.get()
        if self.txt_user.get()=="" or self.txt_passwd == "":
            messagebox.showerror("Error", "Both the fields are mandatory", parent=self.root)
        else:
            mycursor.execute("SELECT * FROM users WHERE Fname = %s  AND Password = %s",
                             (self.txt_user.get(), self.txt_passwd.get()))
            if mycursor.fetchone() is not None:
                print("Success",self.txt_passwd.get())
                #messagebox.showinfo("Welcome", "Successfully logged in", parent=self.root)
                self.command()
                print("test")
                self.txt_passwd.delete(0, 'end')
                self.txt_user.delete(0, 'end')
            else:
                messagebox.showerror("Error", "Incorrect username or password", parent=self.root)

            mycursor.close()

    def command(self):
        self.newWindow=tk.Toplevel(self.root)
        self.app= AfterLogin.AL(self.newWindow)
    def loadRegister(self):
        self.newWindow1 = tk.Toplevel(self.root)
        self.app1 = RegisterPage.Register(self.newWindow1)

# root=Tk()
# obj=Login(root)
#
# root.mainloop()


