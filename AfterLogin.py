import textTospeech
import summarizer
from tkinter import *
from tkinter import PhotoImage, messagebox
import mysql.connector
import tkinter as tk
import cv2
import pytesseract

try:
    import os
    import tkinter.ttk as ttk
    from tkinter import filedialog
except ImportError:
    import Tkinter as tk
    import ttk
    import tkFileDialog as filedialog

db = mysql.connector.connect(host="localhost", user="rootuser", passwd="root", database="myskillhub")


# ===========CODE TO SUMMARISE
# text=input("Enter text: ")
# summarizer.summarize1(text)

# #==========CODE TO GET TEXT IN THE FORM OF AUDIO
# text = input("Enter the text you want in the Audible form: ")
# textTospeech.Say(text)

# #=========DISPLAY OF LOGIN PAGE
# Loginpage.displayLogin()
#
# #=========DISPLAY OF REGISTER PAGE
# registerPage.showRegisterPage()
# root = tk.Tk()
# US.show()
# root.mainloop()


class Audible:
    def __init__(self, root):
        self.root = root

    def listen(self):
        textTospeech.Say(self.txt_audio.get(1.0, END))

    def setup(self):
        self.frame6 = tk.Toplevel(self.root)
        self.frame6.geometry("1000x600+850+50")
        self.frame6.state('zoomed')
        self.img_pic = PhotoImage(file="Images/bg7.png")
        lnl = Label(self.frame6, image=self.img_pic).place(x=1, y=1, relheight=1, relwidth=1)
        style = ttk.Style(self.frame6)
        style.theme_use("clam")
        self.txt_audio = tk.Text(self.frame6)
        self.txt_audio.place(x=50, y=50, height=500, width=500)


        self.lbl_info = Label(self.frame6, text="Welcome to your very own Audible!", bg="#52af52", fg="white",
                              font=("Times new Roman", 20)).place(x=650, y=50)
        self.lbl_info = Label(self.frame6, text="Listen to your favorite piece of article and do your work! ", bg="#52af52",
                              fg="white", font=("Times new Roman", 15, "italic")).place(x=650, y=100)

        self.lbl_info = Label(self.frame6, text="Enter your text here!", bg="#52af52", fg="white",
                              font=("Times new Roman", 15)).place(x=50, y=25)
        btn_listen = Button(self.frame6, text="Convert", bg="green", fg="white",font="Bahnschrift 15",command=self.listen).place(x=50, y=570)
        btn_back = tk.Button(self.frame6, command=(self.frame6.destroy), text="Back",font="Bahnschrift 15", fg="White", bg="Red").place(x=600, y=570)



class ImageTextReader:
    def __init__(self, root):
        self.root = root

    def setup(self):
        self.frame6 = tk.Toplevel(self.root)
        self.frame6.geometry("1000x600+850+50")
        self.frame6.state('zoomed')
        self.img_pic = PhotoImage(file="Images/bg7.png")
        lnl = Label(self.frame6, image=self.img_pic).place(x=1, y=1, relheight=1, relwidth=1)
        style = ttk.Style(self.frame6)
        style.theme_use("clam")

        lbl_choose = Label(self.frame6, text="Type the path to your image:", bg="Red", fg="White", font=(12)).place(
            x=10, y=10)
        self.img_path = Entry(self.frame6)
        self.img_path.place(x=10, y=40, width=200, height=50)

        self.txt_result = Text(self.frame6)
        self.txt_result.place(x=500, y=40, height=500, width=300)

        btn_convert = Button(self.frame6, text="Convert", bg="Green", fg="white", font=15, command=self.convert).place(
            x=10, y=200)
        btn_back = tk.Button(self.frame6, command=(self.frame6.destroy), text="Back", fg="White", bg="Red",
                             font=15).place(x=100, y=200)

    def convert(self):
        img = cv2.imread(self.img_path.get())
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        custom_config = r'--oem 3 --psm 6'
        self.txt_result.insert(1.0, pytesseract.image_to_string(img, config=custom_config))


class Message1:
    def __init__(self, root):
        self.root = root
        self.name = "none"

    def setup(self):

        self.frame4 = tk.Toplevel(self.root, bg="gray")
        self.frame4.geometry("1000x600+850+50")
        self.frame4.state('zoomed')
        l_panelMem = Label(self.frame4, text="Our Experts")

        self.Bg1 = PhotoImage(file="Images/bg7.png")
        l_1 = Label(self.frame4, image=self.Bg1).place(x=1, y=1, relheight=1, relwidth=1)

        self.p1 = PhotoImage(file="Images/Avtar1.png")
        frame5 = tk.Label(self.frame4, image=self.p1, bd=1).place(x=30, y=30, height=100, width=100)

        l_p1 = Button(self.frame4, text="Rajesh kumar\nWeb Devloper", command=self.change_label1, font=15).place(x=30,
                                                                                                                 y=140)
        pic2 = tk.Label(self.frame4, image=self.p1, bd=1).place(x=200, y=30, height=100, width=100)

        l_p2 = Button(self.frame4, text="Tarun kumar\nAI Expert", command=self.change_label2, font=15).place(x=200,
                                                                                                             y=140)

        l_p3 = Button(self.frame4, text="Admin\nAI Expert", font=15, command=self.change_label3).place(x=500, y=140)
        pic2 = tk.Label(self.frame4, image=self.p1, bd=1).place(x=500, y=30, height=100, width=100)

        self.lbl_name = Label(self.frame4, text="Message to:", font=15, bg="red", fg="white")
        self.lbl_name.place(x=30, y=250)
        self.txt_msg = Text(self.frame4)
        self.txt_msg.place(x=30, y=300, height=100, width=200)
        self.lbl_rec = Label(self.frame4, text="Recieved messages:", bg="red", fg="white", font=15).place(x=1000, y=200)
        self.txt_msg_r = Text(self.frame4)
        self.txt_msg_r.place(x=1000, y=250, height=100, width=200)

        btn_back = tk.Button(self.frame4, command=(self.frame4.destroy), text="Back", fg="White", bg="Red",
                             font=15).place(x=150, y=420)
        btn_send = tk.Button(self.frame4, text="Send", bg="green", fg="white", command=self.pr1, font=15).place(x=30,
                                                                                                                y=420)

    def pr(self):
        self.lbl_name['text'] = 'Message to: Tarun Kumar'

        mycursor = db.cursor()
        mycursor.execute("Select * from users")
        result = mycursor.fetchall()
        for i in result:
            self.txt_msg_r.insert(1.0, i)

    def change_label1(self):
        self.name = "Ravi"
        self.lbl_name['text'] = 'Message to: ' + self.name

    def change_label2(self):
        self.name = "Tarun"
        self.lbl_name['text'] = 'Message to: ' + self.name

    def change_label3(self):
        self.name = "Admin"
        self.lbl_name['text'] = 'Message to: ' + self.name

    def pr1(self):

        mycursor = db.cursor()
        if self.txt_msg.get(1.0, END) == 0:
            messagebox.showerror("Error", "Message box is empty", parent=self.root)
        else:
            sendr = "Admin"
            mycursor.execute("Insert into message(sender,reciever,msg) values(%s,%s,%s)",
                             (sendr, self.name, self.txt_msg.get(1.0, END)))

            if self.name == "Admin":
                # mycursor.execute("Select msg from message where reciever = 'Admin';")
                self.txt_msg_r.insert(1.0, self.txt_msg.get(1.0, END))
            db.commit()
            mycursor.close()


class GetSummary:
    def __init__(self, root):
        self.root = root

    def d(self):
        # print(self.txt_sum.get())
        text1 = summarizer.summarize1(self.txt_sum.get(1.0, END))
        self.txt_sum_res.insert(1.0, text1)

    def Summ(self):
        frame2 = Toplevel(self.root, bg="gray")
        frame2.geometry("1000x600+850+50")
        frame2.state('zoomed')
        self.Bg2 = PhotoImage(file="Images/bg7.png")
        l_1 = Label(frame2, image=self.Bg2).place(x=1, y=1, relheight=1, relwidth=1)
        self.l_heading = tk.Label(frame2, text="Enter the text:", fg="white", font=("Times new roman", 15),
                                  bg="gray")
        self.l_heading.place(x=30, y=30)
        self.txt_sum = tk.Text(frame2)
        self.txt_sum.place(x=150, y=30, height=500, width=500)
        self.txt_sum_res = tk.Text(frame2)
        self.txt_sum_res.place(x=700, y=30, height=500, width=500)
        self.l_summary = Label(frame2, text="Your summary will appear here:", fg="white", bg="#e75f5b")
        self.l_summary.place(x=700, y=10)

        self.btn_sum = tk.Button(frame2, text="Get Summary",font="Bahnschrift 15", bg="green", fg="white", command=self.d).place(x=150, y=550)

        btn_back = tk.Button(frame2, command=(frame2.destroy),font="Bahnschrift 15", text="Back", fg="White", bg="Red").place(x=600, y=550)


class Audible1:
    def __int__(self, root):
        self.root = root


    def listen(self):
        textTospeech.Say(self.txt_audio.get(1.0, END))

    def begin(self):
        frame3 = tk.Toplevel(self.root, bg="#ba8181")
        frame3.geometry("1000x600+850+50")
        frame3.state('zoomed')

        self.txt_audio = tk.Text(frame3)
        self.txt_audio.place(x=50, y=50, height=500, width=500)

        self.lbl_info = Label(frame3, text="Welcome to your very own Audible!", bg="#52af52", fg="white",
                              font=("Times new Roman", 20)).place(x=650, y=50)
        self.lbl_info = Label(frame3, text="Listen to your favorite piece of article and do your work! ", bg="#52af52",
                              fg="white", font=("Times new Roman", 15, "italic")).place(x=650, y=100)

        self.lbl_info = Label(frame3, text="Enter your text here!", bg="#52af52", fg="white",
                              font=("Times new Roman", 15)).place(x=50, y=30)
        btn_listen = Button(frame3, text="Convert", bg="green", fg="white", command=self.listen).place(x=50, y=570)
        btn_back = tk.Button(frame3, command=(frame3.destroy), text="Back", fg="White", bg="Red").place(x=600, y=570)


class AL:
    # dictionary of colors:
    color = {"nero": "#e75f5b", "orange": "#52af52", "darkorange": "#ba8181"}

    # setting root window:
    def __init__(self, _w):
        self.root = _w
        # self.root.title("Tkinter Navbar")
        self.img = PhotoImage(file="Images/bg9.png")
        self.root.config(bg="gray17")
        self.lbl_1 = Label(self.root, image=self.img).place(x=0, y=0, relheight=1, relwidth=1)
        self.root.geometry("800x600+850+50")
        self.root.state('zoomed')

        # ==============FRAMES=========

        # setting switch state:
        self.btnState = False

        # loading Navbar icon image:
        self.navIcon = PhotoImage(file="Images/open.png")
        self.closeIcon = PhotoImage(file="Images/back1.png")

        # top Navigation bar:
        self.topFrame = tk.Frame(self.root, bg=self.color["orange"])
        self.topFrame.pack(side="top", fill=tk.X)

        # Header label text:
        self.homeLabel = tk.Label(self.topFrame, text="PE", font="Bahnschrift 15", bg=self.color["orange"], fg="gray17",
                                  height=2, padx=20)
        self.homeLabel.pack(side="right")

        # Main label text:
        self.brandLabel = tk.Label(self.root, text="MySkill\nHub", font="Sylfaen 30", bg="gray17", fg="green")
        frame2 = tk.Frame(self.root, bg="white")
        frame2.place(x=100, y=100)
        self.brandLabel.place(x=700, y=5)

        # Navbar button:
        self.navbarBtn = tk.Button(self.topFrame, image=self.navIcon, bg=self.color["orange"],
                                   activebackground=self.color["orange"], bd=0, padx=20, command=self.switch)
        self.navbarBtn.place(x=10, y=10)

        # setting Navbar frame:
        self.navRoot = tk.Frame(self.root, bg="gray17", height=1000, width=300)
        self.navRoot.place(x=-300, y=0)
        tk.Label(self.navRoot, font="Bahnschrift 15", bg=self.color["orange"], fg="black", height=2, width=300,
                 padx=20).place(x=0, y=0)

        # set y-coordinate of Navbar widgets:
        y = 80
        # option in the navbar:
        options = ["Profile", "Settings", "Help", "About", "Feedback"]
        # Navbar Option Buttons:

        for i in range(5):
            tk.Button(self.navRoot, text=options[i], font="BahnschriftLight 15", bg="gray17", fg=self.color["orange"],
                      activebackground="gray17", activeforeground="green", bd=0).place(x=25, y=y)
            y += 40

        # Navbar Close Button:
        self.closeBtn = tk.Button(self.navRoot, image=self.closeIcon, bg=self.color["orange"],
                                  activebackground=self.color["orange"], bd=0, command=self.switch)
        self.closeBtn.place(x=200, y=5, height=50, width=100)

        A = Audible(self.root)
        G = GetSummary(self.root)
        M = Message1(self.root)
        btn = tk.Button(self.root, text="Click here",font="Bahnschrift 15", command=G.Summ).place(x=500, y=300)

        T = ImageTextReader(self.root)

        # =====ICONS
        self.Icon1 = PhotoImage(file="Images/book.png")
        self.Icon2 = PhotoImage(file="Images/AudioIcon.png")
        self.Icon3 = PhotoImage(file="Images/icon4.png")
        self.Icon4 = PhotoImage(file="Images/text1.png")
        lbl = Label(self.root, image=self.Icon1, bd=10).place(x=500, y=120, height=180, width=180)
        lbl2 = Label(self.root, image=self.Icon2).place(x=800, y=120, height=180, width=180)
        lbl3 = Label(self.root, image=self.Icon3).place(x=500, y=420, height=180, width=180)
        lbl4 = Label(self.root, image=self.Icon4).place(x=800, y=420, height=180, width=180)

        btn2 = tk.Button(self.root, text="Click here For Audio",font="Bahnschrift 15", command=A.setup).place(x=800, y=300)
        btn3 = tk.Button(self.root, text="Click here For Message",font="Bahnschrift 15", command=M.setup).place(x=500, y=620)
        btn4 = tk.Button(self.root, text="Click here For Image to Text",font="Bahnschrift 15", command=T.setup).place(x=800, y=620)
        btn5 = tk.Button(self.root, text="Click to Logout",bg="red",font="Bahnschrift 15", command=self.root.destroy).place(x=1300, y=280)

    # setting switch function:
    def switch(self):

        if self.btnState is True:
            # create animated Navbar closing:
            for x in range(301):
                self.navRoot.place(x=-x, y=0)
                self.topFrame.update()

            # resetting widget colors:
            self.brandLabel.config(bg="gray17", fg="green")
            self.homeLabel.config(bg=self.color["orange"])
            self.topFrame.config(bg=self.color["orange"])
            self.root.config(bg="gray17")

            # turning button OFF:
            self.btnState = False
        else:
            # make root dim:
            self.brandLabel.config(bg=self.color["nero"], fg="#5F5A33")
            self.homeLabel.config(bg=self.color["nero"])
            self.topFrame.config(bg=self.color["nero"])
            self.root.config(bg=self.color["nero"])

            # created animated Navbar opening:
            for x in range(-300, 0):
                self.navRoot.place(x=x, y=0)
                self.topFrame.update()

            # turing button ON:
            self.btnState = True

# root = Tk()
# obj = AL(root)
# root.mainloop()
