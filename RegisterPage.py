from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import mysql.connector
#
registerdb=mysql.connector.connect(host="localhost", user="rootuser", passwd="root", database="myskillhub")

class Register:

    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="gray")

        #===BG Image=====
        self.bg=PhotoImage(file="Images/bg8.png")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        #===LEft IMage===
        self.left = PhotoImage(file="Images/img9.png")
        left = Label(self.root, image=self.left).place(x=80, y=150,width=400,height=500)

        #====Register======
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=150,width=700,height=500)

        title=Label(frame1,text="REGISTER HERE",font=("Times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=50)

        #==============First name and last name==============

        f_name = Label(frame1, text="First name", font=("Times new roman", 15), bg="white", fg="gray").place(
            x=50, y=100)

        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)
        l_name = Label(frame1, text="Last name", font=("Times new roman", 15), bg="white", fg="gray").place(
            x=370, y=100)

        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=370, y=130, width=250)

        #================Password and Confirm===============

        l_pass = Label(frame1, text="Password", font=("Times new roman", 15), bg="white", fg="gray").place(
            x=50, y=160)

        self.txt_pass = Entry(frame1,show="*", font=("times new roman", 15), bg="lightgray")
        self.txt_pass.place(x=50, y=190, width=250)

        l_cpass = Label(frame1, text="Confirm Password", font=("Times new roman", 15), bg="white", fg="gray").place(
            x=370, y=160)

        self.txt_cpass= Entry(frame1,show="*", font=("times new roman", 15), bg="lightgray")
        self.txt_cpass.place(x=370, y=190, width=250)

        #=================Interest===============================
        l_interst = Label(frame1, text="Interest", font=("Times new roman", 15), bg="white", fg="gray").place(
            x=50, y=220)
        self.cmb_interest = ttk.Combobox(frame1, text="Interests(Coding", font=("Times new roman", 15),state="readonly",justify="center")
        self.cmb_interest['values']=("Select","Python","Java","React","AWS")
        self.cmb_interest.place(
            x=50, y=250)
        self.cmb_interest.current(0)

        #==========Button==============
        self.btn_image=PhotoImage(file="Images/submit.png")
        btn=Button(frame1,image=self.btn_image,bd=0,command=self.feed_Info).place(x=50,y=300,height=50,width=200)
        btn_back = Button(frame1, command=(root.destroy), text="Back", fg="White", bg="Red").place(x=50, y=400)

    def feed_Info(self):
        mycursor = registerdb.cursor()
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_pass.get()=="" or self.txt_cpass.get()=="" or self.cmb_interest.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.txt_pass.get()!=self.txt_cpass.get():
            messagebox.showerror("Error", "Passwords don't match!", parent=self.root)
        else:
            mycursor.execute("CREATE TABLE IF NOT EXISTS Users (Fname varchar(30),Lname varchar(30),Password varchar(30))")
            mycursor.execute("INSERT INTO Users ( Fname, Lname,Password) VALUES(%s,%s,%s)", (self.txt_fname.get(), self.txt_lname.get(),self.txt_pass.get()))
        registerdb.commit()
        mycursor.close()
        messagebox.showinfo("Success","Successfully Registered", parent=self.root)
        print("closed")
# root=Tk()
# obj=Register(root)
# root.mainloop()