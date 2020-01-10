from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from tkinter import filedialog
import datetime

'''
def login():
    global loginframe
    loginframe = Frame(frm)
    Label(loginframe, text='xxx', fg="red").pack()
    loginframe.pack()
'''

frm = tk.Tk()
fnt = ('tahoma', 16)
bg = '#ffffff'
bgtxt = '#00ff00'
fg = '#000000'
fw = 700
fh = 600
x = (frm.winfo_screenwidth() - fw) / 2
y = (frm.winfo_screenheight() - fh) / 2 - 50
pad = 10

frm.geometry('%dx%d+%d+%d' % (fw, fh, x, y))
frm.title('Users')
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
svanswer=StringVar()

def Database():
    global conn, cursor
    conn = sqlite3.connect("Accept.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS admins (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, first_name TEXT,last_name TEXT, massage TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS users (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, first_name TEXT, last_name TEXT, id TEXT,responsible_name TEXT,Email Text,user_name TEXT, password TEXT,phone TEXT,gander TEXT,massage TEXT,profile BLOB NOT NULL,answer TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS boards(mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT,id TEXT)")
    conn.commit()
Database()



'''
    if x==txtanswer.get():
        returnpass()
    else:
        messagebox.showinfo('', 'The answer is not right!')
        txtanswer.set('')
        txtanswer.focus()
'''
'''     
def insert_user(user_name,id,first_name,last_name,password,gander,responsible_name,Email,phone,answer):
    cursor.execute("INSERT INTO users (first_name,last_name,id,responsible_name,Email,user_name,password,gander,phone,answer) VALUES(?,?,?,?,?,?,?,?,?,?)",(first_name,last_name,id,responsible_name,Email,user_name,password,gander,phone,answer))
    conn.commit()
'''
def insert_board(name, id):
    cursor.execute("INSERT INTO boards (name,id) VALUES(?,?)", (name, id))
    conn.commit()

def delete_user(id):
    cursor.execute("DELETE FROM 'users' WHERE id=?",(id,))
    conn.commit()
def create():
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
    #elif svprofile.get().strip()=='':
       # messagebox.showinfo('', 'The profile is Empty!')
    elif svanswer.get().strip()=='':
        messagebox.showinfo('', 'The answer to the question is Empty!')
        txtanswer.focus()
    else:
        insert_user(svuser.get(),svId.get(),svfname.get(),svlname.get(),svpass.get(),svgender.get(),svrname.get(),svmail.get(),svphone.get(),svanswer.get())
        svId.set('')
        svfname.set('')
        svlname.set('')
        svgender.set('')
        svrname.set('')
        svmail.set('')
        svprofile.set('')
        svanswer.set('')
        frame.destroy()
        login()


def sign_up():
    global frame, txtuser, txtid, txtfname, txtlname, txtpass, txtgender, txtrname, txtmail, txtphone,txtprofile,txtanswer
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
    Label(frame, text='what your Primary School? ', bg=bg, fg=fg, font=fnt).grid(row=9, column=0)

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
    txtanswer=Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svanswer)

    btns = ttk.Style()
    btns.configure('TButton', font=fnt, pady=pad, padding=pad)
    ttk.Button(frame, text='Create user file Now', command=create).grid(row=10, column=1, pady=pad)
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
    txtanswer.grid(row=10,column=1,pady=pad)

    frame.pack(pady=pad)


def logout(frame):
    # Save in Data Base()
    svuser.set('')
    svpass.set('')
    frame.destroy()
    login()
'''
def Database():
    global conn, cursor
    conn = sqlite3.connect("Accept.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS admins (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, first_name TEXT,last_name TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS users (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, first_name TEXT, last_name TEXT, id TEXT,responsible_name TEXT,Email Text,user_name TEXT, password TEXT,phone TEXT,gander text,profile BLOB,answer TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS boards(mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT,id TEXT)")
    conn.commit()

Database()
'''
def insert_user(user_name,id,first_name,last_name,password,gander,responsible_name,Email,phone,profile,answer):
    cursor.execute("INSERT INTO users (first_name,last_name,id,responsible_name,Email,user_name,password,gander,phone,profile,answer) VALUES(?,?,?,?,?,?,?,?,?,?,?)",(first_name,last_name,id,responsible_name,Email,user_name,password,gander,phone,profile,answer,))
    conn.commit()

def insert_board(name, id):
    cursor.execute("INSERT INTO boards (name,id) VALUES(?,?)", (name, id))
    conn.commit()

def delete_user(id):
    cursor.execute("DELETE FROM 'users' WHERE id=?",(id,))
    conn.commit()

def delete_board(id):
    cursor.execute("DELETE FROM 'boards' WHERE id=?",(id,))
    conn.commit()

def update_information_user(name,last_name,password,user_name,email,responsible_name,phone):
    cursor.execute("UPDATE 'users' SET first_name=?,last_name=?,password=?,user_name=?,Email=?,responsible_name=?,phone=?",(name,last_name,password,user_name,email,responsible_name,phone))
    conn.commit()


def account():
    global a
    a=Frame(frm)
    
    def forget():
        a.forget()
        
           
        def returnpass():
            forgetframe.forget()
            global newpassframe
            newpassframe = Frame(frm)
            def checkpass():

                if txtnew.get()==txt2.get():
                    newpassframe.forget()    
                    account()
                else:
                    messagebox.showinfo('', 'The passwords not matched!')
                    txtnew.focus()
                    txt2.focus() 
            Label(newpassframe,text='New Password',font='impact 25').pack()

            frm.geometry('600x400')
            lblnew=ttk.Label(newpassframe,text='Enter new password:')
            txtnew=ttk.Entry(newpassframe)
            lbl2=ttk.Label(newpassframe,text='Enter the password one more time:')
            txt2=ttk.Entry(newpassframe)
            change=ttk.Button(newpassframe,text='change password',command=checkpass)

            lblnew.config(font=fnt)
            txtnew.config(font=fnt)
            lbl2.config(font=fnt)
            txt2.config(font=fnt)

            lblnew.pack()
            txtnew.pack()
            lbl2.pack()
            txt2.pack()
            change.pack()
            newpassframe.pack()
    
        

        def question():
            global forgetframe
            forgetframe = Frame(frm)
            def forgetpass():
        
                cursor.execute("SELECT * FROM 'users' ")
                rows=cursor.fetchall()
                for i in rows:
                    if txtid.get()==i[3] and txtanswer.get()==i[12]:
                        returnpass()
                        print(txtanswer.get())
            Label(forgetframe,text='Account security',font='impact 25').pack()

            lbl1=ttk.Label(forgetframe,text='your id:')
            lbl=ttk.Label(forgetframe,text='what your primry school?')

            txtanswer=ttk.Entry(forgetframe)
            txtanswer.config(font=fnt)
            txtid=ttk.Entry(forgetframe)
            txtid.config(font=fnt)
            lbl1.config(font=fnt)
            lbl.config(font=fnt)
    
            ok=ttk.Button(forgetframe,text='OK',command=forgetpass)

            lbl1.pack()
            txtid.pack()
            lbl.pack()
            txtanswer.pack()
            ok.pack()
            forgetframe.pack()
        question()

 
    
    def login():
        a.forget()
        global loginFrame
        loginFrame=Frame(frm)
        def check():
            cursor.execute("select * from 'users' where user_name=(?) and password=(?) ",(txtname.get(),txtpass.get()))
            print(txtname.get(),txtpass.get())
            if cursor.fetchone() is None:
                 messagebox.showinfo('', 'Invalid Username or password!')
                 txtname.focus()
                 txtpass.focus() 
            else:
                print(4)
                

        lblname=ttk.Label(loginFrame,text='Enter username:')
        txtname=ttk.Entry(loginFrame)
        lblpass=ttk.Label(loginFrame,text='Enter the password:')
        txtpass=ttk.Entry(loginFrame)

            
        txtname.config(font=fnt)
        txtpass.config(font=fnt)
        lblname.config(font=fnt)
        lblpass.config(font=fnt)
    
        login=ttk.Button(loginFrame,text='login',command=check)

        lblname.pack()
        txtname.pack()
        lblpass.pack()
        txtpass.pack()
        login.pack()
        loginFrame.pack()

    def f():
        Label(a,text="Choose Login Or Register", bg="blue", width="300")
        Label(a,text="").pack()
        Button(a,text="Login",height="2",width="30",command=login).pack()
        Label(a,text="").pack()
        Button(a,text="Register",height="2",width="30",command=sign_up).pack()
        Button(a,text="forget",height="2",width="30",command=forget).pack()
        Label(a,text="").pack()
        a.pack()
    f()






def login():
    global loginFrame
    loginFrame=Frame(frm)
    a=Label(loginFrame,text='',fg='red')
    a.grid(row=0,column=2, pady=20)
    Label(loginFrame,text="Enter user name:").grid(row=1,column=1)
    Entry(loginFrame,textvariable=svuser).grid(row=1,column=2)
    Label(loginFrame, text="Enter password:").grid(row=2, column=1)
    Entry(loginFrame, textvariable=svpass).grid(row=2,column=2)
    Button(loginFrame, text='login',height="2",width="30",command=lambda: check).grid(row=3, column=2, pady=20)
    loginFrame.pack()
#<<<<<<< HEAD



# كود الصورر

'''top=Tk()
top.geometry('1000x600')
image=filedialog.askopenfilename(filetypes=[("Image File",'.png')])
#print(image.split('/')[-1::][0])
conn = sqlite3.connect("Accept.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS pic (name TEXT)")
cursor.execute("INSERT INTO pic (name)VALUES (?)",(image.split('/')[-1::][0],))
conn.commit()
im=PhotoImage(file=image)
top.mainloop()'''
#=======
#>>>>>>> f6276ef1b32f148412718f5262ebf3cb265dccd0

#account()

#frm.mainloop()


#<<<<<<< HEAD




account()

def main_page():
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
    frm.title('Users')
    frm.config(bg=bg)
    B = tk.Button(frm, text="Board", bg="white", height="6", width="30", font="40").grid(row=0, column=1, pady=20)
    # B.pack()
    C = tk.Button(frm, text=" NEW Board", bg="white", height="6", width="30", font="30").grid(row=2, column=1, pady=20)
    # C.pack()
    A = tk.Button(frm, text="Setting", bg="white", height="6", width="30", font="30").grid(row=4, column=1, pady=20)
    # A.pack()
    #frm.iconbitmap('icon.ico')
    frm.mainloop()

frm.mainloop()
#=======
#>>>>>>> f6276ef1b32f148412718f5262ebf3cb265dccd0
