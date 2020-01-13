from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from tkinter import *
from tkinter import filedialog
import sqlite3
import datetime


def login():
    global loginframe
    loginframe = Frame(frm)
    Label(loginframe, text='xxx', fg="red").pack()
    loginframe.pack()


frm = tk.Tk()
fnt = ('tahoma', 12)
bg = 'white'
bgtxt = 'white'
fg = 'black'
fw = 650
fh = 600
x = (frm.winfo_screenwidth() - fw) / 2
y = (frm.winfo_screenheight() - fh) / 2 - 50
pad = 10

frm.geometry('%dx%d+%d+%d' % (fw, fh, x, y))
#frm.title('Users')
frm.config(bg=bg)

svuser = StringVar()
svId = StringVar()
svfname = StringVar()
svlname = StringVar()
svpass = StringVar()
svgender = StringVar()
svrname = StringVar()
svmail = StringVar()
svphone = StringVar()
svprofile=StringVar()
svmassage=StringVar()
def Database():
    global conn, cursor
    conn = sqlite3.connect("Accept.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS admins (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, first_name TEXT,last_name TEXT, massage TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS users (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, first_name TEXT, last_name TEXT, id TEXT,responsible_name TEXT,Email Text,user_name TEXT, password TEXT,phone TEXT,gander TEXT,massage TEXT,profile BLOB NOT NULL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS boards(mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT,id TEXT)")
    conn.commit()

Database()

def insert_user(user_name,id,first_name,last_name,password,gander,responsible_name,Email,phone):
    cursor.execute("INSERT INTO users (first_name,last_name,id,responsible_name,Email,user_name,password,gander,phone) VALUES(?,?,?,?,?,?,?,?,?)",(first_name,last_name,id,responsible_name,Email,user_name,password,gander,phone))
    conn.commit()

def insert_board(name, id):
    cursor.execute("INSERT INTO boards (name,id) VALUES(?,?)", (name, id))
    conn.commit()

def delete_user(id):
    cursor.execute("DELETE FROM 'users' WHERE id=?",(id,))
    conn.commit()
def create():
   ''' if svuser.get().strip() == '':
        messagebox.showinfo('', 'The user name  is Empty!')
        txtuser.focus()
    elif svId.get().strip() == '':
        messagebox.showinfo('', 'The number of id is Empty!')
        txtid.focus()
    elif svpass.get().strip() == '':
        messagebox.showinfo('', 'The password Empty!')
        txtpass.focus()
    elif svfname.get().strip() == '':
        messagebox.showinfo('', 'The first name of the autistic is Empty!')
        txtfname.focus()
    elif svlname.get().strip() == '':
        messagebox.showinfo('', 'The last name of the autistic is Empty!')
        txtlname.focus()
    elif svgender.get() == '':
        messagebox.showinfo('', 'the gender is Empty!')
        txtgender.focus()
    elif svrname.get().strip() == '':
        messagebox.showinfo('', 'The name of the responsible is Empty!')
        txtrname.focus()
    elif svmail.get().strip() == '':
        messagebox.showinfo('', 'The E-mail of the responsible is Empty!')
        txtmail.focus()
    elif svphone).get().strip() == '':
        messagebox.showinfo('', 'The number phone of the responsible is Empty!'
        txtphone.focus()
    elif svprofile.get().strip()=='':
        messagebox.showinfo('', 'The profile is Empty!')

    else:'''
   #insert_user(svuser.get(), svId.get(), svfname.get(), svlname.get(), svpass.get(), svgender.get(), svrname.get(),svmail.get(), svphone.get(), svmassage.get())
   if i.get()==0:
       insert_user(txtuser.get(), txtid.get(), txtfname.get(), txtlname.get(), txtpass.get(), txtgender.get(),
                   txtrname.get(), txtmail.get(), txtphone.get())
   else:
       messagebox.showinfo('', 'you want to agree the terms')

   '''svId.set('')
   svfname.set('')
   svlname.set('')
   svgender.set('')
   svrname.set('')
   svmail.set('')
   svmassage.set('')
   svprofile.set('')
   frame.destroy()
   txtuser.set('')
   txtid.set('')
   txtfname.set('')
   txtlname.set('')
   txtpass.set('')
   txtgender.set('')
   txtrname.set('')
   txtmail.set('')
   txtphone.set('')'''

   frame.destroy()
   login()



def sign_up():
    global frame, txtuser, txtid, txtfname, txtlname, txtpass, txtgender, txtrname, txtmail, txtphone,txtprofile,txtmassage
    frame = Frame(frm, bg=bg)
    # Label(frame, text='User Data', bg='navy', fg='lightblue', font=fnt).pack(pady=pad)

    Label(frame, text='user name:', bg=bg, fg=fg, font=fnt).grid(row=0, column=0)
    Label(frame, text='Autistic ID number:', bg=bg, fg=fg, font=fnt).grid(row=1, column=0)
    Label(frame, text='The first name of the autistic :', bg=bg, fg=fg, font=fnt).grid(row=2, column=0)
    Label(frame, text='The last name of the autistic :', bg=bg, fg=fg, font=fnt).grid(row=3, column=0)
    Label(frame, text='The password :', bg=bg, fg=fg, font=fnt).grid(row=4, column=0)
    Label(frame, text='The gender of the autistic: ', bg=bg, fg=fg, font=fnt).grid(row=5, column=0)
    Label(frame, text='The name of the responsible :', bg=bg, fg=fg, font=fnt).grid(row=6, column=0)
    Label(frame, text='The E-mail of the responsible :', bg=bg, fg=fg, font=fnt).grid(row=7, column=0)
    Label(frame, text='The number phone of the responsible :', bg=bg, fg=fg, font=fnt).grid(row=8, column=0)

    #Label(frame, text='The profile of the Autistic :', bg=bg, fg=fg, font=fnt).grid(row=9, column=0)
    #Label(top, image=im).pack()
    txtuser = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svuser)
    txtid = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svId)
    txtfname = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svfname)
    txtlname = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svlname)
    txtpass = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svpass)
    txtgender = ttk.Combobox(frame, values=('Male', 'Female'),textvariable=svgender, state='readonly')
    txtrname = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svrname)
    txtmail = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svmail)
    txtphone = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svphone)
    txtprofile=Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svprofile)
    btns = ttk.Style()
    btns.configure('TButton', font=fnt, pady=pad, padding=pad)
    #c = Checkbutton(frame, text="I accept the Terms of service ", variable="unchecked", onvalue="checked").grid(row=11, column=0, pady=pad)
    #ttk.Button(frame, text='Create', command=create).grid(row=13, column=3, pady=pad)
    ttk.Button(frame, text='Back').grid(row=13, column=0, pady=8)
    ttk.Button(frame, text='Next',command=pageif).grid(row=13, column=3, pady=8)
    # ttk.Button(frm, text='Exit Now', command=frm.destroy).grid(row=9, column=2, pady=pad)

    txtuser.grid(row=0, column=1, pady=pad)
    txtid.grid(row=1, column=1, pady=pad)
    txtfname.grid(row=2, column=1, pady=pad)
    txtlname.grid(row=3, column=1, pady=pad)
    txtpass.grid(row=4, column=1, pady=pad)
    txtgender.grid(row=5, column=1, pady=pad)
    txtrname.grid(row=6, column=1, pady=pad)
    txtmail.grid(row=7, column=1, pady=pad)
    txtphone.grid(row=8, column=1, pady=pad)
    txtprofile.grid(row=9,column=1,pady=pad)

    frame.pack(pady=pad)
    frame.mainloop()
i=IntVar()
def pageif():
    if svuser.get().strip() == '':
        messagebox.showinfo('', 'The user name  is Empty!')
        txtuser.focus()
    elif svId.get().strip() == '':
        messagebox.showinfo('', 'The number of id is Empty!')
        txtid.focus()
    elif svpass.get().strip() == '':
        messagebox.showinfo('', 'The password Empty!')
        txtpass.focus()
    elif svfname.get().strip() == '':
        messagebox.showinfo('', 'The first name of the autistic is Empty!')
        txtfname.focus()
    elif svlname.get().strip() == '':
        messagebox.showinfo('', 'The last name of the autistic is Empty!')
        txtlname.focus()
    elif svgender.get() == '':
        messagebox.showinfo('', 'the gender is Empty!')
        txtgender.focus()
    elif svrname.get().strip() == '':
        messagebox.showinfo('', 'The name of the responsible is Empty!')
        txtrname.focus()
    elif svmail.get().strip() == '':
        messagebox.showinfo('', 'The E-mail of the responsible is Empty!')
        txtmail.focus()
    elif svphone.get().strip() == '':
        messagebox.showinfo('', 'The number phone of the responsible is Empty!')
        txtphone.focus()
    elif svprofile.get().strip()=='':
        messagebox.showinfo('', 'The profile is Empty!')
    else:
        fnt = ('tahoma', 12)
        bg = 'white'
        bgtxt = 'white'
        fg = 'black'
        fw = 650
        fh = 600
        x = (frm.winfo_screenwidth() - fw) / 2
        y = (frm.winfo_screenheight() - fh) / 2 - 50
        frm.geometry('%dx%d+%d+%d' % (fw, fh, x, y))
        root = Tk()
        Label(root, text='hhhhhhhhhhhh', bg=bg, fg=fg, font=fnt).grid(row=0, column=0)
        c = Checkbutton(root, text="I accept the Terms of service ", variable=i, onvalue="checked").grid(
            row=11, column=0, pady=pad)
        Button(root, text='Create', command=create).grid(row=13, column=3, pady=pad)
        root.mainloop()



def logout(frame):
    # Save in Data Base()
    svuser.set('')
    svpass.set('')
    frame.destroy()
    login()

def Database():
    global conn, cursor
    conn = sqlite3.connect("Accept.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS admins (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, first_name TEXT,last_name TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS users (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, first_name TEXT, last_name TEXT, id TEXT,responsible_name TEXT,Email Text,user_name TEXT, password TEXT,phone TEXT,gander text,profile BLOB)")
    cursor.execute("CREATE TABLE IF NOT EXISTS boards(mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT,id TEXT)")
    conn.commit()

Database()

def insert_user(user_name,id,first_name,last_name,password,gander,responsible_name,Email,phone):
    cursor.execute("INSERT INTO users (first_name,last_name,id,responsible_name,Email,user_name,password,gander,phone) VALUES(?,?,?,?,?,?,?,?,?)",(first_name,last_name,id,responsible_name,Email,user_name,password,gander,phone))
    conn.commit()

def insert_board(name, id):
    cursor.execute("INSERT INTO boards (name,id) VALUES(?,?)", (name, id))
    conn.commit()

def delete_user(username):
    cursor.execute("DELETE FROM 'users' WHERE user_name=?",(username,))
    conn.commit()

def delete_board(id):
    cursor.execute("DELETE FROM 'boards' WHERE id=?",(id,))
    conn.commit()

def update_information_user(name,last_name,password,user_name,email,responsible_name,phone):
    cursor.execute("UPDATE 'users' SET first_name=?,last_name=?,password=?,user_name=?,Email=?,responsible_name=?,phone=?",(name,last_name,password,user_name,email,responsible_name,phone))
    conn.commit()

def update_massage(massage,username):
    cursor.execute("UPDATE 'users' SET massage=? WHERE user_name=?",(massage,username))
    conn.commit()


def account():
    global a
    a=Frame(frm)
    def gotoLogin():
        a.forget()
        login()
        #main_page()
        #page5()
    Label(a,text="Choose Login Or Register", bg="blue", width="300")
    Label(a,text="").pack()
    Button(a,text="Log in",height="2",width="30",command=gotoLogin).pack()
    Label(a,text="").pack()
    Button(a,text="Create a new account?",height="2",width="30",command=sign_up).pack()
    a.pack()


def check(lable):
     cursor.execute("select * from 'users' where user_name=(?) and password=(?) ",(svuser.get(),svpass.get()))
     print(svuser.get(),svpass.get())
     if cursor.fetchone() is None:
         lable.config(text="Invalid Username or password", fg="red")


def checkuser(name):

    cursor.execute("select * from 'users' where user_name=? ", (name,))
    if cursor.fetchone() is not None:
        return True
    return False

def login():
    global loginFrame

    def main_page():
        frm = tk.Tk()
        fnt = ('tahoma', 16)
        bg = '#ffffff'
        bgtxt = '#00ff00'
        fg = '#000000'
        fw = 700
        fh = 600
        x = (frm.winfo_screenwidth() - fw) /2
        y = (frm.winfo_screenheight() - fh) / 2 - 50
        frm.geometry('%dx%d+%d+%d' % (fw, fh, x, y))
        #frm.title('Users')
        frm.config(bg=bg)
        B = tk.Button(frm, text="Board", bg="white", height="6", width="30", font="40").grid(row=0, column=1, pady=20)
        # B.pack()
        C = tk.Button(frm, text=" NEW Board", bg="white", height="6", width="30", font="30").grid(row=2, column=1,pady=20)
        # C.pack()
        A = tk.Button(frm, text="Setting", bg="white", height="6", width="30", font="30").grid(row=4, column=1, pady=20)
        # A.pack()
        frm.mainloop()

    loginFrame=Frame(frm)
    Label(loginFrame,text='',fg='red').grid(row=0,column=2, pady=20)
    Label(loginFrame,text="Enter user name:").grid(row=3,column=1)
    Entry(loginFrame,textvariable=svuser).grid(row=3,column=2)
    Label(loginFrame, text="Enter password:").grid(row=4, column=1)
    Entry(loginFrame, textvariable=svpass).grid(row=4,column=2)
    Button(loginFrame, text='log in',height="2",width="10").grid(row=7,column=5,pady=10)
    loginFrame.pack()



#account()
#frm.mainloop()

def page5():
    frm = tk.Tk()
    window = tk.Toplevel(frm)
    fnt = ('tahoma', 30)
    fw = 900
    fh = 800
    x = (frm.winfo_screenwidth() - fw) / 2
    y = (frm.winfo_screenheight() - fh) / 2 - 50
    frm.geometry('%dx%d+%d+%d' % (fw, fh, x, y))
    #frm.title('Users')
    frm.config(bg="white")

    Button(frm, text="Setting", bg="white", height="6", width="30", font="50").grid(row=6,column=1,padx=300,pady=20)
    Button(frm, text="Create a new board!", bg="white", height="6", width="30", font="50").grid(row=4,column=1,padx=300,pady=20)
    Button(frm, text="An existing boards", bg="white", height="6", width="30", font="50").grid(row=2,column=1,padx=200,pady=20)
    Button(frm, text="Profile", bg="white", height="6", width="15", font="50").grid(row=0,column=1,padx=200,pady=80)
    Button(frm, text="<- Back", bg="white", height="6", width="15", font="50").grid(row=10,column=1,padx=30,pady=80)




def page8():
    frm = tk.Tk()
    window = tk.Toplevel(frm)
    fnt = ('tahoma', 30)
    fw = 900
    fh = 800
    x = (frm.winfo_screenwidth() - fw) / 2
    y = (frm.winfo_screenheight() - fh) / 2 - 50
    frm.geometry('%dx%d+%d+%d' % (fw, fh, x, y))

    frm.config(bg="white")

    Button(frm, text="Language", bg="white", height="6", width="30", font="50").grid(row=4, column=1, padx=100,pady=20)
    Button(frm, text="About!", bg="white", height="6", width="30", font="50",command=HelpFunc).grid(row=2, column=1, padx=100,pady=20)
    Button(frm, text="Edit Profile", bg="white", height="6", width="30", font="50").grid(row=0, column=1,padx=100, pady=20)
    Button(frm, text="<- Back", bg="white", height="3", width="10", font="10").grid(row=10, column=0, padx=5, pady=80)
    frm.mainloop()

def HelpFunc(texthelp):
    frm = tk.Tk()
    global exp
    exp=texthelp

    fnt = ('tahoma', 30)
    fw = 900
    fh = 800
    x = (frm.winfo_screenwidth() - fw) / 2
    y = (frm.winfo_screenheight() - fh) / 2 - 50
    frm.geometry('%dx%d+%d+%d' % (fw, fh, x, y))

    frm.config(bg="white")
    HelpFunc2(exp)
    frm.mainloop()
def HelpFunc2(exp2):
    frm = tk.Tk()
    fnt = ('tahoma', 30)
    fw = 900
    fh = 800
    x = (frm.winfo_screenwidth() - fw) / 2
    y = (frm.winfo_screenheight() - fh) / 2 - 50
    frm.geometry('%dx%d+%d+%d' % (fw, fh, x, y))

    frm.config(bg="white")
    Label(frm, text=exp2, bg=bg, fg=fg, font=fnt).grid(row=2, column=2)

    frm.mainloop()
def page9():
    frame = tk.Tk()
    window = tk.Toplevel(frame)
    fnt = ('tahoma', 15)
    bg = "white"
    bgtxt = "white"
    fg = "black"
    fw = 900
    fh = 800
    x = (frame.winfo_screenwidth() - fw) / 2
    y = (frame.winfo_screenheight() - fh) / 2 - 50
    frame.geometry('%dx%d+%d+%d' % (fw, fh, x, y))
    frame.title('Update')
    svuser = StringVar()
    svId = StringVar()
    svfname = StringVar()
    svlname = StringVar()
    svpass = StringVar()
    svgender = StringVar()
    svrname = StringVar()
    svmail = StringVar()
    svphone = StringVar()
    svprofile = StringVar()
    frame.config(bg="white")
    Label(frame, text='user name:', bg=bg, fg=fg, font=fnt).grid(row=0, column=0,pady=20)
    Label(frame, text='The first name of the autistic :', bg=bg, fg=fg, font=fnt).grid(row=3, column=0,pady=20)
    Label(frame, text='The last name of the autistic :', bg=bg, fg=fg, font=fnt).grid(row=5, column=0,pady=20)
    Label(frame, text='The password :', bg=bg, fg=fg, font=fnt).grid(row=7, column=0,pady=20)
    Label(frame, text='The name of the responsible :', bg=bg, fg=fg, font=fnt).grid(row=9, column=0,pady=20)
    Label(frame, text='The E-mail of the responsible :', bg=bg, fg=fg, font=fnt).grid(row=11, column=0,pady=20)
    Label(frame, text='The number phone of the responsible :', bg=bg, fg=fg, font=fnt).grid(row=13, column=0,pady=20)
    # Label(frame, text='The profile of the Autistic :', bg=bg, fg=fg, font=fnt).grid(row=9, column=0)
    # Label(top, image=im).pack()
    txtuser = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svuser).grid(row=0,column=2)
    txtfname = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svfname).grid(row=3,column=2)
    txtlname = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svlname).grid(row=5,column=2)
    txtpass = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svpass).grid(row=7,column=2)
    txtrname = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svrname).grid(row=9,column=2)
    txtmail = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svmail).grid(row=11,column=2)
    txtphone = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svphone).grid(row=13,column=2)
    #txtprofile = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svprofile).grid(row=15,column=2)
    btns = ttk.Style()
    Button(frame, text='<-Back',bg="white",height="3",width="10").grid(row=20, column=0, pady=20,padx=10)

    Button(frame, text='update',bg="white",height="1",width="5").grid(row=0, column=4, pady=20,padx=10)
    Button(frame, text='update',bg="white",height="1",width="5").grid(row=3, column=4, pady=20,padx=10)
    Button(frame, text='update',bg="white",height="1",width="5").grid(row=5, column=4, pady=20,padx=10)
    Button(frame, text='update',bg="white",height="1",width="5").grid(row=7, column=4, pady=20,padx=10)
    Button(frame, text='update',bg="white",height="1",width="5").grid(row=9, column=4, pady=20,padx=10)
    Button(frame, text='update',bg="white",height="1",width="5").grid(row=11, column=4, pady=20,padx=10)
    Button(frame, text='update',bg="white",height="1",width="5").grid(row=13, column=4, pady=20,padx=10)


def page6():

    frm = tk.Tk()
    fnt = ('tahoma', 16)
    bg = '#ffffff'
    bgtxt = '#00ff00'
    fg = '#000000'
    fw = 700
    fh = 600
    x = (frm.winfo_screenwidth() - fw) / 2
    y = (frm.winfo_screenheight() - fh) / 2 - 50
    frm.geometry('%dx%d+%d+%d' % (fw, fh, x, y))
    frm.title('New Board')
    frm.config(bg=bg)
    idboard = StringVar()
    B = tk.Button(frm, text="Enter", bg="white", height="3", width="15", font="15",command=page7)
    B.grid(row=3, column=4, sticky=W, padx=80, pady=10)
    Label(frm, text='board name:', bg="white", fg=fg, font=" impact 25").grid(row=0, column=2)

    x = ttk.Entry(frm, textvariable=idboard)
    x.config(font=fnt)
    x.grid(row=2, column=2)
    # C= tk.Button(frm, text="Name of board", bg="white", height="6", width="40", font="40").grid(row = 0, column = 1, sticky = W,padx=100,pady=20)
    back = tk.Button(frm, text=" <- Back ", bg="white", height="3", width="10", font="100").grid(row=3, column=0,sticky=W, padx=10,pady=30)
    frm.mainloop()




def page7():
    frm = tk.Tk()
    frm.forget()
    fnt = ('tahoma', 16)
    bg = '#ffffff'
    bgtxt = '#00ff00'
    fg = '#000000'
    fw = 700
    fh = 600
    x = (frm.winfo_screenwidth() - fw) / 2
    y = (frm.winfo_screenheight() - fh) / 2 - 50
    frm.geometry('%dx%d+%d+%d' % (fw, fh, x, y))
    frm.title('add pic in new board')
    frm.config(bg=bg)
    Button(frm, text="+", bg="white", height="10", width="20", font="100").grid(row=1, column=1, sticky=W, padx=60,pady=20)
    Button(frm, text="+", bg="white", height="10", width="20", font="100").grid(row=1, column=4, sticky=W, padx=90,pady=20)
    Button(frm, text="+", bg="white", height="10", width="20", font="100").grid(row=2, column=1, sticky=W, padx=60,pady=50)
    Button(frm, text="+", bg="white", height="10", width="20", font="100").grid(row=2, column=4, sticky=W, padx=90,pady=100)
    Button(frm, text="Save", bg="white", height="3", width="10", font="100").grid(row=3, column=4, sticky=W, padx=170,pady=20)
    back = tk.Button(frm, text=" <- Back ", bg="white", height="3", width="10", font="100",command=page6).grid(row=3, column=0,sticky=W, padx=20,pady=20)

    frm.mainloop()

#page6()



def page11():
    frm = tk.Tk()
    fnt = ('tahoma', 16)
    bg = '#ffffff'
    bgtxt = '#00ff00'
    fg = '#000000'
    fw = 700
    fh = 600
    x = (frm.winfo_screenwidth() - fw) / 2
    y = (frm.winfo_screenheight() - fh) / 2 - 50
    idboard = StringVar()
    frm.geometry('%dx%d+%d+%d' % (fw, fh, x, y))
    frm.title('new pic ')
    Label(frm, text='name of image:', bg="white", fg=fg, font=" impact 25").grid(row=0, column=2)
    frm.config(bg=bg)
    lbl = ttk.Label(frm, text='name of the pic?')
    lbl.config(font=fnt)
    x = ttk.Entry(frm, textvariable=idboard)
    x.config(font=fnt)
    x.grid(row=1, column=2)

    Label(frm, text='add voice:', bg="white", fg=fg, font=" impact 25").grid(row=2, column=2)

    x1 = ttk.Entry(frm, textvariable=idboard)
    x1.config(font=fnt)
    x1.grid(row=3, column=2)
    Button(frm, text="Add pic ", bg="white", height="10", width="20", font="100").grid(row=4, column=2, sticky=W,padx=90, pady=60)

    back = tk.Button(frm, text=" <- Back ", bg="white", height="3", width="10", font="100").grid(row=5, column=0,sticky=W, padx=20,  pady=20)


def page1_admin():
    global m
    page3 = tk.Tk()
    m=Frame(page3)
    #frm.forget()
    fnt = ('tahoma', 16)
    bg = '#ffffff'
    bgtxt = '#00ff00'
    fg = '#000000'
    fw = 900
    fh = 800
    text='an fatye,cmcmdlcmdsl'
    Button(page3, text="Search an User", bg="white", height="5", width="20", font="25",command=page2_admin).grid(row=2, column=1, sticky=W, padx=30,pady=50)
    Button(page3, text="Add a new board", bg="white", height="5", width="20", font="25").grid(row=2, column=3, sticky=W, padx=30,pady=50)
    Button(page3, text="Add a new Catigoria", bg="green", height="5", width="20", font="25").grid(row=3, column=1, sticky=W, padx=30,pady=20)
    Button(page3, text="Update the page explain ", bg="white", height="5", width="20", font="25",command=explain).grid(row=3, column=2, sticky=W, padx=30,pady=20)
    #Button(page3, text="Birthday", bg="green", height="5", width="20", font="25").grid(row=3, column=3, sticky=W, padx=30,pady=20)
    #Button(frm, text="Delete an user ", bg="green", height="5", width="20", font="25").grid(row=4, column=2, sticky=W, padx=30, pady=20)
    Button(page3, text="My design ", bg="green", height="5", width="20", font="25").grid(row=2, column=2, sticky=W, padx=30, pady=50)
    back = tk.Button(page3, text=" <- Back ", bg="white", height="3", width="10", font="100").grid(row=5, column=1,sticky=W, padx=20,pady=20)
    page3.mainloop()
def explain():
    explainpage= tk.Tk()

    fnt = ('tahoma', 30)
    fw = 900
    fh = 800
    x = (explainpage.winfo_screenwidth() - fw) / 2
    y = (explainpage.winfo_screenheight() - fh) / 2 - 50
    explainpage.geometry('%dx%d+%d+%d' % (fw, fh, x, y))

    explainpage.config(bg="white")
    Label(explainpage, text='enter your new explain', bg=bg, fg=fg, font=fnt).grid(row=0, column=0)
    m=Entry(explainpage, bg="white", fg=fg, font=fnt)
    m.grid(row=10, column=2, padx=30,pady=120)
    Button(explainpage, text="Ok", bg="green", height="5", width="20", font="25",command=lambda :HelpFunc(m.get())).grid(row=2, column=2, sticky=W,
                                                                                         padx=30, pady=50)





def page2_admin():
    global r,m
    def funAzr():
        text=r.get()
        if checkuser(text) == True:
            #page3_admin()
            page4_admin()
            #page5_admin()

        if checkuser(text) == False:
            messagebox.showinfo('', 'Not found user!')




    page2 = tk.Tk()
    # frm.forget()
    fnt = ('tahoma', 16)
    bg = '#ffffff'
    bgtxt = '#00ff00'
    fg = '#000000'
    page2.config(bg=bg)
    Label(page2, text='Enter username you want to search:', bg=bg, fg=fg, font=fnt).grid(row=10, column=1, padx=30,pady=120)
    r=Entry(page2, bg="white", fg=fg, font=fnt,textvariable=svuser)
    r.grid(row=10, column=2, padx=30,pady=120)


    Button(page2, text=" Search", bg="white", height="1", width="8", font="15", command=funAzr).grid(row=14,column=4,sticky=W, padx=30, pady=30)
    page2.mainloop()


def page4_admin():
    page4 = tk.Tk()
    # frm.forget()
    fnt = ('tahoma', 16)
    bg = '#ffffff'
    bgtxt = '#00ff00'
    fg = '#000000'
    fw = 900
    fh = 800
    text1 = "Happy Birthday ya qalbiy :) "
    page4.config(bg=bg)
    Button(page4, text="Delete an user", bg="white", height="5", width="20", font="25",command=lambda :delete_user(r.get())).grid(row=3, column=1, sticky=W, padx=30, pady=20)
    Button(page4, text="Wish a Happy Birthday", bg="white", height="5", width="20", font="25",command=lambda :update_massage(text1,r.get())).grid(row=5, column=1, sticky=W, padx=30,pady=20)
    Button(page4, text="Send A massage ", bg="white", height="5", width="20", font="25",command=page5_admin).grid(row=7, column=1, sticky=W,padx=30, pady=20)

    page4.mainloop()
def page5_admin():
    page5 = tk.Tk()
    # frm.forget()
    fnt = ('tahoma', 16)
    bg = '#ffffff'
    bgtxt = '#00ff00'
    fg = '#000000'
    page5.config(bg=bg)
    Label(page5, text='Enter your massage thats you want to send to user ', bg=bg, fg=fg, font=fnt).grid(row=10, column=1, padx=30,pady=120)
    m=Entry(page5, bg="white", fg=fg, font=fnt,textvariable=svmassage)
    m.grid(row=10, column=2, padx=30,pady=120)
    Button(page5, text="Send", bg="white", height="1", width="8", font="15", command=lambda :update_massage(m.get(),r.get())).grid(row=14,column=4,sticky=W, padx=30, pady=30)
    #messagebox.showinfo('', 'The massage send!')


    page5.mainloop()












page8()
#sign_up()
#page1_admin()
'''#page5()

#page9()
#page11()
#page7()
#page6()'''

