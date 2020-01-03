
import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime

def Database():
    global conn, cursos
    conn = sqlite3.connect("admins.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS admins (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, first_name TEXT,last_name TEXT)")
    cursor.execute("INSERT INTO admins (username,password,first_name,last_name) VALUES(?,?,?,?)",("shathab","shatha12","shatha","Abu_arar"))
    cursor.execute("INSERT INTO admins (username,password,first_name,last_name) VALUES(?,?,?,?)",("israaqw","israa12","israa","Abu_qweder"))
    cursor.execute("INSERT INTO admins (username,password,first_name,last_name) VALUES(?,?,?,?)",("fatmekh","fatma12","fatma","khateeb"))
    cursor.execute("INSERT INTO admins (username,password,first_name,last_name) VALUES(?,?,?,?)",("safaaz","safaa12","safaa","alzbarqa"))
    cursor.execute("CREATE TABLE IF NOT EXISTS users (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, first_name TEXT, last_name TEXT, id TEXT,responsible_name TEXT,Email Text,user_name TEXT, password TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS boards(mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT,id TEXT)")
    conn.commit()

Database()

def insert_user(first_name,last_name,id,responsible_name,Email,user_name,password):
    cursor.execute("INSERT INTO users (first_name,last_name,id,responsible_name,Email,user_name,password) VALUES(?,?,?,?,?,?,?,?)",(first_name,last_name,id,responsible_name,responsible_id,Email,user_name,password))
    conn.commit()

    def insert_board(name, id):
        cursor.execute("INSERT INTO boards (name,id) VALUES(?,?)", (name, id))
        conn.commit()

def delete_user(id):
    cursor.execute("DELETE FROM 'users' WHERE id=?",(id,))
    conn.commit()



    def login():
        global loginframe
        loginframe = Frame(frm)
        Label(loginframe, text='xxx', fg="red").pack()
        loginframe.pack()

    frm = tk.Tk()
    fnt = ('tahoma', 16)
    bg = '#ffffff'
    bgtxt = '#00ff00'
    fg = '#000000'
    fw = 700
    fh = 500
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

    def insertdata():
        print("Hello!")

    def create():
        print(svuser.get())

        if svuser.get().strip() == '':
            messagebox.showinfo('', 'The number of id is Empty!')
            txtuser.focus()
        if svId.get().strip() == '':
            messagebox.showinfo('', 'The number of id is Empty!')
            txtid.focus()
        elif svfname.get().strip() == '':
            messagebox.showinfo('', 'The first name of the autistic is Empty!')
            txtfname.focus()
        elif svlname.get().strip() == '':
            messagebox.showinfo('', 'The last name of the autistic is Empty!')
            txtlname.focus()
        elif svgender == '':
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
        else:
            insertdata()
            svId.set('')
            svfname.set('')
            svlname.set('')
            svgender.set('')
            svrname.set('')
            svmail.set('')
            frame.destroy()
            login()

    def sign_up():
        global frame, txtuser, txtid, txtfname, txtlname, txtpass, txtgender, txtrname, txtmail, txtphone
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

        txtuser = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svuser)
        txtid = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svId)
        txtfname = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svfname)
        txtlname = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svlname)
        txtpass = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svpass)
        txtgender = ttk.Combobox(frame, values=('Male', 'Female'), state='readonly')
        txtrname = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svrname)
        txtmail = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svmail)
        txtphone = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svphone)

        btns = ttk.Style()
        btns.configure('TButton', font=fnt, pady=pad, padding=pad)
        ttk.Button(frame, text='Create user file Now', command=create).grid(row=9, column=1, pady=pad)
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

        frame.pack(pady=pad)

    def logout(frame):
        # Save in Data Base()
        svuser.set('')
        svpass.set('')
        frame.destroy()
        login()

    sign_up()
    frm.mainloop()
    input('press enter to exit...')




