
import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
from playsound import playsound
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from tkinter import filedialog
from PIL import ImageTk, Image
import sqlite3
import numpy as np
import io
from builtins import bytes

import datetime

frame=None
catDic = {}
cat1Dic = {}
photonameList = []
lista = []
photoDic = {}
bordDic = {}
photonameList1 = []
photo1Dic = {}

'''
im1=StringVar()
im2=StringVar()
im3=StringVar()
im4=StringVar()
imi=''

ica=StringVar()

image_names={'im1':im1,'im2':im2,'im3':im3,'im4':im4}

bo1=StringVar()

bords_names={'ob1':bo1}

'''


def login():
    global loginframe
    loginframe = Frame(frm)
    Label(loginframe, text='xxx', fg="red").pack()
    loginframe.pack()


def acceptEng():
    print("eng")


def acceptArab():
    print("arab")


def acceptHeb():
    print("heb")


frm = tk.Tk()

fnt = ('tahoma', 16)
bg = '#ffffff'
bgtxt = '#00ff00'
fg = '#000000'
fw = 1000
fh = 700
x = (frm.winfo_screenwidth() - fw) / 2
y = (frm.winfo_screenheight() - fh) / 2 - 50
pad = 10

frm.geometry('%dx%d+%d+%d' % (fw, fh, x, y))
# frm.title('Users')
frm.config(bg=bg)
im1 = StringVar()
im2 = StringVar()
im3 = StringVar()
im4 = StringVar()
imi = ''

svuser = StringVar()
svId = StringVar()
svfname = StringVar()
svlname = StringVar()
svpass = StringVar()
svgender = StringVar()
svrname = StringVar()
svmail = StringVar()
svphone = StringVar()

# svprofile = StringVar()
svanswer = StringVar()
svmassage = StringVar()
svlan = StringVar()


def acceptArab():

    def Database():
        global conn, cursor
        conn = sqlite3.connect("Accept2.db")
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS admins (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, first_name TEXT,last_name TEXT, massage TEXT)")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, first_name TEXT, last_name TEXT, id TEXT,responsible_name TEXT,Email Text,user_name TEXT, password TEXT,phone TEXT,gander TEXT,massage TEXT,answer TEXT,nameprofile TEXT,dataprofile TEXT)")
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS boards(name text,nameim1 text,sound1 blob,image1 text,nameim2 text,sound2 blob,image2 text,nameim3 text,sound3 blob,image3 text,nameim4 text,sound4 blob,image4 text,username text) ')
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS category(name text,c1name text,image1 text,c2name text,image2 text,c3name text,image3 text,c4name text,image4 text,c5name text,image5 text,c6name text,image6 text) ')
        conn.commit()

    Database()
    # cursor.execute("DROP TABLE users;")

    '''
    cursor.execute("INSERT INTO admins (username,password,first_name,last_name) VALUES(?,?,?,?)", ('shatha26','sh','shatha','arar'))
    conn.commit()
    '''
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
        cursor.execute("DELETE FROM 'users' WHERE id=?", (id,))
        conn.commit()

    '''
    def create():
        global i
        if i.get()==0:
            insert_user(txtuser.get(), txtid.get(), txtfname.get(), txtlname.get(), txtpass.get(), txtgender.get(),txtrname.get(), txtmail.get(), txtphone.get(),txtanswer.get())
        else:
            messagebox.showinfo('', "يجب عليك الموافقه على شروط البرمجه")

            '''
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
       txtphone.set('')

       #frame.destroy()


    def sign_up():
        global frame, txtuser, txtid, txtfname, txtlname, txtpass, txtgender, txtrname, txtmail, txtphone,txtprofile,txtmassage
        frame = Frame(frm, bg=bg)
        # Label(frame, text='User Data', bg='navy', fg='lightblue', font=fnt).pack(pady=pad)

        Label(frame, text='اسم المستخدم:', bg=bg, fg=fg, font=fnt).grid(row=0, column=0)
        Label(frame, text='نمرة هوية المتوحد:', bg=bg, fg=fg, font=fnt).grid(row=1, column=0)
        Label(frame, text='الاسم الاول  :', bg=bg, fg=fg, font=fnt).grid(row=2, column=0)
        Label(frame, text='الاسم الثاني :', bg=bg, fg=fg, font=fnt).grid(row=3, column=0)
        Label(frame, text='كلمة السر :', bg=bg, fg=fg, font=fnt).grid(row=4, column=0)
        Label(frame, text='جنس المستخدم: ', bg=bg, fg=fg, font=fnt).grid(row=5, column=0)
        Label(frame, text='اسم المسؤول  :', bg=bg, fg=fg, font=fnt).grid(row=6, column=0)
        Label(frame, text='ايميل المسؤول :', bg=bg, fg=fg, font=fnt).grid(row=7, column=0)
        Label(frame, text='رقم هاتف المسؤول :', bg=bg, fg=fg, font=fnt).grid(row=8, column=0)

        #Label(frame, text='الصوره الشخصيه :', bg=bg, fg=fg, font=fnt).grid(row=9, column=0)
        #Label(top, image=im).pack()
        txtuser = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svuser)
        txtid = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svId)
        txtfname = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svfname)
        txtlname = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svlname)
        txtpass = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svpass)
        txtgender = ttk.Combobox(frame, values=('ذكر', 'انثى'),textvariable=svgender, state='readonly')
        txtrname = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svrname)
        txtmail = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svmail)
        txtphone = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svphone)
        txtprofile=Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svprofile)
        btns = ttk.Style()
        btns.configure('TButton', font=fnt, pady=pad, padding=pad)
        #c = Checkbutton(frame, text="موافق ", variable="unchecked", onvalue="checked").grid(row=11, column=0, pady=pad)
        #ttk.Button(frame, text='Create', command=create).grid(row=13, column=3, pady=pad)
        ttk.Button(frame, text='رجوع').grid(row=13, column=0, pady=8)
        ttk.Button(frame, text='استمر',command=pageif).grid(row=13, column=3, pady=8)
        # ttk.Button(frm, text='الخروج', command=frm.destroy).grid(row=9, column=2, pady=pad)

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
    '''
    i = IntVar()

    def logout(frame):
        # Save in Data Base()
        svuser.set('')
        svpass.set('')
        frame.destroy()

    def insert_user(user_name, id, first_name, last_name, password, Email, responsible_name, gander, phone, answer,
                    nameprofile, dataprofile):
        cursor.execute(
            "INSERT INTO users (first_name,last_name,id,responsible_name,Email,user_name,password,gander,phone,answer,nameprofile,dataprofile) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
            (
            first_name, last_name, id, responsible_name, Email, user_name, password, gander, phone, answer, nameprofile,
            dataprofile))
        conn.commit()

    def insert_board(name, id):
        cursor.execute("INSERT INTO boards (name,id) VALUES(?,?)", (name, id))
        conn.commit()

    def delete_user(id):
        cursor.execute("DELETE FROM 'users' WHERE id=?", (id,))

    def delete_user(username):
        cursor.execute("DELETE FROM 'users' WHERE user_name=?", (username,))
        conn.commit()

    def delete_board(nameB):
        cursor.execute("DELETE FROM 'boards' WHERE name=?", (nameB,))
        conn.commit()

    def update_massage(massage, username):
        cursor.execute("UPDATE 'users' SET massage=? WHERE user_name=?", (massage, username))
        conn.commit()

    imageNameInasert = {'im1name': None, 'im2name': None, 'im3name': None, 'im4name': None}

    imageToInsert = {'im1': None, 'im2': None, 'im3': None, 'im4': None}

    imageNameInasertc = {'im1name': None, 'im2name': None, 'im3name': None, 'im4name': None, 'im5name': None,
                         'im6name': None}

    imageToInsertc = {'im1': None, 'im2': None, 'im3': None, 'im4': None, 'im5': None, 'im6': None}
    exp = 0

    def convertTbinary(key, name):
        a = open(name, 'rb')
        imageNameInasert[key + 'name'] = name

        imageToInsert[key] = a.read()

    isShow1 = None

    def convertToimage(name, imager):
        if (name != None):
            b = open(name, 'wb')
            b.write(imager)
            photonameList.append(name)
            photoDic[name] = PhotoImage(file=name)

    isShow2 = None

    def account():
        global isShow
        isShow = Frame(frm)

        def updatepro():
            def upusername():
                cursor.execute("UPDATE 'users' SET user_name=? WHERE id=? ", (svuser.get(), id))
                conn.commit()
                print(77)

            def upfname():
                cursor.execute("UPDATE 'users' SET first_name=? WHERE id=? ", (svfname.get(), id))
                conn.commit()
                print(88)

            def uplname():
                cursor.execute("UPDATE 'users' SET last_name=? WHERE id=? ", (svlname.get(), id))
                conn.commit()

            def uppass():
                cursor.execute("UPDATE 'users' SET password=? WHERE id=? ", (svpass.get(), id))
                conn.commit()

            def uprname():
                cursor.execute("UPDATE 'users' SET responsible_name=? WHERE id=? ", (svrname.get(), id))
                conn.commit()

            def upphone():
                cursor.execute("UPDATE 'users' SET phone=? WHERE id=? ", (svphone.get(), id))
                conn.commit()

            def upmail():
                cursor.execute("UPDATE 'users' SET Email=? WHERE id=? ", (svmail.get(), id))
                conn.commit()

            # settingframe.forget()
            global isShow
            isShow = Frame(frm)
            Label(isShow, text='اسم المستخدم:', bg=bg, fg=fg, font=fnt).grid(row=0, column=0, pady=20)
            Label(isShow, text='نمرة هوية المتوحد :', bg=bg, fg=fg, font=fnt).grid(row=3, column=0,
                                                                                                pady=20)
            Label(isShow, text='الاسم الاول :', bg=bg, fg=fg, font=fnt).grid(row=5, column=0,
                                                                                               pady=20)
            Label(isShow, text='كلمة السر:', bg=bg, fg=fg, font=fnt).grid(row=7, column=0, pady=20)
            Label(isShow, text='اسم السمؤول :', bg=bg, fg=fg, font=fnt).grid(row=9, column=0, pady=20)
            Label(isShow, text='البريد الالكتروني الخاص بالمسؤول :', bg=bg, fg=fg, font=fnt).grid(row=11, column=0,
                                                                                               pady=20)
            Label(isShow, text='رقم الهاتف الخاص بالمسؤول :', bg=bg, fg=fg, font=fnt).grid(row=13, column=0,
                                                                                                     pady=20)
            # Label(frame, text='The profile of the Autistic :', bg=bg, fg=fg, font=fnt).grid(row=9, column=0)
            # Label(top, image=im).pack()
            Entry(isShow, bg=bgtxt, fg=fg, font=fnt, textvariable=svuser).grid(row=0, column=2)
            Entry(isShow, bg=bgtxt, fg=fg, font=fnt, textvariable=svfname).grid(row=3, column=2)
            Entry(isShow, bg=bgtxt, fg=fg, font=fnt, textvariable=svlname).grid(row=5, column=2)
            Entry(isShow, bg=bgtxt, fg=fg, font=fnt, textvariable=svpass).grid(row=7, column=2)
            Entry(isShow, bg=bgtxt, fg=fg, font=fnt, textvariable=svrname).grid(row=9, column=2)
            Entry(isShow, bg=bgtxt, fg=fg, font=fnt, textvariable=svmail).grid(row=11, column=2)
            Entry(isShow, bg=bgtxt, fg=fg, font=fnt, textvariable=svphone).grid(row=13, column=2)
            # txtprofile = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svprofile).grid(row=15,column=2)
            Button(isShow, text='<-رجوع', bg="white", height="3", width="10", command=settingpage).grid(row=20,
                                                                                                        column=0,
                                                                                                        pady=20,
                                                                                                        padx=10)
            Button(isShow, text='تحديث', bg="white", height="1", width="5", command=upusername).grid(row=0, column=4,
                                                                                                      pady=20, padx=10)
            Button(isShow, text='تحديث', bg="white", height="1", width="5", command=upfname).grid(row=3, column=4,
                                                                                                   pady=20,
                                                                                                   padx=10)
            Button(isShow, text='تحديث', bg="white", height="1", width="5", command=uplname).grid(row=5, column=4,
                                                                                                   pady=20,
                                                                                                   padx=10)
            Button(isShow, text='تحديث', bg="white", height="1", width="5", command=uppass).grid(row=7, column=4,
                                                                                                  pady=20,
                                                                                                  padx=10)
            Button(isShow, text='تحديث', bg="white", height="1", width="5", command=uprname).grid(row=9, column=4,
                                                                                                   pady=20,
                                                                                                   padx=10)
            Button(isShow, text='تحديث', bg="white", height="1", width="5", command=upmail).grid(row=11, column=4,
                                                                                                  pady=20,
                                                                                                  padx=10)
            Button(isShow, text='تحديث', bg="white", height="1", width="5", command=upphone).grid(row=13, column=4,
                                                                                                   pady=20, padx=10)

            isShow.grid()
            isShow.mainloop()

        def create():
            global i
            if i.get() == 0:
                insert_user(txtfname.get(), txtlname.get(), txtid.get(), txtrname.get(), txtmail.get(), txtuser.get(),
                            txtpass.get(), txtgender.get(), txtphone.get(), txtanswer.get(), np, dp)
            else:
                messagebox.showinfo('', "يجب عليك الموافقه على شروط الاستخدام")

        def HelpFunc2():
            global isShow
            isShow.forget()
            isShow = Frame(frm)
            Label(isShow, text=exp, bg=bg, fg=fg, font=fnt).grid(row=2, column=2)

            isShow.pack()

        def HelpFunc(texthelp):
            global isShow
            isShow.forget()
            isShow = Frame(frm)
            Label(isShow, text='الشرح الخاص بك هو :', bg=bg, fg=fg, font=fnt).grid(row=3, column=0, pady=20)
            Label(isShow, text=exp, bg=bg, fg=fg, font=fnt).grid(row=5, column=0, pady=20)

            isShow.mainloop()

        def pageif():
            if svuser.get().strip() == '':
                messagebox.showinfo('', 'اسم المستخدم فارغ')
                txtuser.focus()
            elif svId.get().strip() == '':
                messagebox.showinfo('', 'رقم الهويه فارغ!')
                txtid.focus()
            elif svpass.get().strip() == '':
                messagebox.showinfo('', 'كلمة المرور فارغه!')
                txtpass.focus()
            elif svfname.get().strip() == '':
                messagebox.showinfo('', 'الاسم الاول فارغ!')
                txtfname.focus()
            elif svlname.get().strip() == '':
                messagebox.showinfo('', 'الاسم الثاني فارغ')
                txtlname.focus()
            elif svgender.get() == '':
                messagebox.showinfo('', 'الجنس فارغ!')
                txtgender.focus()
            elif svrname.get().strip() == '':
                messagebox.showinfo('', 'اسم المسؤول فارغ!')
                txtrname.focus()
            elif svmail.get().strip() == '':
                messagebox.showinfo('', 'البريد الالكتروني الخاص بالمسؤول فارغ!')
                txtmail.focus()
            elif svphone.get().strip() == '':
                messagebox.showinfo('', 'رقم الهاتف الخاص بالمسؤول فارغ!')
                txtphone.focus()
            # elif svprofile.get().strip()=='':
            # messagebox.showinfo('', 'The profile is Empty!')
            else:
                global isShow
                isShow.forget()
                isShow = Frame(frm)
                ttt = 'the Termos:\n • Not allowed > upload disturbing images\n •Not allowed to extract audio > that has unsuitable words.\n• The system should be used correctly.\n• Allow managers to control my account.\n• Confirmation of saving my personal information in the system'

                Label(isShow, text=ttt, bg=bg, fg=fg, font=fnt).grid(row=0, column=0)
                c = Checkbutton(isShow, text="اوافق ", variable=i, onvalue="checked").grid(
                    row=11, column=0, pady=pad)
                Button(isShow, text='تسجيل', command=create).grid(row=13, column=3, pady=pad)
                isShow.mainloop()

        def sendmess():
            global isShow
            isShow.forget()
            isShow = Frame(frm)

            def send():
                cursor.execute("UPDATE admins SET massage=?", (svmassage.get(),))
                conn.commit()
                mainpage()

            Label(isShow, text="اكتب رساله:", font=fnt).grid(row=1, column=1)
            Entry(isShow, font=fnt, textvariable=svmassage).grid(row=2, column=1)
            Button(isShow, text="ارسل", bg="white", height="3", width="10", font=fnt, command=send).grid(row=4,
                                                                                                         column=2,
                                                                                                         padx=100,
                                                                                                         pady=20)
            Button(isShow, text="<- رجوع", bg="white", height="3", width="10", font="10", command=settingpage).grid(
                row=4, column=0, padx=5, pady=80)
            isShow.pack()

        def lang():
            global isShow, svlan
            isShow.forget()
            isShow = Frame(frm)

            def chooslan():
                if svlan.get() == 'English':
                    acceptEng()
                elif svlan.get() == 'Arabic':
                    acceptArab()
                elif svlan.get() == 'Hebrew':
                    acceptHeb()

            txtlan = ttk.Combobox(isShow, values=('English', 'Arabic', 'Hebrew'), textvariable=svlan,
                                  state='readonly').grid(row=1, column=1, pady=pad)
            Button(isShow, text="اختار", bg="white", height="3", width="10", font="10", command=chooslan()).grid(
                row=3, column=1, padx=5, pady=80)
            Button(isShow, text="<- رجوع", bg="white", height="3", width="10", font="10", command=settingpage).grid(
                row=4, column=0, padx=5, pady=80)
            isShow.pack()

        def settingpage():
            global isShow
            isShow.forget()
            isShow = Frame(frm)

            Button(isShow, text="لغه", bg="white", height="6", width="30", font=fnt, command=lambda: lang()).grid(
                row=4, column=1,
                padx=100, pady=20)
            Button(isShow, text="اتصل", bg="white", height="6", width="30", font=fnt, command=sendmess).grid(row=6,
                                                                                                                column=1,
                                                                                                                padx=100,
                                                                                                                pady=20)
            Button(isShow, text="مساعده!", bg="white", height="6", width="30", font="50", command=HelpFunc2).grid(row=2,
                                                                                                                column=1,
                                                                                                                padx=100,
                                                                                                                pady=20)
            # Button(isShow, text="Edit Profile", bg="white", height="6", width="30", font="50",command=updatepro).grid(row=0, column=1, padx=100, pady=20)
            Button(isShow, text="<- رجوع", bg="white", height="3", width="10", font="10", command=mainpage).grid(
                row=8, column=0, padx=5, pady=80)

            isShow.pack()

        def sign_up():
            isShow.forget()
            global frame, txtuser, txtid, txtfname, txtlname, txtpass, txtgender, txtrname, txtmail, txtphone, txtprofile, txtanswer
            frame = Frame(frm, bg=bg)
            # Label(frame, text='User Data', bg='navy', fg='lightblue', font=fnt).pack(pady=pad)

            Label(frame, text='اسم المستخدم:', bg=bg, fg=fg, font=fnt).grid(row=0, column=0)
            Label(frame, text='رقم هوية الستخدم:', bg=bg, fg=fg, font=fnt).grid(row=1, column=0)
            Label(frame, text='الاسم الاول :', bg=bg, fg=fg, font=fnt).grid(row=2, column=0)
            Label(frame, text='الاسم الثاني :', bg=bg, fg=fg, font=fnt).grid(row=3, column=0)
            Label(frame, text='كلمة المرور :', bg=bg, fg=fg, font=fnt).grid(row=4, column=0)
            Label(frame, text='جنس المستخدم: ', bg=bg, fg=fg, font=fnt).grid(row=5, column=0)
            Label(frame, text='اسم المسؤول :', bg=bg, fg=fg, font=fnt).grid(row=6, column=0)
            Label(frame, text='البريد الالكتروتي الخاص بالمسؤول :', bg=bg, fg=fg, font=fnt).grid(row=7, column=0)
            Label(frame, text='رقم الهاتف الخاص بالمسؤول :', bg=bg, fg=fg, font=fnt).grid(row=8, column=0)
            Label(frame, text='اسم مدرستك الابتدائيه? ', bg=bg, fg=fg, font=fnt).grid(row=9, column=0)

            # Label(frame, text='The profile of the Autistic :', bg=bg, fg=fg, font=fnt).grid(row=9, column=0)
            # Label(top, image=im).pack()
            txtuser = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svuser)
            txtid = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svId)
            txtfname = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svfname)
            txtlname = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svlname)
            txtpass = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svpass)
            txtgender = ttk.Combobox(frame, values=('Male', 'Female'), textvariable=svgender, state='readonly')
            txtrname = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svrname)
            txtmail = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svmail)
            txtphone = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svphone)
            # txtprofile = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svprofile)
            txtanswer = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svanswer)

            btns = ttk.Style()
            btns.configure('TButton', font=fnt, pady=pad, padding=pad)
            ttk.Button(frame, text='الصوره الشخصيه',
                       command=lambda: saveprofile(filedialog.askopenfilename(filetypes=[("Image File", '.png')]))) \
                .grid(row=10, column=0, pady=15)
            # ttk.Button(frame, text='Create new account', command=create).grid(row=11, column=1, pady=pad)
            # ttk.Button(frm, text='Exit Now', command=frm.destroy).grid(row=9, column=2, pady=pad)
            ttk.Button(frame, text='الرجوع', command=f).grid(row=13, column=0, pady=8)
            ttk.Button(frame, text='استمر', command=pageif).grid(row=13, column=3, pady=8)
            txtuser.grid(row=0, column=1, pady=pad)
            txtid.grid(row=1, column=1, pady=pad)
            txtfname.grid(row=2, column=1, pady=pad)
            txtlname.grid(row=3, column=1, pady=pad)
            txtpass.grid(row=4, column=1, pady=pad)
            txtgender.grid(row=5, column=1, pady=pad)
            txtrname.grid(row=6, column=1, pady=pad)
            txtmail.grid(row=7, column=1, pady=pad)
            txtphone.grid(row=8, column=1, pady=pad)
            txtanswer.grid(row=9, column=1, pady=pad)

            frame.pack(pady=pad)

        def saveprofile(name):
            global np, dp
            a = open(name, 'rb')
            np = name
            dp = a.read()

        def convp():
            cursor.execute("SELECT * FROM users WHERE user_name=?", (svuser.get(),))
            row = cursor.fetchall()
            for i in row:
                name = i[12]
                imager = i[13]
            global ddp
            if (name != None):
                b = open(name, 'wb')
                b.write(imager)
                ddp = PhotoImage(file=name)
                return ddp

            print(5)

        def newbord():
            print(1)
            isShow.forget()

            def insertimag(num):
                def choosepic(num):
                    def choose(key, name):
                        convertTbinary(key, name)
                        isShow1.destroy()

                    def allcat():

                        def funcB(N, K):
                            print(N)

                            def lastFuncc():

                                '''print(numImg)
                                root = Tk()
                                canvas = Canvas(root, width=300, height=300)
                                canvas.pack()
                                im = Image.open(numImg)
                                resized = im.resize((200, 200), Image.ANTIALIAS)
                                photo1 = ImageTk.PhotoImage(resized)
                                myvar = tk.Button(root, image=photo1)
                                myvar.image = photo1
                                myvar.pack()
                                root.mainloop()

                                global isShow
                                isShow=Frame(frm)
                                isShow=imageToInsert['im1']
                            '''

                                def convertToimage(name, imager):
                                    if (name != None):
                                        b = open(name, 'wb')
                                        b.write(imager)
                                        photonameList1.append(name)
                                        photo1Dic[name] = PhotoImage(file=name)

                                global imageNameInasertc
                                cursor.execute("SELECT * FROM category WHERE name=?", (N,))
                                y = cursor.fetchall()
                                for n in y:
                                    for i in range(1, 13, 2):
                                        convertToimage(n[i], n[i + 1])
                                print(photo1Dic)
                                for i in y:
                                    print(i[0])
                                    Fram(N, i[2], i[4], i[6], i[8], i[10], i[12], i[1], i[3], i[5], i[7], i[9], i[11])

                            def Fram(name, data1, data2, data3, data4, data5, data6, image1=None, image2=None,
                                     image3=None, image4=None, image5=None, image6=None):

                                global isShow2, catDic
                                isShow2.forget()
                                isShow2 = Frame(isShow1)
                                print(image1)
                                Label(isShow2, text=name).grid(row=0, columnspan=2, pady=20)
                                print(photo1Dic)
                                if image1:
                                    b = Button(isShow2, height="300", width="300", image=photo1Dic[image1],
                                               command=lambda: choose('im' + str(num), image1))
                                    b.grid(row=1, column=0)
                                if image2:
                                    c = Button(isShow2, height="300", width="300", image=photo1Dic[image2],
                                               command=lambda: choose('im' + str(num), image2))
                                    c.grid(row=1, column=1)
                                if image3:
                                    d = Button(isShow2, height="300", width="300", image=photo1Dic[image3],
                                               command=lambda: choose('im' + str(num), image3))
                                    d.grid(row=1, column=2)
                                if image4:
                                    t = Button(isShow2, height="300", width="300", image=photo1Dic[image4],
                                               command=lambda: choose('im' + str(num), image4))
                                    t.grid(row=2, column=0)
                                if image5:
                                    t = Button(isShow2, height="300", width="300", image=photo1Dic[image5],
                                               command=lambda: choose('im' + str(num), image5))
                                    t.grid(row=2, column=1)
                                if image6:
                                    t = Button(isShow2, height="300", width="300", image=photo1Dic[image6],
                                               command=lambda: choose('im' + str(num), image6))
                                    t.grid(row=2, column=2)
                                Button(isShow2, text="<- رجوع", bg="white", height="3", width="10", font="10",
                                       command=allcat).grid(
                                    row=3, column=0, padx=5, pady=80)
                                # if name in tuple(cat1Dic):
                                # cat1Dic[name].append(isShow2)
                                #### and insert to DB
                                # else:
                                # cat1Dic[name] = isShow2
                                # isShow2 = cat1Dic[name]
                                # print(cat1Dic)
                                isShow2.pack()

                            C = Button(isShow2, text=N, bg="white", height="3", width="15", font="20",
                                       command=lambda: lastFuncc())
                            C.bind('<Button-1>', lambda event, frame=isShow2, arg=N: bord(N))
                            C.grid(row=K, column=1, padx=30, pady=20)

                        global isShow2, row
                        isShow2.forget()

                        isShow2 = Frame(isShow1)

                        cursor.execute("SELECT * FROM category")
                        row = cursor.fetchall()
                        k = 0

                        for i in row:
                            funcB(i[0], k)
                            k += 1
                            '''
                            b=Button(isShow, text=y, bg="white", height="3", width="15", font="20")
                            b.bind('<Button-1>', lambda event, frame=isShow, arg=y: bord(y))
                            b.grid(row=k, column=1, padx=30, pady=20)
                            k+=1
                            '''
                        Button(isShow, text="<- رجوع", bg="white", height="3", width="10", font="10",
                               command=mainpage).grid(
                            row=k, column=0, padx=5, pady=80)

                        isShow2.pack()

                    global isShow2, isShow1

                    isShow1 = tk.Toplevel()
                    isShow2 = Frame(isShow1)

                    def comp():
                        global isShow2
                        convertTbinary('im' + str(num), filedialog.askopenfilename(filetypes=[("Image File", '.png')]))
                        isShow1.destroy()
                        insertimag(num)

                    def cat():
                        global isShow2
                        isShow2.forget()
                        allcat()

                    Button(isShow2, text="فئات", bg="white", height="5", width="20", font="25", command=cat).grid(
                        row=2, column=2, sticky=W, padx=30, pady=50)
                    Button(isShow2, text="من الحاسوب", bg="white", height="5", width="20", font="25",
                           command=comp).grid(row=3, column=2, sticky=W, padx=30, pady=50)
                    Button(isShow, text="<- رجوع", bg="white", height="3", width="10", font="10",
                           command=lambda: insertimag(num)).grid(
                        row=4, column=0, padx=5, pady=80)
                    isShow2.pack()

                def funcVoice(name):

                    fs = 44100  # Sample rate
                    seconds = 3  # Duration of recording
                    print("seeey")
                    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
                    sd.wait()  # Wait until recording is finished
                    file = name
                    write(file, fs, myrecording)  # Save as WAV file
                    global vvo
                    vvo = file
                    # playsound(file)

                def saveimb():
                    global isShow

                    # print(imageToInsert['im1'])
                    # isShow.forget()
                    if num == 1:
                        cursor.execute("UPDATE 'boards' SET nameim1=?,sound1=?,image1=? WHERE name=? ",
                                       (imageNameInasert['im1name'], vvo, imageToInsert['im1'], txtbord.get()))
                        conn.commit()
                    elif num == 2:
                        cursor.execute("UPDATE 'boards' SET nameim2=?,sound2=?,image2=? WHERE name=? ",
                                       (imageNameInasert['im2name'], vvo, imageToInsert['im2'], txtbord.get()))
                        conn.commit()
                    elif num == 3:
                        cursor.execute("UPDATE 'boards' SET nameim3=?,sound3=?,image3=? WHERE name=? ",
                                       (imageNameInasert['im3name'], vvo, imageToInsert['im3'], txtbord.get()))
                        conn.commit()
                    elif num == 4:
                        cursor.execute("UPDATE 'boards' SET nameim4=?,sound4=?,image4=? WHERE name=? ",
                                       (imageNameInasert['im4name'], vvo, imageToInsert['im4'], txtbord.get()))
                        conn.commit()
                    isShow.forget()
                    creatbord()

                    # for n in imageToInsert:
                    # convertToimage(imageNameInasert['im1' + 'name'], imageToInsert['im1'])
                    # Fram(name, imageNameInasert['im1name'])
                    # imageNameInasert['im1name'] = None
                    # ChooseBordOrCat()
                    # catDic[name][0].pack()
                    # isShow=catDic[name][0]

                global isShow
                isShow.forget()
                isShow = Frame(frm)
                Label(isShow, text='اسم الصوره:', bg="white", fg=fg, font=" impact 25").grid(row=0, column=2)
                lbl = ttk.Label(isShow, text='اسم الصوره?')
                lbl.config(font=fnt)
                nameim = ttk.Entry(isShow)
                nameim.config(font=fnt)
                nameim.grid(row=1, column=2)

                Button(isShow, text="اضف صوت ", bg="white", height="5", width="10", font="20",
                       command=lambda: funcVoice("x" + str(num) + txtbord.get() + ".wav")).grid(row=2,
                                                                                                column=2,
                                                                                                sticky=W,
                                                                                                padx=90,
                                                                                                pady=60)

                Button(isShow, text="سجل صوت ", bg="white", height="5", width="10", font="20",
                       command=lambda: choosepic(num)).grid(row=4, column=2, sticky=W, padx=90, pady=60)
                ok = tk.Button(isShow, text=" حفظ"
                                            " ", bg="white", height="3", width="5", font="20",
                               command=saveimb).grid(row=5, column=1, sticky=W, padx=20, pady=20)
                back = tk.Button(isShow, text=" <- رجوع ", bg="white", height="3", width="5", font="20",
                                 command=newbord).grid(row=5,
                                                       column=0,
                                                       sticky=W,
                                                       padx=20,
                                                       pady=20)

                isShow.pack()

            def setImage(im, namecat):
                global imi, isShow
                counter = 0
                isShow.forget()
                imi = im
                isShow = catDic[namecat][counter]
                isShow.pack()

            def save_B():
                cursor.execute("SELECT * FROM admins")
                x = cursor.fetchall()
                for i in x:
                    if svuser.get() == i[1]:
                        cursor.execute("INSERT INTO boards (name,username) VALUES(?,?)", (txtbord.get(), "everyone"))
                        conn.commit()
                        creatbord()
                        return
                cursor.execute("INSERT INTO boards (name,username) VALUES(?,?)", (txtbord.get(), svuser.get()))
                conn.commit()
                creatbord()

            def creatbord():
                def adminoruser():
                    cursor.execute("SELECT * FROM admins")
                    x = cursor.fetchall()
                    for i in x:
                        if svuser.get() == i[1]:
                            page1_admin()
                            return
                    mainpage()

                global isShow
                isShow.forget()
                isShow = Frame(frm)

                # cursor.execute("INSERT INTO boards (name) VALUES(?)", (txtbord.get(),))
                # conn.commit()
                Button(isShow, text="+1", bg="white", height="10", width="20", font="100",
                       command=lambda: insertimag(1)).grid(row=1, column=1, sticky=W, padx=60, pady=20)
                Button(isShow, text="+2", bg="white", height="10", width="20", font="100",
                       command=lambda: insertimag(2)).grid(row=1, column=4, sticky=W, padx=90, pady=20)
                Button(isShow, text="+3", bg="white", height="10", width="20", font="100",
                       command=lambda: insertimag(3)).grid(row=2, column=1, sticky=W, padx=60, pady=50)
                Button(isShow, text="+4", bg="white", height="10", width="20", font="100",
                       command=lambda: insertimag(4)).grid(row=2, column=4, sticky=W, padx=90, pady=100)
                Button(isShow, text="Save", bg="white", height="3", width="10", font="100",
                       command=lambda: adminoruser()).grid(row=3, column=4, sticky=W, padx=170, pady=20)
                back = tk.Button(isShow, text=" <- Back ", bg="white", height="3", width="10", font="100",
                                 command=namebord).grid(row=3, column=0, sticky=W, padx=20, pady=20)

                isShow.pack()

            def namebord():
                global isShow, txtbord
                isShow.forget()
                print(2)
                print(3)
                isShow = Frame(frm)
                B = ttk.Button(isShow, text="ادخل", command=save_B)
                Label(isShow, text='اسم اللوح:', font=fnt).pack()
                print(4)
                txtbord = ttk.Entry(isShow)
                txtbord.config(font=fnt)

                print(5)
                txtbord.pack()
                B.pack()

                Button(isShow, text="<- رجوع", bg="white", height="3", width="10", font="10", command=mainpage).pack()
                isShow.pack()
                # mainframe.pack()

            namebord()

        def bord(z):

            print(z)

            def voice(num):

                for i in row:
                    if i[0] == z:
                        if num == 3:
                            playsound(i[2])
                        elif num == 6:
                            playsound(i[5])
                        elif num == 9:
                            playsound(i[8])
                        elif num == 12:
                            playsound(i[11])

            # print(row)

            '''
            global isShow
            isShow.forget()
            isShow = Frame(frm)
            cursor.execute("SELECT * FROM boards WHERE name=?", (z,))
            row = cursor.fetchall()
            for i in row:
                j = 1
                print(i)
                lastFunc(i[3], 3)

                b1=Button(isShow, bg="white", height="10", width="20", font="100", image=i[3],command=lambda: voice(1)).grid(row=1, column=1, sticky=W, padx=60, pady=20)
                b2=Button(isShow, bg="white", height="10", width="20", font="100", image=i[6],command=lambda: voice(2)).grid(row=1, column=4, sticky=W, padx=90, pady=20)
                b3=Button(isShow, bg="white", height="10", width="20", font="100", image=i[9],command=lambda: voice(3)).grid(row=2, column=1, sticky=W, padx=60, pady=50)
                b4=Button(isShow, bg="white", height="10", width="20", font="100", image=i[12],command=lambda: voice(4)).grid(row=2, column=4, sticky=W, padx=90, pady=100)
                # Button(bordframe, text="Save", bg="white", height="3", width="10", font="100").grid(row=3, column=4,sticky=W, padx=170,pady=20)
                back = tk.Button(isShow, text=" <- Back ", bg="white", height="3", width="10", font="100",command=lambda: allboards()).grid(row=3,column=0,sticky=W,padx=20,pady=20)

                b1.image=convertToimage('name1.txt', i[3])
                b2.image=convertToimage('name2.txt', i[6])
                b3.image=convertToimage('name3.txt', i[9])
                b4.image=convertToimage('name4.txt', i[12])
                '''
            isShow.pack()

        def allboards():

            def funcB(N, K):
                print(N)

                def lastFunc():

                    '''print(numImg)
                    root = Tk()
                    canvas = Canvas(root, width=300, height=300)
                    canvas.pack()
                    im = Image.open(numImg)
                    resized = im.resize((200, 200), Image.ANTIALIAS)
                    photo1 = ImageTk.PhotoImage(resized)
                    myvar = tk.Button(root, image=photo1)
                    myvar.image = photo1
                    myvar.pack()
                    root.mainloop()

                    global isShow
                    isShow=Frame(frm)
                    isShow=imageToInsert['im1']
                '''
                    global imageNameInasert
                    cursor.execute("SELECT * FROM boards WHERE name=?", (N,))
                    y = cursor.fetchall()
                    for n in y:
                        for i in range(1, 11, 3):
                            convertToimage(n[i], n[i + 2])
                    print(photoDic)
                    cursor.execute("SELECT * FROM boards WHERE name=?", (N,))
                    x = cursor.fetchall()
                    for i in x:
                        print(i[0])
                        Fram(N, i[1], i[4], i[7], i[10])
                    imageNameInasert['im1name'], imageNameInasert['im2name'], imageNameInasert['im3name'], \
                    imageNameInasert[
                        'im4name'] = None, None, None, None

                def Fram(name, image1=None, image2=None, image3=None, image4=None):
                    def voice(num):
                        cursor.execute("SELECT * FROM boards WHERE name=?", (name,))
                        vo = cursor.fetchall()
                        for i in vo:
                            if i[0] == name:
                                if num == 1:
                                    playsound(i[2])
                                elif num == 2:
                                    playsound(i[5])
                                elif num == 3:
                                    playsound(i[8])
                                elif num == 4:
                                    playsound(i[11])

                    global isShow, catDic
                    isShow.forget()
                    isShow = Frame(frm)
                    print(image1)
                    Label(isShow, text=name).grid(row=0, columnspan=2, pady=20)
                    print(photoDic)
                    if image1:
                        b = Button(isShow, height="400", width="400", image=photoDic[image1], command=lambda: voice(1))
                        b.grid(row=1, column=0)
                    if image2:
                        c = Button(isShow, height="400", width="400", image=photoDic[image2], command=lambda: voice(2))
                        c.grid(row=1, column=1)
                    if image3:
                        d = Button(isShow, height="400", width="400", image=photoDic[image3], command=lambda: voice(3))
                        d.grid(row=2, column=0)
                    if image4:
                        t = Button(isShow, height="400", width="400", image=photoDic[image4], command=lambda: voice(4))
                        t.grid(row=2, column=1)
                    Button(isShow, text="<-رجوع", bg="white", height="3", width="10", font="10",
                           command=allboards).grid(
                        row=3, column=0, padx=5, pady=80)
                    if name in tuple(catDic):
                        catDic[name].append(isShow)
                        #### and insert to DB
                    else:
                        catDic[name] = isShow
                    isShow = catDic[name]
                    print(catDic)
                    isShow.pack()

                C = Button(isShow, text=N, bg="white", height="3", width="15", font="20", command=lambda: lastFunc())
                C.bind('<Button-1>', lambda event, frame=isShow, arg=N: bord(N))
                C.grid(row=K, column=1, padx=30, pady=20)

            global isShow, row
            isShow.forget()

            isShow = Frame(frm)

            cursor.execute("SELECT * FROM boards")
            row = cursor.fetchall()
            k = 0

            for i in row:
                if i[13] == svuser.get() or i[13] == "everyone":
                    funcB(i[0], k)
                    k += 1
                '''
                b=Button(isShow, text=y, bg="white", height="3", width="15", font="20")
                b.bind('<Button-1>', lambda event, frame=isShow, arg=y: bord(y))
                b.grid(row=k, column=1, padx=30, pady=20)
                k+=1
                '''
            Button(isShow, text="<- رجوع", bg="white", height="3", width="10", font="10", command=mainpage).grid(
                row=k, column=0, padx=5, pady=80)
            isShow.pack()

        def mainpage():

            global isShow
            isShow.forget()
            isShow = Frame(frm)
            '''
            create=ttk.Button(mainframe,text='Create a new board!',command= newbord)
            exi=ttk.Button(mainframe,text='An existing boards')
            setting=ttk.Button(mainframe,text='setting')
            profile=ttk.Button(mainframe,text='profile')
            profile.pack()
            create.pack()
            exi.pack()
            setting.pack()

            '''
            cursor.execute("SELECT * FROM users WHERE user_name=?", (svuser.get(),))
            row = cursor.fetchall()
            for i in row:
                proimg = i[12]
            # create = ttk.Button(mainframe, text='Create a new board!')

            Label(isShow, bg="white", font=fnt, height=200, width=200, image=convp()).grid(row=2, column=1, padx=300,
                                                                                           pady=10)
            Button(isShow, text="اعدادات", bg="white", font=fnt, command=settingpage).grid(row=8, column=1, padx=300,
                                                                                           pady=10)
            Button(isShow, text="اصنع لوح جديد!", bg="white", font=fnt, command=newbord).grid(row=6, column=1,
                                                                                                   padx=300, pady=10)
            Button(isShow, text="الالواح الموجوده", bg="white", font=fnt, command=allboards).grid(row=4, column=1,
                                                                                                    padx=200, pady=10)
            # Button(mainframe, text="Profile", bg="white", font=fnt).grid(row=0, column=1, padx=200, pady=20)

            isShow.pack()

        def forget():
            global isShow
            isShow.forget()

            def returnpass():
                global isShow
                isShow.forget()
                isShow = Frame(frm)

                def checkpass():

                    if txtnew.get() == txt2.get():
                        account()
                    else:
                        messagebox.showinfo('', 'كلمة المرور غير صحيحه!')
                        txtnew.focus()
                        txt2.focus()

                Label(isShow, text='كلمة مرور جديده', font='impact 25').pack()

                lblnew = ttk.Label(isShow, text='ادخل كلمة مرور جديده:')
                txtnew = ttk.Entry(isShow)
                lbl2 = ttk.Label(isShow, text='ادخل كلمة مرور للتاكير:')
                txt2 = ttk.Entry(isShow)
                change = ttk.Button(isShow, text='تبديل كلمة المرور', command=checkpass)
                Button(isShow, text="<- رجوع", bg="white", height="3", width="10", font="10", command=question).grid(
                    row=4, column=0, padx=5, pady=80)
                lblnew.config(font=fnt)
                txtnew.config(font=fnt)
                lbl2.config(font=fnt)
                txt2.config(font=fnt)

                lblnew.pack()
                txtnew.pack()
                lbl2.pack()
                txt2.pack()
                change.pack()
                isShow.pack()

            def question():
                global isShow
                isShow.forget()
                isShow = Frame(frm)

                def forgetpass():

                    cursor.execute("SELECT * FROM 'users' ")
                    rows = cursor.fetchall()
                    for i in rows:
                        if txtid.get() == i[3] and txtanswer.get() == i[12]:
                            returnpass()
                            print(txtanswer.get())

                Label(isShow, text='امن الحساب', font='impact 25').pack()

                lbl1 = ttk.Label(isShow, text='رقم هويتك:')
                lbl = ttk.Label(isShow, text='ما هي مدرستك الابتدائيه?')

                txtanswer = ttk.Entry(isShow)
                txtanswer.config(font=fnt)
                txtid = ttk.Entry(isShow)
                txtid.config(font=fnt)
                lbl1.config(font=fnt)
                lbl.config(font=fnt)
                Button(isShow, text="<- رجوع", bg="white", height="3", width="10", font="10", command=login).grid(
                    row=4, column=0, padx=5, pady=80)
                ok = ttk.Button(isShow, text='OK', command=forgetpass)

                lbl1.pack()
                txtid.pack()
                lbl.pack()
                txtanswer.pack()
                ok.pack()
                isShow.pack()

            question()

        def checkuser(name):

            cursor.execute("select * from 'users' where user_name=? ", (name,))
            if cursor.fetchone() is not None:
                return True
            return False

        def page2_admin():
            global r, isShow

            def funAzr():
                text = r.get()
                if checkuser(text) == True:
                    # page3_admin()
                    page4_admin()
                    # page5_admin()

                if checkuser(text) == False:
                    messagebox.showinfo('', 'اسم المستخدم غير موجود!')

            isShow.forget()
            isShow = Frame(frm)
            Label(isShow, text='ادخل اسم المستخدم اللذي تريد البجث عنه:', bg=bg, fg=fg, font=fnt).grid(row=10, column=1,
                                                                                                  padx=30,
                                                                                                  pady=120)
            r = Entry(isShow, bg="white", fg=fg, font=fnt, textvariable=svuser)
            r.grid(row=10, column=2, padx=30, pady=120)

            Button(isShow, text=" ابحث", bg="white", height="1", width="8", font="15", command=funAzr).grid(row=14,
                                                                                                              column=4,
                                                                                                              sticky=W,
                                                                                                              padx=30,
                                                                                                              pady=30)
            Button(isShow, text="<- رجوع", bg="white", height="3", width="10", font="10", command=page1_admin).grid(
                row=14, column=0, padx=5, pady=80)
            isShow.mainloop()

        def adminbord():
            global isShow
            isShow.forget()
            isShow = Frame(frm)
            Button(isShow, text="اظافة لوح جديد", bg="white", height="5", width="20", font="25", command=newbord).grid(
                row=2,
                column=2,
                sticky=W,
                padx=30,
                pady=50)
            Button(isShow, text="كل الالواح", bg="white", height="5", width="20", font="25", command=allboards).grid(
                row=3,
                column=2,
                sticky=W,
                padx=30,
                pady=50)
            Button(isShow, text="<- رجوع", bg="white", height="3", width="10", font="10", command=page1_admin).grid(
                row=4, column=0, padx=5, pady=80)
            isShow.pack()

        def allcat():

            def funcB(N, K):
                print(N)

                def lastFuncc():

                    '''print(numImg)
                    root = Tk()
                    canvas = Canvas(root, width=300, height=300)
                    canvas.pack()
                    im = Image.open(numImg)
                    resized = im.resize((200, 200), Image.ANTIALIAS)
                    photo1 = ImageTk.PhotoImage(resized)
                    myvar = tk.Button(root, image=photo1)
                    myvar.image = photo1
                    myvar.pack()
                    root.mainloop()

                    global isShow
                    isShow=Frame(frm)
                    isShow=imageToInsert['im1']
                '''

                    def convertToimage(name, imager):
                        if (name != None):
                            b = open(name, 'wb')
                            b.write(imager)
                            photonameList1.append(name)
                            photo1Dic[name] = PhotoImage(file=name)

                    global imageNameInasertc
                    cursor.execute("SELECT * FROM category WHERE name=?", (N,))
                    y = cursor.fetchall()
                    for n in y:
                        for i in range(1, 13, 2):
                            convertToimage(n[i], n[i + 1])
                    print(photo1Dic)
                    for i in y:
                        print(i[0])
                        Fram(N, i[1], i[3], i[5], i[7], i[9], i[11])
                    imageNameInasert['im1name'], imageNameInasert['im2name'], imageNameInasert['im3name'], \
                    imageNameInasert[
                        'im4name'] = None, None, None, None

                def Fram(name, image1=None, image2=None, image3=None, image4=None, image5=None, image6=None):

                    global isShow, catDic
                    isShow.forget()
                    isShow = Frame(frm)
                    print(image1)
                    Label(isShow, text=name, height="10", width="20", ).grid(row=0, columnspan=2, pady=20)
                    print(photo1Dic)
                    if image1:
                        b = Button(isShow, height="300", width="300", image=photo1Dic[image1])
                        b.grid(row=1, column=0)
                    if image2:
                        c = Button(isShow, height="300", width="300", image=photo1Dic[image2])
                        c.grid(row=1, column=1)
                    if image3:
                        d = Button(isShow, height="300", width="300", image=photo1Dic[image3])
                        d.grid(row=1, column=2)
                    if image4:
                        t = Button(isShow, height="300", width="300", image=photo1Dic[image4])
                        t.grid(row=2, column=0)
                    if image5:
                        t = Button(isShow, height="300", width="300", image=photo1Dic[image5])
                        t.grid(row=2, column=1)
                    if image6:
                        t = Button(isShow, height="300", width="300", image=photo1Dic[image6])
                        t.grid(row=2, column=2)
                    Button(isShow, text="<- رجوع", bg="white", height="3", width="10", font="10",
                           command=allcat).grid(
                        row=3, column=0, padx=5, pady=80)
                    if name in tuple(cat1Dic):
                        cat1Dic[name].append(isShow)
                        #### and insert to DB
                    else:
                        cat1Dic[name] = isShow
                    isShow = cat1Dic[name]
                    print(cat1Dic)
                    isShow.pack()

                C = Button(isShow, text=N, bg="white", height="3", width="15", font="20", command=lambda: lastFuncc())
                C.bind('<Button-1>', lambda event, frame=isShow, arg=N: bord(N))
                C.grid(row=K, column=1, padx=30, pady=20)

            global isShow, row
            isShow.forget()

            isShow = Frame(frm)

            cursor.execute("SELECT * FROM category")
            row = cursor.fetchall()
            k = 0

            for i in row:
                funcB(i[0], k)
                k += 1
                '''
                b=Button(isShow, text=y, bg="white", height="3", width="15", font="20")
                b.bind('<Button-1>', lambda event, frame=isShow, arg=y: bord(y))
                b.grid(row=k, column=1, padx=30, pady=20)
                k+=1
                '''
            Button(isShow, text="<- رجوع", bg="white", height="3", width="10", font="10", command=admincat).grid(
                row=k, column=0, padx=5, pady=80)

            isShow.pack()

        def newcat():

            def saveimc(num):
                if num == 1:
                    cursor.execute("UPDATE 'category' SET c1name=?,image1=? WHERE name=? ",
                                   (imageNameInasertc['im1name'], imageToInsertc['im1'], txtcat.get()))
                    conn.commit()
                elif num == 2:
                    cursor.execute("UPDATE 'category' SET c2name=?,image2=? WHERE name=? ",
                                   (imageNameInasertc['im2name'], imageToInsertc['im2'], txtcat.get()))
                    conn.commit()
                elif num == 3:
                    cursor.execute("UPDATE 'category' SET c3name=?,image3=? WHERE name=? ",
                                   (imageNameInasertc['im3name'], imageToInsertc['im3'], txtcat.get()))
                    conn.commit()
                elif num == 4:
                    cursor.execute("UPDATE 'category' SET c4name=?,image4=? WHERE name=? ",
                                   (imageNameInasertc['im4name'], imageToInsertc['im4'], txtcat.get()))
                    conn.commit()
                elif num == 5:
                    cursor.execute("UPDATE 'category' SET c5name=?,image5=? WHERE name=? ",
                                   (imageNameInasertc['im5name'], imageToInsertc['im5'], txtcat.get()))
                    conn.commit()
                elif num == 6:
                    cursor.execute("UPDATE 'category' SET c6name=?,image6=? WHERE name=? ",
                                   (imageNameInasertc['im6name'], imageToInsertc['im6'], txtcat.get()))
                    conn.commit()

                # for n in imageToInsert:
                # convertToimage(imageNameInasert['im1' + 'name'], imageToInsert['im1'])
                # Fram(name, imageNameInasert['im1name'])
                # imageNameInasert['im1name'] = None
                # ChooseBordOrCat()
                # catDic[name][0].pack()
                # isShow=catDic[name][0]

            def setImage(im, namecat):
                global imi, isShow
                counter = 0
                isShow.forget()
                imi = im
                isShow = catDic[namecat][counter]
                isShow.pack()

            def save_C():

                cursor.execute("INSERT INTO category (name) VALUES(?)", (txtcat.get(),))
                conn.commit()
                creatcat()

            def convertTbinaryc(key, name, num):
                a = open(name, 'rb')
                imageNameInasertc[key + 'name'] = name

                imageToInsertc[key] = a.read()
                saveimc(num)

            def creatcat():
                global isShow
                isShow.forget()
                isShow = Frame(frm)

                # cursor.execute("INSERT INTO boards (name) VALUES(?)", (txtbord.get(),))
                # conn.commit()
                Button(isShow, text="+1", bg="white", height="10", width="20", font="100",
                       command=lambda: convertTbinaryc('im' + str(1),
                                                       filedialog.askopenfilename(filetypes=[("Image File", '.png')]),
                                                       1)).grid(row=1, column=0, sticky=W, padx=60, pady=20)
                Button(isShow, text="+2", bg="white", height="10", width="20", font="100",
                       command=lambda: convertTbinaryc('im' + str(2),
                                                       filedialog.askopenfilename(filetypes=[("Image File", '.png')]),
                                                       2)).grid(row=1, column=3, sticky=W, padx=90, pady=20)
                Button(isShow, text="+3", bg="white", height="10", width="20", font="100",
                       command=lambda: convertTbinaryc('im' + str(3),
                                                       filedialog.askopenfilename(filetypes=[("Image File", '.png')]),
                                                       3)).grid(row=1, column=5, sticky=W, padx=60, pady=50)
                Button(isShow, text="+4", bg="white", height="10", width="20", font="100",
                       command=lambda: convertTbinaryc('im' + str(4),
                                                       filedialog.askopenfilename(filetypes=[("Image File", '.png')]),
                                                       4)).grid(row=2, column=0, sticky=W, padx=90, pady=100)
                Button(isShow, text="+5", bg="white", height="10", width="20", font="100",
                       command=lambda: convertTbinaryc('im' + str(5),
                                                       filedialog.askopenfilename(filetypes=[("Image File", '.png')]),
                                                       4)).grid(row=2, column=3, sticky=W, padx=90, pady=100)
                Button(isShow, text="+6", bg="white", height="10", width="20", font="100",
                       command=lambda: convertTbinaryc('im' + str(6),
                                                       filedialog.askopenfilename(filetypes=[("Image File", '.png')]),
                                                       4)).grid(row=2, column=5, sticky=W, padx=90, pady=100)

                Button(isShow, text="حفظ", bg="white", height="3", width="10", font="100",
                       command=lambda: page1_admin()).grid(row=3, column=4, sticky=W, padx=170, pady=20)
                back = tk.Button(isShow, text=" <- رجوع ", bg="white", height="3", width="10", font="100",
                                 command=namecat).grid(row=3, column=0, sticky=W, padx=20, pady=20)

                isShow.pack()

            def namecat():
                global isShow, txtcat
                isShow.forget()
                print(2)
                print(3)
                isShow = Frame(frm)
                B = ttk.Button(isShow, text="ادخل", command=save_C)
                Label(isShow, text='اسم الفئه:', font=fnt).pack()
                print(4)
                txtcat = ttk.Entry(isShow)
                txtcat.config(font=fnt)
                Button(isShow, text="<- رجوع", bg="white", height="3", width="10", font="10", command=admincat()).grid(
                    row=4, column=0, padx=5, pady=80)

                print(5)
                txtcat.pack()
                B.pack()

                back = ttk.Button(isShow, text=" <- Back ")
                back.pack()
                isShow.pack()
                # mainframe.pack()

            namecat()

        def admincat():
            global isShow
            isShow.forget()
            isShow = Frame(frm)
            Button(isShow, text="اظافة فئه جديده", bg="white", height="5", width="20", font="25",
                   command=newcat).grid(
                row=2,
                column=2,
                sticky=W,
                padx=30,
                pady=50)
            Button(isShow, text="كل الفئات ", bg="white", height="5", width="20", font="25", command=allcat).grid(
                row=3,
                column=2,
                sticky=W,
                padx=30,
                pady=50)
            Button(isShow, text="<- رجوع", bg="white", height="3", width="10", font="10", command=page1_admin).grid(
                row=4, column=0, padx=5, pady=80)
            isShow.pack()

        def addadmin():
            global isShow
            isShow.forget()
            isShow = Frame(frm)

            def add():
                cursor.execute("INSERT INTO admins (username,password,first_name,last_name) VALUES(?,?,?,?)",
                               (svuser.get(), svpass.get(), svfname.get(), svlname.get()))
                conn.commit()
                page1_admin()

            Label(isShow, text="ادخل اسم المستخدم:", font=fnt).grid(row=1, column=1)
            Entry(isShow, textvariable=svuser, font=fnt).grid(row=1, column=2)
            Label(isShow, text="ادخل كلمة المرور:", font=fnt).grid(row=2, column=1)
            Entry(isShow, textvariable=svpass, font=fnt).grid(row=2, column=2)
            Label(isShow, text="ادخل الاسم الاول:", font=fnt).grid(row=3, column=1)
            Entry(isShow, textvariable=svfname, font=fnt).grid(row=3, column=2)
            Label(isShow, text="ادخل الاسم الثاني:", font=fnt).grid(row=4, column=1)
            Entry(isShow, textvariable=svlname, font=fnt).grid(row=4, column=2)
            Button(isShow, text="اضف", bg="white", font=1, command=add).grid(row=5, column=2, padx=10, pady=10)
            Button(isShow, text="<- رجوع", bg="white", height="3", width="10", font="10", command=page1_admin).grid(
                row=6, column=0, padx=5, pady=80)
            isShow.pack()

        def page1_admin():
            global isShow
            isShow.forget()
            isShow = Frame(frm)

            Button(isShow, text="ابحث عن مستخدم", bg="white", height="5", width="20", font="25",
                   command=page2_admin).grid(
                row=2, column=1, sticky=W, padx=30, pady=50)
            Button(isShow, text="الواح", bg="white", height="5", width="20", font="25", command=adminbord).grid(row=2,
                                                                                                                 column=3,
                                                                                                                 sticky=W,
                                                                                                                 padx=30,
                                                                                                                 pady=50)
            Button(isShow, text="فئات", bg="green", height="5", width="20", font="25", command=admincat).grid(
                row=3, column=1,
                sticky=W,
                padx=30, pady=20)
            Button(isShow, text="جدث صفحة الشرح  ", bg="white", height="5", width="20", font="25",
                   command=explain).grid(row=3, column=2, sticky=W, padx=30, pady=20)
            # Button(page3, text="Birthday", bg="green", height="5", width="20", font="25").grid(row=3, column=3, sticky=W, padx=30,pady=20)
            # Button(frm, text="Delete an user ", bg="green", height="5", width="20", font="25").grid(row=4, column=2, sticky=W, padx=30, pady=20)
            Button(isShow, text="تصميمي ", bg="green", height="5", width="20", font="25").grid(row=2, column=2,
                                                                                                  sticky=W,
                                                                                                  padx=30, pady=50)
            Button(isShow, text="اضافة مشرف", bg="green", height="5", width="20", font="25", command=addadmin).grid(
                row=3, column=3, sticky=W,
                padx=30, pady=50)

            isShow.pack()

        def explain():
            global isShow
            isShow.forget
            isShow = Frame(frm)
            Label(isShow, text='ادخل شرحك', bg=bg, fg=fg, font=fnt).grid(row=0, column=0)
            m = Entry(isShow, bg="white", fg=fg, font=fnt)
            m.grid(row=10, column=2, padx=30, pady=120)
            Button(isShow, text="Ok", bg="green", height="5", width="20", font="25",
                   command=lambda: HelpFunc(m.get())).grid(row=2, column=2, sticky=W,
                                                           padx=30, pady=50)
            Button(isShow, text="<- رجوع", bg="white", height="3", width="10", font="10", command=page1_admin).grid(
                row=4, column=0, padx=5, pady=80)
            isShow.pack()

        def page4_admin():
            global isShow
            isShow.forget()
            isShow = Frame(frm)
            text1 = "Happy Birthday ya qalbiy :) "
            Button(isShow, text="حذف مستخدم", bg="white", height="5", width="20", font="25",
                   command=lambda: delete_user(r.get())).grid(row=3, column=1, sticky=W, padx=30, pady=20)
            Button(isShow, text="Happy Birthday", bg="white", height="5", width="20", font="25",
                   command=lambda: update_massage(text1, r.get())).grid(row=5, column=1, sticky=W, padx=30, pady=20)
            Button(isShow, text="ارسال رساله ", bg="white", height="5", width="20", font="25",
                   command=page5_admin).grid(
                row=7, column=1, sticky=W, padx=30, pady=20)
            Button(isShow, text="<- رجوع", bg="white", height="3", width="10", font="10", command=page1_admin).grid(
                row=7, column=0, padx=5, pady=80)

            page4.mainloop()

        def page5_admin():
            global isShow
            isShow.forget
            isShow = Frame(frm)
            Label(isShow, text='ادخل الرساله التي تريد ارسالها الى المستخدم ', bg=bg, fg=fg, font=fnt).grid(
                row=10,
                column=1,
                padx=30,
                pady=120)
            m = Entry(isShow, bg="white", fg=fg, font=fnt, textvariable=svmassage)
            m.grid(row=10, column=2, padx=30, pady=120)
            Button(isShow, text="ارسل", bg="white", height="1", width="8", font="15",
                   command=lambda: update_massage(m.get(), r.get())).grid(row=14, column=4, sticky=W, padx=30, pady=30)
            Button(isShow, text="<- رجوع", bg="white", height="3", width="10", font="10", command=page4_admin).grid(
                row=14, column=0, padx=5, pady=80)
            # messagebox.showinfo('', 'The massage send!')

        def login():

            global isShow, svuser
            isShow.forget()
            isShow = Frame(frm)

            def check():
                print(svuser.get(), svpass.get())
                cursor.execute("select * from 'users' where user_name=(?) and password=(?) ",
                               (svuser.get(), svpass.get()))
                print(svuser.get(), svpass.get())
                if cursor.fetchone() is None:
                    cursor.execute("select * from 'admins' where username=(?) and password=(?) ",
                                   (svuser.get(), svpass.get()))
                    if cursor.fetchone() is None:
                        messagebox.showinfo('', 'Invalid Username or password!')

                    else:
                        page1_admin()
                else:

                    global id
                    cursor.execute("SELECT * FROM 'users' ")
                    rows = cursor.fetchall()
                    for i in rows:
                        if svuser.get() == i[6] and svpass.get() == i[7]:
                            id = i[3]
                    isShow.forget()
                    mainpage()

            Label(isShow, text="ادخل اسم المستخدم:").grid(row=1, column=1)
            Entry(isShow, textvariable=svuser).grid(row=2, column=1)
            Label(isShow, text="ادخل كلمة المرور:").grid(row=3, column=1)
            Entry(isShow, textvariable=svpass).grid(row=4, column=1)
            '''
            lblname=ttk.Label(loginFrame,text='Enter username:').grid(row=1,column=2,padx=10,pady=10)
            txtname=ttk.Entry(loginFrame).grid(row=2,column=2,padx=10,pady=10)
            lblpass=ttk.Label(loginFrame,text='Enter the password:').grid(row=3,column=2,padx=10,pady=10)
            txtpass=ttk.Entry(loginFrame).grid(row=4,column=2,padx=10,pady=10)
    '''
            Button(isShow, text='دخول', bg="white", font=5, command=check).grid(row=5, column=1, padx=10, pady=10)
            Button(isShow, text="نسيت كلمة المرور", bg="white", font=1, command=forget).grid(row=5, column=2, padx=10,
                                                                                            pady=10)
            Button(isShow, text="<- رجوع", bg="white", height="3", width="10", font="10", command=f).grid(
                row=5, column=0, padx=5, pady=80)
            isShow.pack()

        def f():
            global isShow, frame
            if frame:
                frame.forget()
            if isShow:
                isShow.forget()
            isShow = Frame(frm)
            Label(isShow, text="Choose Login Or Register", bg="blue", width="300")
            Label(isShow, text="").pack()
            Button(isShow, text="دخول", height="2", width="30", command=login).pack()
            Label(isShow, text="").pack()
            Button(isShow, text="تسجيل", height="2", width="30", command=sign_up).pack()
            Label(isShow, text="").pack()
            isShow.pack()
            isShow.mainloop()

        f()

    account()

def acceptHeb():
    def Database():
        global conn, cursor
        conn = sqlite3.connect("Accept2.db")
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS admins (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, first_name TEXT,last_name TEXT, massage TEXT)")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, first_name TEXT, last_name TEXT, id TEXT,responsible_name TEXT,Email Text,user_name TEXT, password TEXT,phone TEXT,gander TEXT,massage TEXT,answer TEXT,nameprofile TEXT,dataprofile TEXT)")
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS boards(name text,nameim1 text,sound1 blob,image1 text,nameim2 text,sound2 blob,image2 text,nameim3 text,sound3 blob,image3 text,nameim4 text,sound4 blob,image4 text,username text) ')
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS category(name text,c1name text,image1 text,c2name text,image2 text,c3name text,image3 text,c4name text,image4 text,c5name text,image5 text,c6name text,image6 text) ')
        conn.commit()

    Database()
    # cursor.execute("DROP TABLE users;")

    '''
    cursor.execute("INSERT INTO admins (username,password,first_name,last_name) VALUES(?,?,?,?)", ('shatha26','sh','shatha','arar'))
    conn.commit()
    '''
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
        cursor.execute("DELETE FROM 'users' WHERE id=?", (id,))
        conn.commit()

    '''
    def create():
        global i
        if i.get()==0:
            insert_user(txtuser.get(), txtid.get(), txtfname.get(), txtlname.get(), txtpass.get(), txtgender.get(),txtrname.get(), txtmail.get(), txtphone.get(),txtanswer.get())
        else:
            messagebox.showinfo('', "you want to agree the terms")

            '''
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
       txtphone.set('')

       #frame.destroy()


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
    '''
    i = IntVar()

    def logout(frame):
        # Save in Data Base()
        svuser.set('')
        svpass.set('')
        frame.destroy()

    def insert_user(user_name, id, first_name, last_name, password, Email, responsible_name, gander, phone, answer,
                    nameprofile, dataprofile):
        cursor.execute(
            "INSERT INTO users (first_name,last_name,id,responsible_name,Email,user_name,password,gander,phone,answer,nameprofile,dataprofile) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
            (
            first_name, last_name, id, responsible_name, Email, user_name, password, gander, phone, answer, nameprofile,
            dataprofile))
        conn.commit()

    def insert_board(name, id):
        cursor.execute("INSERT INTO boards (name,id) VALUES(?,?)", (name, id))
        conn.commit()

    def delete_user(id):
        cursor.execute("DELETE FROM 'users' WHERE id=?", (id,))

    def delete_user(username):
        cursor.execute("DELETE FROM 'users' WHERE user_name=?", (username,))
        conn.commit()

    def delete_board(nameB):
        cursor.execute("DELETE FROM 'boards' WHERE name=?", (nameB,))
        conn.commit()

    def update_massage(massage, username):
        cursor.execute("UPDATE 'users' SET massage=? WHERE user_name=?", (massage, username))
        conn.commit()

    imageNameInasert = {'im1name': None, 'im2name': None, 'im3name': None, 'im4name': None}

    imageToInsert = {'im1': None, 'im2': None, 'im3': None, 'im4': None}

    imageNameInasertc = {'im1name': None, 'im2name': None, 'im3name': None, 'im4name': None, 'im5name': None,
                         'im6name': None}

    imageToInsertc = {'im1': None, 'im2': None, 'im3': None, 'im4': None, 'im5': None, 'im6': None}
    exp = 0

    def convertTbinary(key, name):
        a = open(name, 'rb')
        imageNameInasert[key + 'name'] = name

        imageToInsert[key] = a.read()

    isShow1 = None

    def convertToimage(name, imager):
        if (name != None):
            b = open(name, 'wb')
            b.write(imager)
            photonameList.append(name)
            photoDic[name] = PhotoImage(file=name)

    isShow2 = None

    def account():
        global isShow
        isShow = Frame(frm)

        def updatepro():
            def upusername():
                cursor.execute("UPDATE 'users' SET user_name=? WHERE id=? ", (svuser.get(), id))
                conn.commit()
                print(77)

            def upfname():
                cursor.execute("UPDATE 'users' SET first_name=? WHERE id=? ", (svfname.get(), id))
                conn.commit()
                print(88)

            def uplname():
                cursor.execute("UPDATE 'users' SET last_name=? WHERE id=? ", (svlname.get(), id))
                conn.commit()

            def uppass():
                cursor.execute("UPDATE 'users' SET password=? WHERE id=? ", (svpass.get(), id))
                conn.commit()

            def uprname():
                cursor.execute("UPDATE 'users' SET responsible_name=? WHERE id=? ", (svrname.get(), id))
                conn.commit()

            def upphone():
                cursor.execute("UPDATE 'users' SET phone=? WHERE id=? ", (svphone.get(), id))
                conn.commit()

            def upmail():
                cursor.execute("UPDATE 'users' SET Email=? WHERE id=? ", (svmail.get(), id))
                conn.commit()

            # settingframe.forget()
            global isShow
            isShow = Frame(frm)
            Label(isShow, text='שם המשתמש:', bg=bg, fg=fg, font=fnt).grid(row=0, column=0, pady=20)
            Label(isShow, text='השם הראשון של האוטיסט :', bg=bg, fg=fg, font=fnt).grid(row=3, column=0,
                                                                                                pady=20)
            Label(isShow, text='שם המשפחה:', bg=bg, fg=fg, font=fnt).grid(row=5, column=0,
                                                                                               pady=20)
            Label(isShow, text='הסיסמה:', bg=bg, fg=fg, font=fnt).grid(row=7, column=0, pady=20)
            Label(isShow, text='שם האחראי :', bg=bg, fg=fg, font=fnt).grid(row=9, column=0, pady=20)
            Label(isShow, text='אימל האחראי:', bg=bg, fg=fg, font=fnt).grid(row=11, column=0,
                                                                                               pady=20)
            Label(isShow, text='מספר הטילפון של האחראי:', bg=bg, fg=fg, font=fnt).grid(row=13, column=0,
                                                                                                     pady=20)
            # Label(frame, text='The profile of the Autistic :', bg=bg, fg=fg, font=fnt).grid(row=9, column=0)
            # Label(top, image=im).pack()
            Entry(isShow, bg=bgtxt, fg=fg, font=fnt, textvariable=svuser).grid(row=0, column=2)
            Entry(isShow, bg=bgtxt, fg=fg, font=fnt, textvariable=svfname).grid(row=3, column=2)
            Entry(isShow, bg=bgtxt, fg=fg, font=fnt, textvariable=svlname).grid(row=5, column=2)
            Entry(isShow, bg=bgtxt, fg=fg, font=fnt, textvariable=svpass).grid(row=7, column=2)
            Entry(isShow, bg=bgtxt, fg=fg, font=fnt, textvariable=svrname).grid(row=9, column=2)
            Entry(isShow, bg=bgtxt, fg=fg, font=fnt, textvariable=svmail).grid(row=11, column=2)
            Entry(isShow, bg=bgtxt, fg=fg, font=fnt, textvariable=svphone).grid(row=13, column=2)
            # txtprofile = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svprofile).grid(row=15,column=2)
            Button(isShow, text='<-חזרה', bg="white", height="3", width="10", command=settingpage).grid(row=20,
                                                                                                        column=0,
                                                                                                        pady=20,
                                                                                                        padx=10)
            Button(isShow, text='עידכון', bg="white", height="1", width="5", command=upusername).grid(row=0, column=4,
                                                                                                      pady=20, padx=10)
            Button(isShow, text='עידכון', bg="white", height="1", width="5", command=upfname).grid(row=3, column=4,
                                                                                                   pady=20,
                                                                                                   padx=10)
            Button(isShow, text='עידכון', bg="white", height="1", width="5", command=uplname).grid(row=5, column=4,
                                                                                                   pady=20,
                                                                                                   padx=10)
            Button(isShow, text='עידכון', bg="white", height="1", width="5", command=uppass).grid(row=7, column=4,
                                                                                                  pady=20,
                                                                                                  padx=10)
            Button(isShow, text='עידכון', bg="white", height="1", width="5", command=uprname).grid(row=9, column=4,
                                                                                                   pady=20,
                                                                                                   padx=10)
            Button(isShow, text='עידכון', bg="white", height="1", width="5", command=upmail).grid(row=11, column=4,
                                                                                                  pady=20,
                                                                                                  padx=10)
            Button(isShow, text='עידכון', bg="white", height="1", width="5", command=upphone).grid(row=13, column=4,
                                                                                                   pady=20, padx=10)

            isShow.grid()
            isShow.mainloop()

        def create():
            global i
            if i.get() == 0:
                insert_user(txtfname.get(), txtlname.get(), txtid.get(), txtrname.get(), txtmail.get(), txtuser.get(),
                            txtpass.get(), txtgender.get(), txtphone.get(), txtanswer.get(), np, dp)
            else:
                messagebox.showinfo('', "אתה חייב להסכים על התנאים")

        def HelpFunc2():
            global isShow
            isShow.forget()
            isShow = Frame(frm)
            Label(isShow, text=exp, bg=bg, fg=fg, font=fnt).grid(row=2, column=2)

            isShow.pack()

        def HelpFunc(texthelp):
            global isShow
            isShow.forget()
            isShow = Frame(frm)
            Label(isShow, text='ההסבר שלך:', bg=bg, fg=fg, font=fnt).grid(row=3, column=0, pady=20)
            Label(isShow, text=exp, bg=bg, fg=fg, font=fnt).grid(row=5, column=0, pady=20)

            isShow.mainloop()

        def pageif():
            if svuser.get().strip() == '':
                messagebox.showinfo('', 'שם המשתמש ריק!')
                txtuser.focus()
            elif svId.get().strip() == '':
                messagebox.showinfo('', 'מספר תעודת הזהות ריק!')
                txtid.focus()
            elif svpass.get().strip() == '':
                messagebox.showinfo('', 'הסיסמה ריק!')
                txtpass.focus()
            elif svfname.get().strip() == '':
                messagebox.showinfo('', 'השם ריק')
                txtfname.focus()
            elif svlname.get().strip() == '':
                messagebox.showinfo('', 'השם השני ריק')
                txtlname.focus()
            elif svgender.get() == '':
                messagebox.showinfo('', 'מין ריק!')
                txtgender.focus()
            elif svrname.get().strip() == '':
                messagebox.showinfo('', 'שם האחראי ריק')
                txtrname.focus()
            elif svmail.get().strip() == '':
                messagebox.showinfo('', 'ה אימיל ריק')
                txtmail.focus()
            elif svphone.get().strip() == '':
                messagebox.showinfo('', 'מספר הטלפון ריק!')
                txtphone.focus()
            # elif svprofile.get().strip()=='':
            # messagebox.showinfo('', 'The profile is Empty!')
            else:
                global isShow
                isShow.forget()
                isShow = Frame(frm)
                ttt = 'the Termos:\n • Not allowed > upload disturbing images\n •Not allowed to extract audio > that has unsuitable words.\n• The system should be used correctly.\n• Allow managers to control my account.\n• Confirmation of saving my personal information in the system'

                Label(isShow, text=ttt, bg=bg, fg=fg, font=fnt).grid(row=0, column=0)
                c = Checkbutton(isShow, text="אני מסכים  ", variable=i, onvalue="checked").grid(
                    row=11, column=0, pady=pad)
                Button(isShow, text='לצור', command=create).grid(row=13, column=3, pady=pad)
                isShow.mainloop()

        def sendmess():
            global isShow
            isShow.forget()
            isShow = Frame(frm)

            def send():
                cursor.execute("UPDATE admins SET massage=?", (svmassage.get(),))
                conn.commit()
                mainpage()

            Label(isShow, text="הקלד הודעה :", font=fnt).grid(row=1, column=1)
            Entry(isShow, font=fnt, textvariable=svmassage).grid(row=2, column=1)
            Button(isShow, text="שלח", bg="white", height="3", width="10", font=fnt, command=send).grid(row=4,
                                                                                                         column=2,
                                                                                                         padx=100,
                                                                                                         pady=20)
            Button(isShow, text="<- חזרה", bg="white", height="3", width="10", font="10", command=settingpage).grid(
                row=4, column=0, padx=5, pady=80)
            isShow.pack()

        def lang():
            global isShow, svlan
            isShow.forget()
            isShow = Frame(frm)

            def chooslan():
                if svlan.get() == 'English':
                    isShow.forget()
                    frm.destroy()
                    acceptEng()
                elif svlan.get() == 'Arabic':
                    frm.destroy()
                    acceptArab()
                elif svlan.get() == 'Hebrew':
                    frm.destroy()
                    acceptHeb()

            txtlan = ttk.Combobox(isShow, values=('English', 'Arabic', 'Hebrew'), textvariable=svlan,
                                  state='readonly').grid(row=1, column=1, pady=pad)
            Button(isShow, text="בחור", bg="white", height="3", width="10", font="10", command=chooslan()).grid(
                row=3, column=1, padx=5, pady=80)
            Button(isShow, text="<- חזרה", bg="white", height="3", width="10", font="10", command=settingpage).grid(
                row=4, column=0, padx=5, pady=80)
            isShow.pack()

        def settingpage():
            global isShow
            isShow.forget()
            isShow = Frame(frm)

            Button(isShow, text="שפה", bg="white", height="6", width="30", font=fnt, command=lambda: lang()).grid(
                row=4, column=1,
                padx=100, pady=20)
            Button(isShow, text="חיבור", bg="white", height="6", width="30", font=fnt, command=sendmess).grid(row=6,
                                                                                                                column=1,
                                                                                                                padx=100,
                                                                                                                pady=20)
            Button(isShow, text="עזרה!", bg="white", height="6", width="30", font="50", command=HelpFunc2).grid(row=2,
                                                                                                                column=1,
                                                                                                                padx=100,
                                                                                                                pady=20)
            # Button(isShow, text="Edit Profile", bg="white", height="6", width="30", font="50",command=updatepro).grid(row=0, column=1, padx=100, pady=20)
            Button(isShow, text="<- חזרה", bg="white", height="3", width="10", font="10", command=mainpage).grid(
                row=8, column=0, padx=5, pady=80)

            isShow.pack()

        def sign_up():
            isShow.forget()
            global frame, txtuser, txtid, txtfname, txtlname, txtpass, txtgender, txtrname, txtmail, txtphone, txtprofile, txtanswer
            frame = Frame(frm, bg=bg)
            # Label(frame, text='User Data', bg='navy', fg='lightblue', font=fnt).pack(pady=pad)

            Label(frame, text='שם משתמש:', bg=bg, fg=fg, font=fnt).grid(row=0, column=0)
            Label(frame, text='מספר תעודת זהות של אוטיסטית:', bg=bg, fg=fg, font=fnt).grid(row=1, column=0)
            Label(frame, text='שמו הפרטי של האוטיסט :', bg=bg, fg=fg, font=fnt).grid(row=2, column=0)
            Label(frame, text='שם המשפחה של האוטיסט :', bg=bg, fg=fg, font=fnt).grid(row=3, column=0)
            Label(frame, text='הסיסמא:', bg=bg, fg=fg, font=fnt).grid(row=4, column=0)
            Label(frame, text='מין האוטיסט: ', bg=bg, fg=fg, font=fnt).grid(row=5, column=0)
            Label(frame, text='שם האחראי :', bg=bg, fg=fg, font=fnt).grid(row=6, column=0)
            Label(frame, text='הדואר האלקטרוני של האחראי :', bg=bg, fg=fg, font=fnt).grid(row=7, column=0)
            Label(frame, text='הטלפון המספרי של האחראי:', bg=bg, fg=fg, font=fnt).grid(row=8, column=0)
            Label(frame, text='מה בית הספר היסודי שלך? ', bg=bg, fg=fg, font=fnt).grid(row=9, column=0)

            # Label(frame, text='The profile of the Autistic :', bg=bg, fg=fg, font=fnt).grid(row=9, column=0)
            # Label(top, image=im).pack()
            txtuser = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svuser)
            txtid = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svId)
            txtfname = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svfname)
            txtlname = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svlname)
            txtpass = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svpass)
            txtgender = ttk.Combobox(frame, values=('Male', 'Female'), textvariable=svgender, state='readonly')
            txtrname = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svrname)
            txtmail = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svmail)
            txtphone = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svphone)
            # txtprofile = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svprofile)
            txtanswer = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svanswer)

            btns = ttk.Style()
            btns.configure('TButton', font=fnt, pady=pad, padding=pad)
            ttk.Button(frame, text='תמונת פרופיל',
                       command=lambda: saveprofile(filedialog.askopenfilename(filetypes=[("Image File", '.png')]))) \
                .grid(row=10, column=0, pady=15)
            # ttk.Button(frame, text='Create new account', command=create).grid(row=11, column=1, pady=pad)
            # ttk.Button(frm, text='Exit Now', command=frm.destroy).grid(row=9, column=2, pady=pad)
            ttk.Button(frame, text='חזור', command=f).grid(row=13, column=0, pady=8)
            ttk.Button(frame, text='המשך', command=pageif).grid(row=13, column=3, pady=8)
            txtuser.grid(row=0, column=1, pady=pad)
            txtid.grid(row=1, column=1, pady=pad)
            txtfname.grid(row=2, column=1, pady=pad)
            txtlname.grid(row=3, column=1, pady=pad)
            txtpass.grid(row=4, column=1, pady=pad)
            txtgender.grid(row=5, column=1, pady=pad)
            txtrname.grid(row=6, column=1, pady=pad)
            txtmail.grid(row=7, column=1, pady=pad)
            txtphone.grid(row=8, column=1, pady=pad)
            txtanswer.grid(row=9, column=1, pady=pad)

            frame.pack(pady=pad)

        def saveprofile(name):
            global np, dp
            a = open(name, 'rb')
            np = name
            dp = a.read()

        def convp():
            cursor.execute("SELECT * FROM users WHERE user_name=?", (svuser.get(),))
            row = cursor.fetchall()
            for i in row:
                name = i[12]
                imager = i[13]
            global ddp
            if (name != None):
                b = open(name, 'wb')
                b.write(imager)
                ddp = PhotoImage(file=name)
                return ddp

            print(5)

        def newbord():
            print(1)
            isShow.forget()

            def insertimag(num):
                def choosepic(num):
                    def choose(key, name):
                        convertTbinary(key, name)
                        isShow1.destroy()

                    def allcat():

                        def funcB(N, K):
                            print(N)

                            def lastFuncc():

                                '''print(numImg)
                                root = Tk()
                                canvas = Canvas(root, width=300, height=300)
                                canvas.pack()
                                im = Image.open(numImg)
                                resized = im.resize((200, 200), Image.ANTIALIAS)
                                photo1 = ImageTk.PhotoImage(resized)
                                myvar = tk.Button(root, image=photo1)
                                myvar.image = photo1
                                myvar.pack()
                                root.mainloop()

                                global isShow
                                isShow=Frame(frm)
                                isShow=imageToInsert['im1']
                            '''

                                def convertToimage(name, imager):
                                    if (name != None):
                                        b = open(name, 'wb')
                                        b.write(imager)
                                        photonameList1.append(name)
                                        photo1Dic[name] = PhotoImage(file=name)

                                global imageNameInasertc
                                cursor.execute("SELECT * FROM category WHERE name=?", (N,))
                                y = cursor.fetchall()
                                for n in y:
                                    for i in range(1, 13, 2):
                                        convertToimage(n[i], n[i + 1])
                                print(photo1Dic)
                                for i in y:
                                    print(i[0])
                                    Fram(N, i[2], i[4], i[6], i[8], i[10], i[12], i[1], i[3], i[5], i[7], i[9], i[11])

                            def Fram(name, data1, data2, data3, data4, data5, data6, image1=None, image2=None,
                                     image3=None, image4=None, image5=None, image6=None):

                                global isShow2, catDic
                                isShow2.forget()
                                isShow2 = Frame(isShow1)
                                print(image1)
                                Label(isShow2, text=name).grid(row=0, columnspan=2, pady=20)
                                print(photo1Dic)
                                if image1:
                                    b = Button(isShow2, height="300", width="300", image=photo1Dic[image1],
                                               command=lambda: choose('im' + str(num), image1))
                                    b.grid(row=1, column=0)
                                if image2:
                                    c = Button(isShow2, height="300", width="300", image=photo1Dic[image2],
                                               command=lambda: choose('im' + str(num), image2))
                                    c.grid(row=1, column=1)
                                if image3:
                                    d = Button(isShow2, height="300", width="300", image=photo1Dic[image3],
                                               command=lambda: choose('im' + str(num), image3))
                                    d.grid(row=1, column=2)
                                if image4:
                                    t = Button(isShow2, height="300", width="300", image=photo1Dic[image4],
                                               command=lambda: choose('im' + str(num), image4))
                                    t.grid(row=2, column=0)
                                if image5:
                                    t = Button(isShow2, height="300", width="300", image=photo1Dic[image5],
                                               command=lambda: choose('im' + str(num), image5))
                                    t.grid(row=2, column=1)
                                if image6:
                                    t = Button(isShow2, height="300", width="300", image=photo1Dic[image6],
                                               command=lambda: choose('im' + str(num), image6))
                                    t.grid(row=2, column=2)
                                Button(isShow2, text="<- חזור", bg="white", height="3", width="10", font="10",
                                       command=allcat).grid(
                                    row=3, column=0, padx=5, pady=80)
                                # if name in tuple(cat1Dic):
                                # cat1Dic[name].append(isShow2)
                                #### and insert to DB
                                # else:
                                # cat1Dic[name] = isShow2
                                # isShow2 = cat1Dic[name]
                                # print(cat1Dic)
                                isShow2.pack()

                            C = Button(isShow2, text=N, bg="white", height="3", width="15", font="20",
                                       command=lambda: lastFuncc())
                            C.bind('<Button-1>', lambda event, frame=isShow2, arg=N: bord(N))
                            C.grid(row=K, column=1, padx=30, pady=20)

                        global isShow2, row
                        isShow2.forget()

                        isShow2 = Frame(isShow1)

                        cursor.execute("SELECT * FROM category")
                        row = cursor.fetchall()
                        k = 0

                        for i in row:
                            funcB(i[0], k)
                            k += 1
                            '''
                            b=Button(isShow, text=y, bg="white", height="3", width="15", font="20")
                            b.bind('<Button-1>', lambda event, frame=isShow, arg=y: bord(y))
                            b.grid(row=k, column=1, padx=30, pady=20)
                            k+=1
                            '''
                        Button(isShow, text="<- חזור", bg="white", height="3", width="10", font="10",
                               command=mainpage).grid(
                            row=k, column=0, padx=5, pady=80)

                        isShow2.pack()

                    global isShow2, isShow1

                    isShow1 = tk.Toplevel()
                    isShow2 = Frame(isShow1)

                    def comp():
                        global isShow2
                        convertTbinary('im' + str(num), filedialog.askopenfilename(filetypes=[("Image File", '.png')]))
                        isShow1.destroy()
                        insertimag(num)

                    def cat():
                        global isShow2
                        isShow2.forget()
                        allcat()

                    Button(isShow2, text="קטגוריה", bg="white", height="5", width="20", font="25", command=cat).grid(
                        row=2, column=2, sticky=W, padx=30, pady=50)
                    Button(isShow2, text="ממחשב", bg="white", height="5", width="20", font="25",
                           command=comp).grid(row=3, column=2, sticky=W, padx=30, pady=50)
                    Button(isShow, text="<- חזור", bg="white", height="3", width="10", font="10",
                           command=lambda: insertimag(num)).grid(
                        row=4, column=0, padx=5, pady=80)
                    isShow2.pack()

                def funcVoice(name):

                    fs = 44100  # Sample rate
                    seconds = 3  # Duration of recording
                    print("seeey")
                    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
                    sd.wait()  # Wait until recording is finished
                    file = name
                    write(file, fs, myrecording)  # Save as WAV file
                    global vvo
                    vvo = file
                    # playsound(file)

                def saveimb():
                    global isShow

                    # print(imageToInsert['im1'])
                    # isShow.forget()
                    if num == 1:
                        cursor.execute("UPDATE 'boards' SET nameim1=?,sound1=?,image1=? WHERE name=? ",
                                       (imageNameInasert['im1name'], vvo, imageToInsert['im1'], txtbord.get()))
                        conn.commit()
                    elif num == 2:
                        cursor.execute("UPDATE 'boards' SET nameim2=?,sound2=?,image2=? WHERE name=? ",
                                       (imageNameInasert['im2name'], vvo, imageToInsert['im2'], txtbord.get()))
                        conn.commit()
                    elif num == 3:
                        cursor.execute("UPDATE 'boards' SET nameim3=?,sound3=?,image3=? WHERE name=? ",
                                       (imageNameInasert['im3name'], vvo, imageToInsert['im3'], txtbord.get()))
                        conn.commit()
                    elif num == 4:
                        cursor.execute("UPDATE 'boards' SET nameim4=?,sound4=?,image4=? WHERE name=? ",
                                       (imageNameInasert['im4name'], vvo, imageToInsert['im4'], txtbord.get()))
                        conn.commit()
                    isShow.forget()
                    creatbord()

                    # for n in imageToInsert:
                    # convertToimage(imageNameInasert['im1' + 'name'], imageToInsert['im1'])
                    # Fram(name, imageNameInasert['im1name'])
                    # imageNameInasert['im1name'] = None
                    # ChooseBordOrCat()
                    # catDic[name][0].pack()
                    # isShow=catDic[name][0]

                global isShow
                isShow.forget()
                isShow = Frame(frm)
                Label(isShow, text='שם התמונה:', bg="white", fg=fg, font=" impact 25").grid(row=0, column=2)
                lbl = ttk.Label(isShow, text='שם התמונה?')
                lbl.config(font=fnt)
                nameim = ttk.Entry(isShow)
                nameim.config(font=fnt)
                nameim.grid(row=1, column=2)

                Button(isShow, text="הוסף קול  ", bg="white", height="5", width="10", font="20",
                       command=lambda: funcVoice("x" + str(num) + txtbord.get() + ".wav")).grid(row=2,
                                                                                                column=2,
                                                                                                sticky=W,
                                                                                                padx=90,
                                                                                                pady=60)

                Button(isShow, text="הוסף תמונה ", bg="white", height="5", width="10", font="20",
                       command=lambda: choosepic(num)).grid(row=4, column=2, sticky=W, padx=90, pady=60)
                ok = tk.Button(isShow, text=" שמור ", bg="white", height="3", width="5", font="20",
                               command=saveimb).grid(row=5, column=1, sticky=W, padx=20, pady=20)
                back = tk.Button(isShow, text=" <- חזור ", bg="white", height="3", width="5", font="20",
                                 command=newbord).grid(row=5,
                                                       column=0,
                                                       sticky=W,
                                                       padx=20,
                                                       pady=20)

                isShow.pack()

            def setImage(im, namecat):
                global imi, isShow
                counter = 0
                isShow.forget()
                imi = im
                isShow = catDic[namecat][counter]
                isShow.pack()

            def save_B():
                cursor.execute("SELECT * FROM admins")
                x = cursor.fetchall()
                for i in x:
                    if svuser.get() == i[1]:
                        cursor.execute("INSERT INTO boards (name,username) VALUES(?,?)", (txtbord.get(), "everyone"))
                        conn.commit()
                        creatbord()
                        return
                cursor.execute("INSERT INTO boards (name,username) VALUES(?,?)", (txtbord.get(), svuser.get()))
                conn.commit()
                creatbord()

            def creatbord():
                def adminoruser():
                    cursor.execute("SELECT * FROM admins")
                    x = cursor.fetchall()
                    for i in x:
                        if svuser.get() == i[1]:
                            page1_admin()
                            return
                    mainpage()

                global isShow
                isShow.forget()
                isShow = Frame(frm)

                # cursor.execute("INSERT INTO boards (name) VALUES(?)", (txtbord.get(),))
                # conn.commit()
                Button(isShow, text="+1", bg="white", height="10", width="20", font="100",
                       command=lambda: insertimag(1)).grid(row=1, column=1, sticky=W, padx=60, pady=20)
                Button(isShow, text="+2", bg="white", height="10", width="20", font="100",
                       command=lambda: insertimag(2)).grid(row=1, column=4, sticky=W, padx=90, pady=20)
                Button(isShow, text="+3", bg="white", height="10", width="20", font="100",
                       command=lambda: insertimag(3)).grid(row=2, column=1, sticky=W, padx=60, pady=50)
                Button(isShow, text="+4", bg="white", height="10", width="20", font="100",
                       command=lambda: insertimag(4)).grid(row=2, column=4, sticky=W, padx=90, pady=100)
                Button(isShow, text="שמור", bg="white", height="3", width="10", font="100",
                       command=lambda: adminoruser()).grid(row=3, column=4, sticky=W, padx=170, pady=20)
                back = tk.Button(isShow, text=" <-חזור ", bg="white", height="3", width="10", font="100",
                                 command=namebord).grid(row=3, column=0, sticky=W, padx=20, pady=20)

                isShow.pack()

            def namebord():
                global isShow, txtbord
                isShow.forget()
                print(2)
                print(3)
                isShow = Frame(frm)
                B = ttk.Button(isShow, text="להיכנס", command=save_B)
                Label(isShow, text='שם הלוח:', font=fnt).pack()
                print(4)
                txtbord = ttk.Entry(isShow)
                txtbord.config(font=fnt)

                print(5)
                txtbord.pack()
                B.pack()

                Button(isShow, text="<- חזור", bg="white", height="3", width="10", font="10", command=mainpage).pack()
                isShow.pack()
                # mainframe.pack()

            namebord()

        def bord(z):

            print(z)

            def voice(num):

                for i in row:
                    if i[0] == z:
                        if num == 3:
                            playsound(i[2])
                        elif num == 6:
                            playsound(i[5])
                        elif num == 9:
                            playsound(i[8])
                        elif num == 12:
                            playsound(i[11])

            # print(row)

            '''
            global isShow
            isShow.forget()
            isShow = Frame(frm)
            cursor.execute("SELECT * FROM boards WHERE name=?", (z,))
            row = cursor.fetchall()
            for i in row:
                j = 1
                print(i)
                lastFunc(i[3], 3)

                b1=Button(isShow, bg="white", height="10", width="20", font="100", image=i[3],command=lambda: voice(1)).grid(row=1, column=1, sticky=W, padx=60, pady=20)
                b2=Button(isShow, bg="white", height="10", width="20", font="100", image=i[6],command=lambda: voice(2)).grid(row=1, column=4, sticky=W, padx=90, pady=20)
                b3=Button(isShow, bg="white", height="10", width="20", font="100", image=i[9],command=lambda: voice(3)).grid(row=2, column=1, sticky=W, padx=60, pady=50)
                b4=Button(isShow, bg="white", height="10", width="20", font="100", image=i[12],command=lambda: voice(4)).grid(row=2, column=4, sticky=W, padx=90, pady=100)
                # Button(bordframe, text="Save", bg="white", height="3", width="10", font="100").grid(row=3, column=4,sticky=W, padx=170,pady=20)
                back = tk.Button(isShow, text=" <- Back ", bg="white", height="3", width="10", font="100",command=lambda: allboards()).grid(row=3,column=0,sticky=W,padx=20,pady=20)

                b1.image=convertToimage('name1.txt', i[3])
                b2.image=convertToimage('name2.txt', i[6])
                b3.image=convertToimage('name3.txt', i[9])
                b4.image=convertToimage('name4.txt', i[12])
                '''
            isShow.pack()

        def allboards():

            def funcB(N, K):
                print(N)

                def lastFunc():

                    '''print(numImg)
                    root = Tk()
                    canvas = Canvas(root, width=300, height=300)
                    canvas.pack()
                    im = Image.open(numImg)
                    resized = im.resize((200, 200), Image.ANTIALIAS)
                    photo1 = ImageTk.PhotoImage(resized)
                    myvar = tk.Button(root, image=photo1)
                    myvar.image = photo1
                    myvar.pack()
                    root.mainloop()

                    global isShow
                    isShow=Frame(frm)
                    isShow=imageToInsert['im1']
                '''
                    global imageNameInasert
                    cursor.execute("SELECT * FROM boards WHERE name=?", (N,))
                    y = cursor.fetchall()
                    for n in y:
                        for i in range(1, 11, 3):
                            convertToimage(n[i], n[i + 2])
                    print(photoDic)
                    cursor.execute("SELECT * FROM boards WHERE name=?", (N,))
                    x = cursor.fetchall()
                    for i in x:
                        print(i[0])
                        Fram(N, i[1], i[4], i[7], i[10])
                    imageNameInasert['im1name'], imageNameInasert['im2name'], imageNameInasert['im3name'], \
                    imageNameInasert[
                        'im4name'] = None, None, None, None

                def Fram(name, image1=None, image2=None, image3=None, image4=None):
                    def voice(num):
                        cursor.execute("SELECT * FROM boards WHERE name=?", (name,))
                        vo = cursor.fetchall()
                        for i in vo:
                            if i[0] == name:
                                if num == 1:
                                    playsound(i[2])
                                elif num == 2:
                                    playsound(i[5])
                                elif num == 3:
                                    playsound(i[8])
                                elif num == 4:
                                    playsound(i[11])

                    global isShow, catDic
                    isShow.forget()
                    isShow = Frame(frm)
                    print(image1)
                    Label(isShow, text=name).grid(row=0, columnspan=2, pady=20)
                    print(photoDic)
                    if image1:
                        b = Button(isShow, height="400", width="400", image=photoDic[image1], command=lambda: voice(1))
                        b.grid(row=1, column=0)
                    if image2:
                        c = Button(isShow, height="400", width="400", image=photoDic[image2], command=lambda: voice(2))
                        c.grid(row=1, column=1)
                    if image3:
                        d = Button(isShow, height="400", width="400", image=photoDic[image3], command=lambda: voice(3))
                        d.grid(row=2, column=0)
                    if image4:
                        t = Button(isShow, height="400", width="400", image=photoDic[image4], command=lambda: voice(4))
                        t.grid(row=2, column=1)
                    Button(isShow, text="<- חזור", bg="white", height="3", width="10", font="10",
                           command=allboards).grid(
                        row=3, column=0, padx=5, pady=80)
                    if name in tuple(catDic):
                        catDic[name].append(isShow)
                        #### and insert to DB
                    else:
                        catDic[name] = isShow
                    isShow = catDic[name]
                    print(catDic)
                    isShow.pack()

                C = Button(isShow, text=N, bg="white", height="3", width="15", font="20", command=lambda: lastFunc())
                C.bind('<Button-1>', lambda event, frame=isShow, arg=N: bord(N))
                C.grid(row=K, column=1, padx=30, pady=20)

            global isShow, row
            isShow.forget()

            isShow = Frame(frm)

            cursor.execute("SELECT * FROM boards")
            row = cursor.fetchall()
            k = 0

            for i in row:
                if i[13] == svuser.get() or i[13] == "everyone":
                    funcB(i[0], k)
                    k += 1
                '''
                b=Button(isShow, text=y, bg="white", height="3", width="15", font="20")
                b.bind('<Button-1>', lambda event, frame=isShow, arg=y: bord(y))
                b.grid(row=k, column=1, padx=30, pady=20)
                k+=1
                '''
            Button(isShow, text="<- Back", bg="white", height="3", width="10", font="10", command=mainpage).grid(
                row=k, column=0, padx=5, pady=80)
            isShow.pack()

        def mainpage():

            global isShow
            isShow.forget()
            isShow = Frame(frm)
            '''
            create=ttk.Button(mainframe,text='Create a new board!',command= newbord)
            exi=ttk.Button(mainframe,text='An existing boards')
            setting=ttk.Button(mainframe,text='setting')
            profile=ttk.Button(mainframe,text='profile')
            profile.pack()
            create.pack()
            exi.pack()
            setting.pack()

            '''
            cursor.execute("SELECT * FROM users WHERE user_name=?", (svuser.get(),))
            row = cursor.fetchall()
            for i in row:
                proimg = i[12]
            # create = ttk.Button(mainframe, text='Create a new board!')

            Label(isShow, bg="white", font=fnt, height=200, width=200, image=convp()).grid(row=2, column=1, padx=300,
                                                                                           pady=10)
            Button(isShow, text="הגדרות", bg="white", font=fnt, command=settingpage).grid(row=8, column=1, padx=300,
                                                                                           pady=10)
            Button(isShow, text="צור לוח חדש!", bg="white", font=fnt, command=newbord).grid(row=6, column=1,
                                                                                                   padx=300, pady=10)
            Button(isShow, text="לוחות קיימים", bg="white", font=fnt, command=allboards).grid(row=4, column=1,
                                                                                                    padx=200, pady=10)
            # Button(mainframe, text="Profile", bg="white", font=fnt).grid(row=0, column=1, padx=200, pady=20)

            isShow.pack()

        def forget():
            global isShow
            isShow.forget()

            def returnpass():
                global isShow
                isShow.forget()
                isShow = Frame(frm)

                def checkpass():

                    if txtnew.get() == txt2.get():
                        account()
                    else:
                        messagebox.showinfo('', 'הסיסמאות לא תואמות!')
                        txtnew.focus()
                        txt2.focus()

                Label(isShow, text='סיסמה חדשה', font='impact 25').pack()

                lblnew = ttk.Label(isShow, text='הכנס סיסמה חדשה:')
                txtnew = ttk.Entry(isShow)
                lbl2 = ttk.Label(isShow, text='הזן את הסיסמה פעם נוספת:')
                txt2 = ttk.Entry(isShow)
                change = ttk.Button(isShow, text='שנה סיסמא', command=checkpass)
                Button(isShow, text="<- חזור", bg="white", height="3", width="10", font="10", command=question).grid(
                    row=4, column=0, padx=5, pady=80)
                lblnew.config(font=fnt)
                txtnew.config(font=fnt)
                lbl2.config(font=fnt)
                txt2.config(font=fnt)

                lblnew.pack()
                txtnew.pack()
                lbl2.pack()
                txt2.pack()
                change.pack()
                isShow.pack()

            def question():
                global isShow
                isShow.forget()
                isShow = Frame(frm)

                def forgetpass():

                    cursor.execute("SELECT * FROM 'users' ")
                    rows = cursor.fetchall()
                    for i in rows:
                        if txtid.get() == i[3] and txtanswer.get() == i[12]:
                            returnpass()
                            print(txtanswer.get())

                Label(isShow, text='אבטחת חשבון', font='impact 25').pack()

                lbl1 = ttk.Label(isShow, text='מספר תעודת זהות')
                lbl = ttk.Label(isShow, text='מה בית הספר היסודי שלך?')

                txtanswer = ttk.Entry(isShow)
                txtanswer.config(font=fnt)
                txtid = ttk.Entry(isShow)
                txtid.config(font=fnt)
                lbl1.config(font=fnt)
                lbl.config(font=fnt)
                Button(isShow, text="<- חזור", bg="white", height="3", width="10", font="10", command=login).grid(
                    row=4, column=0, padx=5, pady=80)
                ok = ttk.Button(isShow, text='OK', command=forgetpass)

                lbl1.pack()
                txtid.pack()
                lbl.pack()
                txtanswer.pack()
                ok.pack()
                isShow.pack()

            question()

        def checkuser(name):

            cursor.execute("select * from 'users' where user_name=? ", (name,))
            if cursor.fetchone() is not None:
                return True
            return False

        def page2_admin():
            global r, isShow

            def funAzr():
                text = r.get()
                if checkuser(text) == True:
                    # page3_admin()
                    page4_admin()
                    # page5_admin()

                if checkuser(text) == False:
                    messagebox.showinfo('', 'משתמש לא נמצא!')

            isShow.forget()
            isShow = Frame(frm)
            Label(isShow, text='הזן את שם המשתמש שאתה רוצה לחפש:', bg=bg, fg=fg, font=fnt).grid(row=10, column=1,
                                                                                                  padx=30,
                                                                                                  pady=120)
            r = Entry(isShow, bg="white", fg=fg, font=fnt, textvariable=svuser)
            r.grid(row=10, column=2, padx=30, pady=120)

            Button(isShow, text=" חפש", bg="white", height="1", width="8", font="15", command=funAzr).grid(row=14,
                                                                                                              column=4,
                                                                                                              sticky=W,
                                                                                                              padx=30,
                                                                                                              pady=30)
            Button(isShow, text="<-חזור", bg="white", height="3", width="10", font="10", command=page1_admin).grid(
                row=14, column=0, padx=5, pady=80)
            isShow.mainloop()

        def adminbord():
            global isShow
            isShow.forget()
            isShow = Frame(frm)
            Button(isShow, text="הוסף לוח חדש", bg="white", height="5", width="20", font="25", command=newbord).grid(
                row=2,
                column=2,
                sticky=W,
                padx=30,
                pady=50)
            Button(isShow, text="כל הלוחות", bg="white", height="5", width="20", font="25", command=allboards).grid(
                row=3,
                column=2,
                sticky=W,
                padx=30,
                pady=50)
            Button(isShow, text="<- חזור", bg="white", height="3", width="10", font="10", command=page1_admin).grid(
                row=4, column=0, padx=5, pady=80)
            isShow.pack()

        def allcat():

            def funcB(N, K):
                print(N)

                def lastFuncc():

                    '''print(numImg)
                    root = Tk()
                    canvas = Canvas(root, width=300, height=300)
                    canvas.pack()
                    im = Image.open(numImg)
                    resized = im.resize((200, 200), Image.ANTIALIAS)
                    photo1 = ImageTk.PhotoImage(resized)
                    myvar = tk.Button(root, image=photo1)
                    myvar.image = photo1
                    myvar.pack()
                    root.mainloop()

                    global isShow
                    isShow=Frame(frm)
                    isShow=imageToInsert['im1']
                '''

                    def convertToimage(name, imager):
                        if (name != None):
                            b = open(name, 'wb')
                            b.write(imager)
                            photonameList1.append(name)
                            photo1Dic[name] = PhotoImage(file=name)

                    global imageNameInasertc
                    cursor.execute("SELECT * FROM category WHERE name=?", (N,))
                    y = cursor.fetchall()
                    for n in y:
                        for i in range(1, 13, 2):
                            convertToimage(n[i], n[i + 1])
                    print(photo1Dic)
                    for i in y:
                        print(i[0])
                        Fram(N, i[1], i[3], i[5], i[7], i[9], i[11])
                    imageNameInasert['im1name'], imageNameInasert['im2name'], imageNameInasert['im3name'], \
                    imageNameInasert[
                        'im4name'] = None, None, None, None

                def Fram(name, image1=None, image2=None, image3=None, image4=None, image5=None, image6=None):

                    global isShow, catDic
                    isShow.forget()
                    isShow = Frame(frm)
                    print(image1)
                    Label(isShow, text=name, height="10", width="20", ).grid(row=0, columnspan=2, pady=20)
                    print(photo1Dic)
                    if image1:
                        b = Button(isShow, height="300", width="300", image=photo1Dic[image1])
                        b.grid(row=1, column=0)
                    if image2:
                        c = Button(isShow, height="300", width="300", image=photo1Dic[image2])
                        c.grid(row=1, column=1)
                    if image3:
                        d = Button(isShow, height="300", width="300", image=photo1Dic[image3])
                        d.grid(row=1, column=2)
                    if image4:
                        t = Button(isShow, height="300", width="300", image=photo1Dic[image4])
                        t.grid(row=2, column=0)
                    if image5:
                        t = Button(isShow, height="300", width="300", image=photo1Dic[image5])
                        t.grid(row=2, column=1)
                    if image6:
                        t = Button(isShow, height="300", width="300", image=photo1Dic[image6])
                        t.grid(row=2, column=2)
                    Button(isShow, text="<- Back", bg="white", height="3", width="10", font="10",
                           command=allcat).grid(
                        row=3, column=0, padx=5, pady=80)
                    if name in tuple(cat1Dic):
                        cat1Dic[name].append(isShow)
                        #### and insert to DB
                    else:
                        cat1Dic[name] = isShow
                    isShow = cat1Dic[name]
                    print(cat1Dic)
                    isShow.pack()

                C = Button(isShow, text=N, bg="white", height="3", width="15", font="20", command=lambda: lastFuncc())
                C.bind('<Button-1>', lambda event, frame=isShow, arg=N: bord(N))
                C.grid(row=K, column=1, padx=30, pady=20)

            global isShow, row
            isShow.forget()

            isShow = Frame(frm)

            cursor.execute("SELECT * FROM category")
            row = cursor.fetchall()
            k = 0

            for i in row:
                funcB(i[0], k)
                k += 1
                '''
                b=Button(isShow, text=y, bg="white", height="3", width="15", font="20")
                b.bind('<Button-1>', lambda event, frame=isShow, arg=y: bord(y))
                b.grid(row=k, column=1, padx=30, pady=20)
                k+=1
                '''
            Button(isShow, text="<- חזור", bg="white", height="3", width="10", font="10", command=admincat).grid(
                row=k, column=0, padx=5, pady=80)

            isShow.pack()

        def newcat():

            def saveimc(num):
                if num == 1:
                    cursor.execute("UPDATE 'category' SET c1name=?,image1=? WHERE name=? ",
                                   (imageNameInasertc['im1name'], imageToInsertc['im1'], txtcat.get()))
                    conn.commit()
                elif num == 2:
                    cursor.execute("UPDATE 'category' SET c2name=?,image2=? WHERE name=? ",
                                   (imageNameInasertc['im2name'], imageToInsertc['im2'], txtcat.get()))
                    conn.commit()
                elif num == 3:
                    cursor.execute("UPDATE 'category' SET c3name=?,image3=? WHERE name=? ",
                                   (imageNameInasertc['im3name'], imageToInsertc['im3'], txtcat.get()))
                    conn.commit()
                elif num == 4:
                    cursor.execute("UPDATE 'category' SET c4name=?,image4=? WHERE name=? ",
                                   (imageNameInasertc['im4name'], imageToInsertc['im4'], txtcat.get()))
                    conn.commit()
                elif num == 5:
                    cursor.execute("UPDATE 'category' SET c5name=?,image5=? WHERE name=? ",
                                   (imageNameInasertc['im5name'], imageToInsertc['im5'], txtcat.get()))
                    conn.commit()
                elif num == 6:
                    cursor.execute("UPDATE 'category' SET c6name=?,image6=? WHERE name=? ",
                                   (imageNameInasertc['im6name'], imageToInsertc['im6'], txtcat.get()))
                    conn.commit()

                # for n in imageToInsert:
                # convertToimage(imageNameInasert['im1' + 'name'], imageToInsert['im1'])
                # Fram(name, imageNameInasert['im1name'])
                # imageNameInasert['im1name'] = None
                # ChooseBordOrCat()
                # catDic[name][0].pack()
                # isShow=catDic[name][0]

            def setImage(im, namecat):
                global imi, isShow
                counter = 0
                isShow.forget()
                imi = im
                isShow = catDic[namecat][counter]
                isShow.pack()

            def save_C():

                cursor.execute("INSERT INTO category (name) VALUES(?)", (txtcat.get(),))
                conn.commit()
                creatcat()

            def convertTbinaryc(key, name, num):
                a = open(name, 'rb')
                imageNameInasertc[key + 'name'] = name

                imageToInsertc[key] = a.read()
                saveimc(num)

            def creatcat():
                global isShow
                isShow.forget()
                isShow = Frame(frm)

                # cursor.execute("INSERT INTO boards (name) VALUES(?)", (txtbord.get(),))
                # conn.commit()
                Button(isShow, text="+1", bg="white", height="10", width="20", font="100",
                       command=lambda: convertTbinaryc('im' + str(1),
                                                       filedialog.askopenfilename(filetypes=[("Image File", '.png')]),
                                                       1)).grid(row=1, column=0, sticky=W, padx=60, pady=20)
                Button(isShow, text="+2", bg="white", height="10", width="20", font="100",
                       command=lambda: convertTbinaryc('im' + str(2),
                                                       filedialog.askopenfilename(filetypes=[("Image File", '.png')]),
                                                       2)).grid(row=1, column=3, sticky=W, padx=90, pady=20)
                Button(isShow, text="+3", bg="white", height="10", width="20", font="100",
                       command=lambda: convertTbinaryc('im' + str(3),
                                                       filedialog.askopenfilename(filetypes=[("Image File", '.png')]),
                                                       3)).grid(row=1, column=5, sticky=W, padx=60, pady=50)
                Button(isShow, text="+4", bg="white", height="10", width="20", font="100",
                       command=lambda: convertTbinaryc('im' + str(4),
                                                       filedialog.askopenfilename(filetypes=[("Image File", '.png')]),
                                                       4)).grid(row=2, column=0, sticky=W, padx=90, pady=100)
                Button(isShow, text="+5", bg="white", height="10", width="20", font="100",
                       command=lambda: convertTbinaryc('im' + str(5),
                                                       filedialog.askopenfilename(filetypes=[("Image File", '.png')]),
                                                       4)).grid(row=2, column=3, sticky=W, padx=90, pady=100)
                Button(isShow, text="+6", bg="white", height="10", width="20", font="100",
                       command=lambda: convertTbinaryc('im' + str(6),
                                                       filedialog.askopenfilename(filetypes=[("Image File", '.png')]),
                                                       4)).grid(row=2, column=5, sticky=W, padx=90, pady=100)

                Button(isShow, text="שמור", bg="white", height="3", width="10", font="100",
                       command=lambda: page1_admin()).grid(row=3, column=4, sticky=W, padx=170, pady=20)
                back = tk.Button(isShow, text=" <-חזור ", bg="white", height="3", width="10", font="100",
                                 command=namecat).grid(row=3, column=0, sticky=W, padx=20, pady=20)

                isShow.pack()

            def namecat():
                global isShow, txtcat
                isShow.forget()
                print(2)
                print(3)
                isShow = Frame(frm)
                B = ttk.Button(isShow, text="הכניס", command=save_C)
                Label(isShow, text='שם קטיגוריה:', font=fnt).pack()
                print(4)
                txtcat = ttk.Entry(isShow)
                txtcat.config(font=fnt)
                Button(isShow, text="<- חזור", bg="white", height="3", width="10", font="10", command=admincat()).grid(
                    row=4, column=0, padx=5, pady=80)

                print(5)
                txtcat.pack()
                B.pack()

                back = ttk.Button(isShow, text=" <- חזור ")
                back.pack()
                isShow.pack()
                # mainframe.pack()

            namecat()

        def admincat():
            global isShow
            isShow.forget()
            isShow = Frame(frm)
            Button(isShow, text="הוסף קטיגוריה חדשה", bg="white", height="5", width="20", font="25",
                   command=newcat).grid(
                row=2,
                column=2,
                sticky=W,
                padx=30,
                pady=50)
            Button(isShow, text="כל הקטגוריות", bg="white", height="5", width="20", font="25", command=allcat).grid(
                row=3,
                column=2,
                sticky=W,
                padx=30,
                pady=50)
            Button(isShow, text="<-חזור", bg="white", height="3", width="10", font="10", command=page1_admin).grid(
                row=4, column=0, padx=5, pady=80)
            isShow.pack()

        def addadmin():
            global isShow
            isShow.forget()
            isShow = Frame(frm)

            def add():
                cursor.execute("INSERT INTO admins (username,password,first_name,last_name) VALUES(?,?,?,?)",
                               (svuser.get(), svpass.get(), svfname.get(), svlname.get()))
                conn.commit()
                page1_admin()

            Label(isShow, text="הכנס שם משתמש:", font=fnt).grid(row=1, column=1)
            Entry(isShow, textvariable=svuser, font=fnt).grid(row=1, column=2)
            Label(isShow, text="הזן את הסיסמה:", font=fnt).grid(row=2, column=1)
            Entry(isShow, textvariable=svpass, font=fnt).grid(row=2, column=2)
            Label(isShow, text="הזן שם פרטי:", font=fnt).grid(row=3, column=1)
            Entry(isShow, textvariable=svfname, font=fnt).grid(row=3, column=2)
            Label(isShow, text="הזן שם משפחה:", font=fnt).grid(row=4, column=1)
            Entry(isShow, textvariable=svlname, font=fnt).grid(row=4, column=2)
            Button(isShow, text="להוסיף", bg="white", font=1, command=add).grid(row=5, column=2, padx=10, pady=10)
            Button(isShow, text="<- חזור", bg="white", height="3", width="10", font="10", command=page1_admin).grid(
                row=6, column=0, padx=5, pady=80)
            isShow.pack()

        def page1_admin():
            global isShow
            isShow.forget()
            isShow = Frame(frm)

            Button(isShow, text="חפש משתמש", bg="white", height="5", width="20", font="25",
                   command=page2_admin).grid(
                row=2, column=1, sticky=W, padx=30, pady=50)
            Button(isShow, text="לוחות", bg="white", height="5", width="20", font="25", command=adminbord).grid(row=2,
                                                                                                                 column=3,
                                                                                                                 sticky=W,
                                                                                                                 padx=30,
                                                                                                                 pady=50)
            Button(isShow, text="קטיגוריה", bg="green", height="5", width="20", font="25", command=admincat).grid(
                row=3, column=1,
                sticky=W,
                padx=30, pady=20)
            Button(isShow, text="עדכן את הדף הסבר ", bg="white", height="5", width="20", font="25",
                   command=explain).grid(row=3, column=2, sticky=W, padx=30, pady=20)
            # Button(page3, text="Birthday", bg="green", height="5", width="20", font="25").grid(row=3, column=3, sticky=W, padx=30,pady=20)
            # Button(frm, text="Delete an user ", bg="green", height="5", width="20", font="25").grid(row=4, column=2, sticky=W, padx=30, pady=20)
            Button(isShow, text="עיצוב שלי ", bg="green", height="5", width="20", font="25").grid(row=2, column=2,
                                                                                                  sticky=W,
                                                                                                  padx=30, pady=50)
            Button(isShow, text="הוסף מנהל ", bg="green", height="5", width="20", font="25", command=addadmin).grid(
                row=3, column=3, sticky=W,
                padx=30, pady=50)

            isShow.pack()

        def explain():
            global isShow
            isShow.forget
            isShow = Frame(frm)
            Label(isShow, text='הזן את ההסבר החדש שלך', bg=bg, fg=fg, font=fnt).grid(row=0, column=0)
            m = Entry(isShow, bg="white", fg=fg, font=fnt)
            m.grid(row=10, column=2, padx=30, pady=120)
            Button(isShow, text="Ok", bg="green", height="5", width="20", font="25",
                   command=lambda: HelpFunc(m.get())).grid(row=2, column=2, sticky=W,
                                                           padx=30, pady=50)
            Button(isShow, text="<-חזור", bg="white", height="3", width="10", font="10", command=page1_admin).grid(
                row=4, column=0, padx=5, pady=80)
            isShow.pack()

        def page4_admin():
            global isShow
            isShow.forget()
            isShow = Frame(frm)
            text1 = "Happy Birthday ya qalbiy :) "
            Button(isShow, text="מחק משתמש", bg="white", height="5", width="20", font="25",
                   command=lambda: delete_user(r.get())).grid(row=3, column=1, sticky=W, padx=30, pady=20)
            Button(isShow, text="מאחל יום הולדת שמח", bg="white", height="5", width="20", font="25",
                   command=lambda: update_massage(text1, r.get())).grid(row=5, column=1, sticky=W, padx=30, pady=20)
            Button(isShow, text="שלח הודעה ", bg="white", height="5", width="20", font="25",
                   command=page5_admin).grid(
                row=7, column=1, sticky=W, padx=30, pady=20)
            Button(isShow, text="<- חזור", bg="white", height="3", width="10", font="10", command=page1_admin).grid(
                row=7, column=0, padx=5, pady=80)

            page4.mainloop()

        def page5_admin():
            global isShow
            isShow.forget
            isShow = Frame(frm)
            Label(isShow, text='הזן את ההודעה שברצונך לשלוח למשתמש', bg=bg, fg=fg, font=fnt).grid(
                row=10,
                column=1,
                padx=30,
                pady=120)
            m = Entry(isShow, bg="white", fg=fg, font=fnt, textvariable=svmassage)
            m.grid(row=10, column=2, padx=30, pady=120)
            Button(isShow, text="שלח", bg="white", height="1", width="8", font="15",
                   command=lambda: update_massage(m.get(), r.get())).grid(row=14, column=4, sticky=W, padx=30, pady=30)
            Button(isShow, text="<-חזור", bg="white", height="3", width="10", font="10", command=page4_admin).grid(
                row=14, column=0, padx=5, pady=80)
            # messagebox.showinfo('', 'The massage send!')

        def login():

            global isShow, svuser
            isShow.forget()
            isShow = Frame(frm)

            def check():
                print(svuser.get(), svpass.get())
                cursor.execute("select * from 'users' where user_name=(?) and password=(?) ",
                               (svuser.get(), svpass.get()))
                print(svuser.get(), svpass.get())
                if cursor.fetchone() is None:
                    cursor.execute("select * from 'admins' where username=(?) and password=(?) ",
                                   (svuser.get(), svpass.get()))
                    if cursor.fetchone() is None:
                        messagebox.showinfo('', 'Invalid Username or password!')

                    else:
                        page1_admin()
                else:

                    global id
                    cursor.execute("SELECT * FROM 'users' ")
                    rows = cursor.fetchall()
                    for i in rows:
                        if svuser.get() == i[6] and svpass.get() == i[7]:
                            id = i[3]
                    isShow.forget()
                    mainpage()

            Label(isShow, text="הכנס שם משתמש:").grid(row=1, column=1)
            Entry(isShow, textvariable=svuser).grid(row=2, column=1)
            Label(isShow, text="הזן את הסיסמה:").grid(row=3, column=1)
            Entry(isShow, textvariable=svpass).grid(row=4, column=1)
            '''
            lblname=ttk.Label(loginFrame,text='Enter username:').grid(row=1,column=2,padx=10,pady=10)
            txtname=ttk.Entry(loginFrame).grid(row=2,column=2,padx=10,pady=10)
            lblpass=ttk.Label(loginFrame,text='Enter the password:').grid(row=3,column=2,padx=10,pady=10)
            txtpass=ttk.Entry(loginFrame).grid(row=4,column=2,padx=10,pady=10)
    '''
            Button(isShow, text='התחברות', bg="white", font=5, command=check).grid(row=5, column=1, padx=10, pady=10)
            Button(isShow, text="שכח סיסמא ", bg="white", font=1, command=forget).grid(row=5, column=2, padx=10,
                                                                                            pady=10)
            Button(isShow, text="<- חזור", bg="white", height="3", width="10", font="10", command=f).grid(
                row=5, column=0, padx=5, pady=80)
            isShow.pack()

        def f():
            global isShow, frame
            if frame:
                frame.forget()
            if isShow:
                isShow.forget()
            isShow = Frame(frm)
            Label(isShow, text="בחר כניסה או הרשמה", bg="blue", width="300")
            Label(isShow, text="").pack()
            Button(isShow, text="התחברות", height="2", width="30", command=login).pack()
            Label(isShow, text="").pack()
            Button(isShow, text="להירשם", height="2", width="30", command=sign_up).pack()
            Label(isShow, text="").pack()
            isShow.pack()
            isShow.mainloop()

        f()

    account()
def acceptEng():
    i = IntVar()

    def Database():
        global conn, cursor
        conn = sqlite3.connect("Accept2.db")
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS admins (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, first_name TEXT,last_name TEXT, massage TEXT)")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, first_name TEXT, last_name TEXT, id TEXT,responsible_name TEXT,Email Text,user_name TEXT, password TEXT,phone TEXT,gander TEXT,massage TEXT,answer TEXT,nameprofile TEXT,dataprofile TEXT)")
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS boards(name text,nameim1 text,sound1 blob,image1 text,nameim2 text,sound2 blob,image2 text,nameim3 text,sound3 blob,image3 text,nameim4 text,sound4 blob,image4 text,username text) ')
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS category(name text,c1name text,image1 text,c2name text,image2 text,c3name text,image3 text,c4name text,image4 text,c5name text,image5 text,c6name text,image6 text) ')
        conn.commit()

    Database()
    # cursor.execute("DROP TABLE users;")

    '''
    cursor.execute("INSERT INTO admins (username,password,first_name,last_name) VALUES(?,?,?,?)", ('shatha26','sh','shatha','arar'))
    conn.commit()
    '''
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
        cursor.execute("DELETE FROM 'users' WHERE id=?", (id,))
        conn.commit()

    '''
    def create():
        global i
        if i.get()==0:
            insert_user(txtuser.get(), txtid.get(), txtfname.get(), txtlname.get(), txtpass.get(), txtgender.get(),txtrname.get(), txtmail.get(), txtphone.get(),txtanswer.get())
        else:
            messagebox.showinfo('', "you want to agree the terms")

            '''
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
       txtphone.set('')

       #frame.destroy()


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
    '''
    i = IntVar()

    def logout(frame):
        # Save in Data Base()
        svuser.set('')
        svpass.set('')
        frame.destroy()

    def insert_user(user_name, id, first_name, last_name, password, Email, responsible_name, gander, phone, answer,
                    nameprofile, dataprofile):
        cursor.execute(
            "INSERT INTO users (first_name,last_name,id,responsible_name,Email,user_name,password,gander,phone,answer,nameprofile,dataprofile) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
            (
            first_name, last_name, id, responsible_name, Email, user_name, password, gander, phone, answer, nameprofile,
            dataprofile))
        conn.commit()

    def insert_board(name, id):
        cursor.execute("INSERT INTO boards (name,id) VALUES(?,?)", (name, id))
        conn.commit()

    def delete_user(id):
        cursor.execute("DELETE FROM 'users' WHERE id=?", (id,))

    def delete_user(username):
        cursor.execute("DELETE FROM 'users' WHERE user_name=?", (username,))
        conn.commit()

    def delete_board(nameB):
        cursor.execute("DELETE FROM 'boards' WHERE name=?", (nameB,))
        conn.commit()

    def update_massage(massage, username):
        cursor.execute("UPDATE 'users' SET massage=? WHERE user_name=?", (massage, username))
        conn.commit()

    imageNameInasert = {'im1name': None, 'im2name': None, 'im3name': None, 'im4name': None}

    imageToInsert = {'im1': None, 'im2': None, 'im3': None, 'im4': None}

    imageNameInasertc = {'im1name': None, 'im2name': None, 'im3name': None, 'im4name': None, 'im5name': None,
                         'im6name': None}

    imageToInsertc = {'im1': None, 'im2': None, 'im3': None, 'im4': None, 'im5': None, 'im6': None}
    exp = 0

    def convertTbinary(key, name):
        a = open(name, 'rb')
        imageNameInasert[key + 'name'] = name

        imageToInsert[key] = a.read()

    isShow1 = None

    def convertToimage(name, imager):
        if (name != None):
            b = open(name, 'wb')
            b.write(imager)
            photonameList.append(name)
            photoDic[name] = PhotoImage(file=name)

    isShow2 = None

    def account():
        i = IntVar()
        global isShow
        isShow = Frame(frm)

        def updatepro():
            def upusername():
                cursor.execute("UPDATE 'users' SET user_name=? WHERE id=? ", (svuser.get(), id))
                conn.commit()
                print(77)

            def upfname():
                cursor.execute("UPDATE 'users' SET first_name=? WHERE id=? ", (svfname.get(), id))
                conn.commit()
                print(88)

            def uplname():
                cursor.execute("UPDATE 'users' SET last_name=? WHERE id=? ", (svlname.get(), id))
                conn.commit()

            def uppass():
                cursor.execute("UPDATE 'users' SET password=? WHERE id=? ", (svpass.get(), id))
                conn.commit()

            def uprname():
                cursor.execute("UPDATE 'users' SET responsible_name=? WHERE id=? ", (svrname.get(), id))
                conn.commit()

            def upphone():
                cursor.execute("UPDATE 'users' SET phone=? WHERE id=? ", (svphone.get(), id))
                conn.commit()

            def upmail():
                cursor.execute("UPDATE 'users' SET Email=? WHERE id=? ", (svmail.get(), id))
                conn.commit()

            # settingframe.forget()
            global isShow
            isShow = Frame(frm)
            Label(isShow, text='user name:', bg=bg, fg=fg, font=fnt).grid(row=0, column=0, pady=20)
            Label(isShow, text='The first name of the autistic :', bg=bg, fg=fg, font=fnt).grid(row=3, column=0,
                                                                                                pady=20)
            Label(isShow, text='The last name of the autistic :', bg=bg, fg=fg, font=fnt).grid(row=5, column=0,
                                                                                               pady=20)
            Label(isShow, text='The password :', bg=bg, fg=fg, font=fnt).grid(row=7, column=0, pady=20)
            Label(isShow, text='The name of the responsible :', bg=bg, fg=fg, font=fnt).grid(row=9, column=0, pady=20)
            Label(isShow, text='The E-mail of the responsible :', bg=bg, fg=fg, font=fnt).grid(row=11, column=0,
                                                                                               pady=20)
            Label(isShow, text='The number phone of the responsible :', bg=bg, fg=fg, font=fnt).grid(row=13, column=0,
                                                                                                     pady=20)
            # Label(frame, text='The profile of the Autistic :', bg=bg, fg=fg, font=fnt).grid(row=9, column=0)
            # Label(top, image=im).pack()
            Entry(isShow, bg=bgtxt, fg=fg, font=fnt, textvariable=svuser).grid(row=0, column=2)
            Entry(isShow, bg=bgtxt, fg=fg, font=fnt, textvariable=svfname).grid(row=3, column=2)
            Entry(isShow, bg=bgtxt, fg=fg, font=fnt, textvariable=svlname).grid(row=5, column=2)
            Entry(isShow, bg=bgtxt, fg=fg, font=fnt, textvariable=svpass).grid(row=7, column=2)
            Entry(isShow, bg=bgtxt, fg=fg, font=fnt, textvariable=svrname).grid(row=9, column=2)
            Entry(isShow, bg=bgtxt, fg=fg, font=fnt, textvariable=svmail).grid(row=11, column=2)
            Entry(isShow, bg=bgtxt, fg=fg, font=fnt, textvariable=svphone).grid(row=13, column=2)
            # txtprofile = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svprofile).grid(row=15,column=2)
            Button(isShow, text='<-Back', bg="white", height="3", width="10", command=settingpage).grid(row=20,
                                                                                                        column=0,
                                                                                                        pady=20,
                                                                                                        padx=10)
            Button(isShow, text='update', bg="white", height="1", width="5", command=upusername).grid(row=0, column=4,
                                                                                                      pady=20, padx=10)
            Button(isShow, text='update', bg="white", height="1", width="5", command=upfname).grid(row=3, column=4,
                                                                                                   pady=20,
                                                                                                   padx=10)
            Button(isShow, text='update', bg="white", height="1", width="5", command=uplname).grid(row=5, column=4,
                                                                                                   pady=20,
                                                                                                   padx=10)
            Button(isShow, text='update', bg="white", height="1", width="5", command=uppass).grid(row=7, column=4,
                                                                                                  pady=20,
                                                                                                  padx=10)
            Button(isShow, text='update', bg="white", height="1", width="5", command=uprname).grid(row=9, column=4,
                                                                                                   pady=20,
                                                                                                   padx=10)
            Button(isShow, text='update', bg="white", height="1", width="5", command=upmail).grid(row=11, column=4,
                                                                                                  pady=20,
                                                                                                  padx=10)
            Button(isShow, text='update', bg="white", height="1", width="5", command=upphone).grid(row=13, column=4,
                                                                                                   pady=20, padx=10)

            isShow.grid()
            isShow.mainloop()

        def create():

            global i
            if i.get() == 0:
                insert_user(txtfname.get(), txtlname.get(), txtid.get(), txtrname.get(), txtmail.get(), txtuser.get(),
                            txtpass.get(), txtgender.get(), txtphone.get(), txtanswer.get(), np, dp)
            else:
                messagebox.showinfo('', "you want to agree the terms")

        def HelpFunc2():
            global isShow
            isShow.forget()
            isShow = Frame(frm)
            Label(isShow, text=exp, bg=bg, fg=fg, font=fnt).grid(row=2, column=2)

            isShow.pack()

        def HelpFunc(texthelp):
            global isShow
            isShow.forget()
            isShow = Frame(frm)
            Label(isShow, text='your explain is :', bg=bg, fg=fg, font=fnt).grid(row=3, column=0, pady=20)
            Label(isShow, text=exp, bg=bg, fg=fg, font=fnt).grid(row=5, column=0, pady=20)

            isShow.mainloop()

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
            # elif svprofile.get().strip()=='':
            # messagebox.showinfo('', 'The profile is Empty!')
            else:
                i = IntVar()
                fr = tk.Tk()
                fnt = ('tahoma', 16)
                bg = '#ffffff'
                bgtxt = '#00ff00'
                fg = '#000000'
                fw = 700
                fh = 600
                x = (fr.winfo_screenwidth() - fw) / 2
                y = (fr.winfo_screenheight() - fh) / 2 - 50
                fr.geometry('%dx%d+%d+%d' % (fw, fh, x, y))
                fr.title('add pic in new board')
                fr.config(bg=bg)

                ttt = 'the Termos:\n • Not allowed > upload disturbing images\n •Not allowed to extract audio > that has unsuitable words.\n• The system should be used correctly.\n• Allow managers to control my account.\n• Confirmation of saving my personal information in the system'

                Label(fr, text=ttt, bg=bg, fg=fg, font=fnt).grid(row=0, column=0)
                c = Checkbutton(fr, text="I accept the Terms of service ", variable=i, onvalue="checked").grid(
                    row=11, column=0, pady=pad)
                Button(fr, text='Create', command=create).grid(row=13, column=3, pady=pad)
            fr.mainloop()

        def sendmess():
            global isShow
            isShow.forget()
            isShow = Frame(frm)

            def send():
                cursor.execute("UPDATE admins SET massage=?", (svmassage.get(),))
                conn.commit()
                mainpage()

            Label(isShow, text="Type message:", font=fnt).grid(row=1, column=1)
            Entry(isShow, font=fnt, textvariable=svmassage).grid(row=2, column=1)
            Button(isShow, text="send", bg="white", height="3", width="10", font=fnt, command=send).grid(row=4,
                                                                                                         column=2,
                                                                                                         padx=100,
                                                                                                         pady=20)
            Button(isShow, text="<- Back", bg="white", height="3", width="10", font="10", command=settingpage).grid(
                row=4, column=0, padx=5, pady=80)
            isShow.pack()

        def lang():
            global isShow, svlan
            isShow.forget()
            isShow = Frame(frm)

            def chooslan():
                if svlan.get() == 'English':
                    acceptEng()
                elif svlan.get() == 'Arabic':
                    acceptArab()
                elif svlan.get() == 'Hebrew':
                    acceptHeb()
                return

            txtlan = ttk.Combobox(isShow, values=('English', 'Arabic', 'Hebrew'), textvariable=svlan,
                                  state='readonly').grid(row=1, column=1, pady=pad)
            Button(isShow, text="choose", bg="white", height="3", width="10", font="10", command=chooslan()).grid(
                row=3, column=1, padx=5, pady=80)
            Button(isShow, text="<- Back", bg="white", height="3", width="10", font="10", command=settingpage).grid(
                row=4, column=0, padx=5, pady=80)
            isShow.pack()

        def settingpage():
            global isShow
            isShow.forget()
            isShow = Frame(frm)

            Button(isShow, text="Language", bg="white", height="6", width="30", font=fnt, command=lambda: lang()).grid(
                row=4, column=1,
                padx=100, pady=20)
            Button(isShow, text="contact", bg="white", height="6", width="30", font=fnt, command=sendmess).grid(row=6,
                                                                                                                column=1,
                                                                                                                padx=100,
                                                                                                                pady=20)
            Button(isShow, text="Help!", bg="white", height="6", width="30", font="50", command=HelpFunc2).grid(row=2,
                                                                                                                column=1,
                                                                                                                padx=100,
                                                                                                                pady=20)
            # Button(isShow, text="Edit Profile", bg="white", height="6", width="30", font="50",command=updatepro).grid(row=0, column=1, padx=100, pady=20)
            Button(isShow, text="<- Back", bg="white", height="3", width="10", font="10", command=mainpage).grid(
                row=8, column=0, padx=5, pady=80)

            isShow.pack()

        def sign_up():
            isShow.forget()
            global frame, txtuser, txtid, txtfname, txtlname, txtpass, txtgender, txtrname, txtmail, txtphone, txtprofile, txtanswer
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

            # Label(frame, text='The profile of the Autistic :', bg=bg, fg=fg, font=fnt).grid(row=9, column=0)
            # Label(top, image=im).pack()
            txtuser = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svuser)
            txtid = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svId)
            txtfname = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svfname)
            txtlname = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svlname)
            txtpass = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svpass)
            txtgender = ttk.Combobox(frame, values=('Male', 'Female'), textvariable=svgender, state='readonly')
            txtrname = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svrname)
            txtmail = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svmail)
            txtphone = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svphone)
            # txtprofile = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svprofile)
            txtanswer = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svanswer)

            btns = ttk.Style()
            btns.configure('TButton', font=fnt, pady=pad, padding=pad)
            ttk.Button(frame, text='profile pic',
                       command=lambda: saveprofile(filedialog.askopenfilename(filetypes=[("Image File", '.png')]))) \
                .grid(row=10, column=0, pady=15)
            # ttk.Button(frame, text='Create new account', command=create).grid(row=11, column=1, pady=pad)
            # ttk.Button(frm, text='Exit Now', command=frm.destroy).grid(row=9, column=2, pady=pad)
            ttk.Button(frame, text='Back', command=f).grid(row=13, column=0, pady=8)
            ttk.Button(frame, text='Next', command=pageif).grid(row=13, column=3, pady=8)
            txtuser.grid(row=0, column=1, pady=pad)
            txtid.grid(row=1, column=1, pady=pad)
            txtfname.grid(row=2, column=1, pady=pad)
            txtlname.grid(row=3, column=1, pady=pad)
            txtpass.grid(row=4, column=1, pady=pad)
            txtgender.grid(row=5, column=1, pady=pad)
            txtrname.grid(row=6, column=1, pady=pad)
            txtmail.grid(row=7, column=1, pady=pad)
            txtphone.grid(row=8, column=1, pady=pad)
            txtanswer.grid(row=9, column=1, pady=pad)

            frame.pack(pady=pad)

        def saveprofile(name):
            global np, dp
            a = open(name, 'rb')
            np = name
            dp = a.read()

        def convp():
            cursor.execute("SELECT * FROM users WHERE user_name=?", (svuser.get(),))
            row = cursor.fetchall()
            for i in row:
                name = i[12]
                imager = i[13]
            global ddp
            if (name != None):
                b = open(name, 'wb')
                b.write(imager)
                ddp = PhotoImage(file=name)
                return ddp

            print(5)

        def newbord():
            print(1)
            isShow.forget()

            def insertimag(num):
                def choosepic(num):
                    def choose(key, name):
                        convertTbinary(key, name)
                        isShow1.destroy()

                    def allcat():

                        def funcB(N, K):
                            print(N)

                            def lastFuncc():

                                '''print(numImg)
                                root = Tk()
                                canvas = Canvas(root, width=300, height=300)
                                canvas.pack()
                                im = Image.open(numImg)
                                resized = im.resize((200, 200), Image.ANTIALIAS)
                                photo1 = ImageTk.PhotoImage(resized)
                                myvar = tk.Button(root, image=photo1)
                                myvar.image = photo1
                                myvar.pack()
                                root.mainloop()

                                global isShow
                                isShow=Frame(frm)
                                isShow=imageToInsert['im1']
                            '''

                                def convertToimage(name, imager):
                                    if (name != None):
                                        b = open(name, 'wb')
                                        b.write(imager)
                                        photonameList1.append(name)
                                        photo1Dic[name] = PhotoImage(file=name)

                                global imageNameInasertc
                                cursor.execute("SELECT * FROM category WHERE name=?", (N,))
                                y = cursor.fetchall()
                                for n in y:
                                    for i in range(1, 13, 2):
                                        convertToimage(n[i], n[i + 1])
                                print(photo1Dic)
                                for i in y:
                                    print(i[0])
                                    Fram(N, i[2], i[4], i[6], i[8], i[10], i[12], i[1], i[3], i[5], i[7], i[9], i[11])

                            def Fram(name, data1, data2, data3, data4, data5, data6, image1=None, image2=None,
                                     image3=None, image4=None, image5=None, image6=None):

                                global isShow2, catDic
                                isShow2.forget()
                                isShow2 = Frame(isShow1)
                                print(image1)
                                Label(isShow2, text=name).grid(row=0, columnspan=2, pady=20)
                                print(photo1Dic)
                                if image1:
                                    b = Button(isShow2, height="300", width="300", image=photo1Dic[image1],
                                               command=lambda: choose('im' + str(num), image1))
                                    b.grid(row=1, column=0)
                                if image2:
                                    c = Button(isShow2, height="300", width="300", image=photo1Dic[image2],
                                               command=lambda: choose('im' + str(num), image2))
                                    c.grid(row=1, column=1)
                                if image3:
                                    d = Button(isShow2, height="300", width="300", image=photo1Dic[image3],
                                               command=lambda: choose('im' + str(num), image3))
                                    d.grid(row=1, column=2)
                                if image4:
                                    t = Button(isShow2, height="300", width="300", image=photo1Dic[image4],
                                               command=lambda: choose('im' + str(num), image4))
                                    t.grid(row=2, column=0)
                                if image5:
                                    t = Button(isShow2, height="300", width="300", image=photo1Dic[image5],
                                               command=lambda: choose('im' + str(num), image5))
                                    t.grid(row=2, column=1)
                                if image6:
                                    t = Button(isShow2, height="300", width="300", image=photo1Dic[image6],
                                               command=lambda: choose('im' + str(num), image6))
                                    t.grid(row=2, column=2)
                                Button(isShow2, text="<- Back", bg="white", height="3", width="10", font="10",
                                       command=allcat).grid(
                                    row=3, column=0, padx=5, pady=80)
                                # if name in tuple(cat1Dic):
                                # cat1Dic[name].append(isShow2)
                                #### and insert to DB
                                # else:
                                # cat1Dic[name] = isShow2
                                # isShow2 = cat1Dic[name]
                                # print(cat1Dic)
                                isShow2.pack()

                            C = Button(isShow2, text=N, bg="white", height="3", width="15", font="20",
                                       command=lambda: lastFuncc())
                            C.bind('<Button-1>', lambda event, frame=isShow2, arg=N: bord(N))
                            C.grid(row=K, column=1, padx=30, pady=20)

                        global isShow2, row
                        isShow2.forget()

                        isShow2 = Frame(isShow1)

                        cursor.execute("SELECT * FROM category")
                        row = cursor.fetchall()
                        k = 0

                        for i in row:
                            funcB(i[0], k)
                            k += 1
                            '''
                            b=Button(isShow, text=y, bg="white", height="3", width="15", font="20")
                            b.bind('<Button-1>', lambda event, frame=isShow, arg=y: bord(y))
                            b.grid(row=k, column=1, padx=30, pady=20)
                            k+=1
                            '''
                        Button(isShow, text="<- Back", bg="white", height="3", width="10", font="10",
                               command=mainpage).grid(
                            row=k, column=0, padx=5, pady=80)

                        isShow2.pack()

                    global isShow2, isShow1

                    isShow1 = tk.Toplevel()
                    isShow2 = Frame(isShow1)

                    def comp():
                        global isShow2
                        convertTbinary('im' + str(num), filedialog.askopenfilename(filetypes=[("Image File", '.png')]))
                        isShow1.destroy()
                        insertimag(num)

                    def cat():
                        global isShow2
                        isShow2.forget()
                        allcat()

                    Button(isShow2, text="category", bg="white", height="5", width="20", font="25", command=cat).grid(
                        row=2, column=2, sticky=W, padx=30, pady=50)
                    Button(isShow2, text="from computer", bg="white", height="5", width="20", font="25",
                           command=comp).grid(row=3, column=2, sticky=W, padx=30, pady=50)
                    Button(isShow, text="<- Back", bg="white", height="3", width="10", font="10",
                           command=lambda: insertimag(num)).grid(
                        row=4, column=0, padx=5, pady=80)
                    isShow2.pack()

                def funcVoice(name):

                    fs = 44100  # Sample rate
                    seconds = 3  # Duration of recording
                    print("seeey")
                    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
                    sd.wait()  # Wait until recording is finished
                    file = name
                    write(file, fs, myrecording)  # Save as WAV file
                    global vvo
                    vvo = file
                    # playsound(file)

                def saveimb():
                    global isShow

                    # print(imageToInsert['im1'])
                    # isShow.forget()
                    if num == 1:
                        cursor.execute("UPDATE 'boards' SET nameim1=?,sound1=?,image1=? WHERE name=? ",
                                       (imageNameInasert['im1name'], vvo, imageToInsert['im1'], txtbord.get()))
                        conn.commit()
                    elif num == 2:
                        cursor.execute("UPDATE 'boards' SET nameim2=?,sound2=?,image2=? WHERE name=? ",
                                       (imageNameInasert['im2name'], vvo, imageToInsert['im2'], txtbord.get()))
                        conn.commit()
                    elif num == 3:
                        cursor.execute("UPDATE 'boards' SET nameim3=?,sound3=?,image3=? WHERE name=? ",
                                       (imageNameInasert['im3name'], vvo, imageToInsert['im3'], txtbord.get()))
                        conn.commit()
                    elif num == 4:
                        cursor.execute("UPDATE 'boards' SET nameim4=?,sound4=?,image4=? WHERE name=? ",
                                       (imageNameInasert['im4name'], vvo, imageToInsert['im4'], txtbord.get()))
                        conn.commit()
                    isShow.forget()
                    creatbord()

                    # for n in imageToInsert:
                    # convertToimage(imageNameInasert['im1' + 'name'], imageToInsert['im1'])
                    # Fram(name, imageNameInasert['im1name'])
                    # imageNameInasert['im1name'] = None
                    # ChooseBordOrCat()
                    # catDic[name][0].pack()
                    # isShow=catDic[name][0]

                global isShow
                isShow.forget()
                isShow = Frame(frm)
                Label(isShow, text='name of image:', bg="white", fg=fg, font=" impact 25").grid(row=0, column=2)
                lbl = ttk.Label(isShow, text='name of the pic?')
                lbl.config(font=fnt)
                nameim = ttk.Entry(isShow)
                nameim.config(font=fnt)
                nameim.grid(row=1, column=2)

                Button(isShow, text="Add voice  ", bg="white", height="5", width="10", font="20",
                       command=lambda: funcVoice("x" + str(num) + txtbord.get() + ".wav")).grid(row=2,
                                                                                                column=2,
                                                                                                sticky=W,
                                                                                                padx=90,
                                                                                                pady=60)

                Button(isShow, text="Add pic ", bg="white", height="5", width="10", font="20",
                       command=lambda: choosepic(num)).grid(row=4, column=2, sticky=W, padx=90, pady=60)
                ok = tk.Button(isShow, text=" save ", bg="white", height="3", width="5", font="20",
                               command=saveimb).grid(row=5, column=1, sticky=W, padx=20, pady=20)
                back = tk.Button(isShow, text=" <- Back ", bg="white", height="3", width="5", font="20",
                                 command=newbord).grid(row=5,
                                                       column=0,
                                                       sticky=W,
                                                       padx=20,
                                                       pady=20)

                isShow.pack()

            def setImage(im, namecat):
                global imi, isShow
                counter = 0
                isShow.forget()
                imi = im
                isShow = catDic[namecat][counter]
                isShow.pack()

            def save_B():
                cursor.execute("SELECT * FROM admins")
                x = cursor.fetchall()
                for i in x:
                    if svuser.get() == i[1]:
                        cursor.execute("INSERT INTO boards (name,username) VALUES(?,?)", (txtbord.get(), "everyone"))
                        conn.commit()
                        creatbord()
                        return
                cursor.execute("INSERT INTO boards (name,username) VALUES(?,?)", (txtbord.get(), svuser.get()))
                conn.commit()
                creatbord()

            def creatbord():
                def adminoruser():
                    cursor.execute("SELECT * FROM admins")
                    x = cursor.fetchall()
                    for i in x:
                        if svuser.get() == i[1]:
                            page1_admin()
                            return
                    mainpage()

                global isShow
                isShow.forget()
                isShow = Frame(frm)

                # cursor.execute("INSERT INTO boards (name) VALUES(?)", (txtbord.get(),))
                # conn.commit()
                Button(isShow, text="+1", bg="white", height="10", width="20", font="100",
                       command=lambda: insertimag(1)).grid(row=1, column=1, sticky=W, padx=60, pady=20)
                Button(isShow, text="+2", bg="white", height="10", width="20", font="100",
                       command=lambda: insertimag(2)).grid(row=1, column=4, sticky=W, padx=90, pady=20)
                Button(isShow, text="+3", bg="white", height="10", width="20", font="100",
                       command=lambda: insertimag(3)).grid(row=2, column=1, sticky=W, padx=60, pady=50)
                Button(isShow, text="+4", bg="white", height="10", width="20", font="100",
                       command=lambda: insertimag(4)).grid(row=2, column=4, sticky=W, padx=90, pady=100)
                Button(isShow, text="Save", bg="white", height="3", width="10", font="100",
                       command=lambda: adminoruser()).grid(row=3, column=4, sticky=W, padx=170, pady=20)
                back = tk.Button(isShow, text=" <- Back ", bg="white", height="3", width="10", font="100",
                                 command=namebord).grid(row=3, column=0, sticky=W, padx=20, pady=20)

                isShow.pack()

            def namebord():
                global isShow, txtbord
                isShow.forget()
                print(2)
                print(3)
                isShow = Frame(frm)
                B = ttk.Button(isShow, text="Enter", command=save_B)
                Label(isShow, text='board name:', font=fnt).pack()
                print(4)
                txtbord = ttk.Entry(isShow)
                txtbord.config(font=fnt)

                print(5)
                txtbord.pack()
                B.pack()

                Button(isShow, text="<- Back", bg="white", height="3", width="10", font="10", command=mainpage).pack()
                isShow.pack()
                # mainframe.pack()

            namebord()

        def bord(z):

            print(z)

            def voice(num):

                for i in row:
                    if i[0] == z:
                        if num == 3:
                            playsound(i[2])
                        elif num == 6:
                            playsound(i[5])
                        elif num == 9:
                            playsound(i[8])
                        elif num == 12:
                            playsound(i[11])

            # print(row)

            '''
            global isShow
            isShow.forget()
            isShow = Frame(frm)
            cursor.execute("SELECT * FROM boards WHERE name=?", (z,))
            row = cursor.fetchall()
            for i in row:
                j = 1
                print(i)
                lastFunc(i[3], 3)

                b1=Button(isShow, bg="white", height="10", width="20", font="100", image=i[3],command=lambda: voice(1)).grid(row=1, column=1, sticky=W, padx=60, pady=20)
                b2=Button(isShow, bg="white", height="10", width="20", font="100", image=i[6],command=lambda: voice(2)).grid(row=1, column=4, sticky=W, padx=90, pady=20)
                b3=Button(isShow, bg="white", height="10", width="20", font="100", image=i[9],command=lambda: voice(3)).grid(row=2, column=1, sticky=W, padx=60, pady=50)
                b4=Button(isShow, bg="white", height="10", width="20", font="100", image=i[12],command=lambda: voice(4)).grid(row=2, column=4, sticky=W, padx=90, pady=100)
                # Button(bordframe, text="Save", bg="white", height="3", width="10", font="100").grid(row=3, column=4,sticky=W, padx=170,pady=20)
                back = tk.Button(isShow, text=" <- Back ", bg="white", height="3", width="10", font="100",command=lambda: allboards()).grid(row=3,column=0,sticky=W,padx=20,pady=20)

                b1.image=convertToimage('name1.txt', i[3])
                b2.image=convertToimage('name2.txt', i[6])
                b3.image=convertToimage('name3.txt', i[9])
                b4.image=convertToimage('name4.txt', i[12])
                '''
            isShow.pack()

        def allboards():

            def funcB(N, K):
                print(N)

                def lastFunc():

                    '''print(numImg)
                    root = Tk()
                    canvas = Canvas(root, width=300, height=300)
                    canvas.pack()
                    im = Image.open(numImg)
                    resized = im.resize((200, 200), Image.ANTIALIAS)
                    photo1 = ImageTk.PhotoImage(resized)
                    myvar = tk.Button(root, image=photo1)
                    myvar.image = photo1
                    myvar.pack()
                    root.mainloop()

                    global isShow
                    isShow=Frame(frm)
                    isShow=imageToInsert['im1']
                '''
                    global imageNameInasert
                    cursor.execute("SELECT * FROM boards WHERE name=?", (N,))
                    y = cursor.fetchall()
                    for n in y:
                        for i in range(1, 11, 3):
                            convertToimage(n[i], n[i + 2])
                    print(photoDic)
                    cursor.execute("SELECT * FROM boards WHERE name=?", (N,))
                    x = cursor.fetchall()
                    for i in x:
                        print(i[0])
                        Fram(N, i[1], i[4], i[7], i[10])
                    imageNameInasert['im1name'], imageNameInasert['im2name'], imageNameInasert['im3name'], \
                    imageNameInasert[
                        'im4name'] = None, None, None, None

                def Fram(name, image1=None, image2=None, image3=None, image4=None):
                    def voice(num):
                        cursor.execute("SELECT * FROM boards WHERE name=?", (name,))
                        vo = cursor.fetchall()
                        for i in vo:
                            if i[0] == name:
                                if num == 1:
                                    playsound(i[2])
                                elif num == 2:
                                    playsound(i[5])
                                elif num == 3:
                                    playsound(i[8])
                                elif num == 4:
                                    playsound(i[11])

                    global isShow, catDic
                    isShow.forget()
                    isShow = Frame(frm)
                    print(image1)
                    Label(isShow, text=name).grid(row=0, columnspan=2, pady=20)
                    print(photoDic)
                    if image1:
                        b = Button(isShow, height="400", width="400", image=photoDic[image1], command=lambda: voice(1))
                        b.grid(row=1, column=0)
                    if image2:
                        c = Button(isShow, height="400", width="400", image=photoDic[image2], command=lambda: voice(2))
                        c.grid(row=1, column=1)
                    if image3:
                        d = Button(isShow, height="400", width="400", image=photoDic[image3], command=lambda: voice(3))
                        d.grid(row=2, column=0)
                    if image4:
                        t = Button(isShow, height="400", width="400", image=photoDic[image4], command=lambda: voice(4))
                        t.grid(row=2, column=1)
                    Button(isShow, text="<- Back", bg="white", height="3", width="10", font="10",
                           command=allboards).grid(
                        row=3, column=0, padx=5, pady=80)
                    if name in tuple(catDic):
                        catDic[name].append(isShow)
                        #### and insert to DB
                    else:
                        catDic[name] = isShow
                    isShow = catDic[name]
                    print(catDic)
                    isShow.pack()

                C = Button(isShow, text=N, bg="white", height="3", width="15", font="20", command=lambda: lastFunc())
                C.bind('<Button-1>', lambda event, frame=isShow, arg=N: bord(N))
                C.grid(row=K, column=1, padx=30, pady=20)

            global isShow, row
            isShow.forget()

            isShow = Frame(frm)

            cursor.execute("SELECT * FROM boards")
            row = cursor.fetchall()
            k = 0

            for i in row:
                if i[13] == svuser.get() or i[13] == "everyone":
                    funcB(i[0], k)
                    k += 1
                '''
                b=Button(isShow, text=y, bg="white", height="3", width="15", font="20")
                b.bind('<Button-1>', lambda event, frame=isShow, arg=y: bord(y))
                b.grid(row=k, column=1, padx=30, pady=20)
                k+=1
                '''
            Button(isShow, text="<- Back", bg="white", height="3", width="10", font="10", command=mainpage).grid(
                row=k, column=0, padx=5, pady=80)
            isShow.pack()

        def mainpage():

            global isShow
            isShow.forget()
            isShow = Frame(frm)
            '''
            create=ttk.Button(mainframe,text='Create a new board!',command= newbord)
            exi=ttk.Button(mainframe,text='An existing boards')
            setting=ttk.Button(mainframe,text='setting')
            profile=ttk.Button(mainframe,text='profile')
            profile.pack()
            create.pack()
            exi.pack()
            setting.pack()

            '''
            cursor.execute("SELECT * FROM users WHERE user_name=?", (svuser.get(),))
            row = cursor.fetchall()
            for i in row:
                proimg = i[12]
            # create = ttk.Button(mainframe, text='Create a new board!')

            Label(isShow, bg="white", font=fnt, height=200, width=200, image=convp()).grid(row=2, column=1, padx=300,
                                                                                           pady=10)
            Button(isShow, text="Setting", bg="white", font=fnt, command=settingpage).grid(row=8, column=1, padx=300,
                                                                                           pady=10)
            Button(isShow, text="Create a new board!", bg="white", font=fnt, command=newbord).grid(row=6, column=1,
                                                                                                   padx=300, pady=10)
            Button(isShow, text="An existing boards", bg="white", font=fnt, command=allboards).grid(row=4, column=1,
                                                                                                    padx=200, pady=10)
            # Button(mainframe, text="Profile", bg="white", font=fnt).grid(row=0, column=1, padx=200, pady=20)

            isShow.pack()

        def forget():
            global isShow
            isShow.forget()

            def returnpass():
                global isShow
                isShow.forget()
                isShow = Frame(frm)

                def checkpass():

                    if txtnew.get() == txt2.get():
                        account()
                    else:
                        messagebox.showinfo('', 'The passwords not matched!')
                        txtnew.focus()
                        txt2.focus()

                Label(isShow, text='New Password', font='impact 25').pack()

                lblnew = ttk.Label(isShow, text='Enter new password:')
                txtnew = ttk.Entry(isShow)
                lbl2 = ttk.Label(isShow, text='Enter the password one more time:')
                txt2 = ttk.Entry(isShow)
                change = ttk.Button(isShow, text='change password', command=checkpass)
                Button(isShow, text="<- Back", bg="white", height="3", width="10", font="10", command=question).grid(
                    row=4, column=0, padx=5, pady=80)
                lblnew.config(font=fnt)
                txtnew.config(font=fnt)
                lbl2.config(font=fnt)
                txt2.config(font=fnt)

                lblnew.pack()
                txtnew.pack()
                lbl2.pack()
                txt2.pack()
                change.pack()
                isShow.pack()

            def question():
                global isShow
                isShow.forget()
                isShow = Frame(frm)

                def forgetpass():

                    cursor.execute("SELECT * FROM 'users' ")
                    rows = cursor.fetchall()
                    for i in rows:
                        if txtid.get() == i[3] and txtanswer.get() == i[12]:
                            returnpass()
                            print(txtanswer.get())

                Label(isShow, text='Account security', font='impact 25').pack()

                lbl1 = ttk.Label(isShow, text='your id:')
                lbl = ttk.Label(isShow, text='what your primry school?')

                txtanswer = ttk.Entry(isShow)
                txtanswer.config(font=fnt)
                txtid = ttk.Entry(isShow)
                txtid.config(font=fnt)
                lbl1.config(font=fnt)
                lbl.config(font=fnt)
                Button(isShow, text="<- Back", bg="white", height="3", width="10", font="10", command=login).grid(
                    row=4, column=0, padx=5, pady=80)
                ok = ttk.Button(isShow, text='OK', command=forgetpass)

                lbl1.pack()
                txtid.pack()
                lbl.pack()
                txtanswer.pack()
                ok.pack()
                isShow.pack()

            question()

        def checkuser(name):

            cursor.execute("select * from 'users' where user_name=? ", (name,))
            if cursor.fetchone() is not None:
                return True
            return False

        def page2_admin():
            global r, isShow

            def funAzr():
                text = r.get()
                if checkuser(text) == True:
                    # page3_admin()
                    page4_admin()
                    # page5_admin()

                if checkuser(text) == False:
                    messagebox.showinfo('', 'Not found user!')

            isShow.forget()
            isShow = Frame(frm)
            Label(isShow, text='Enter username you want to search:', bg=bg, fg=fg, font=fnt).grid(row=10, column=1,
                                                                                                  padx=30,
                                                                                                  pady=120)
            r = Entry(isShow, bg="white", fg=fg, font=fnt, textvariable=svuser)
            r.grid(row=10, column=2, padx=30, pady=120)

            Button(isShow, text=" Search", bg="white", height="1", width="8", font="15", command=funAzr).grid(row=14,
                                                                                                              column=4,
                                                                                                              sticky=W,
                                                                                                              padx=30,
                                                                                                              pady=30)
            Button(isShow, text="<- Back", bg="white", height="3", width="10", font="10", command=page1_admin).grid(
                row=14, column=0, padx=5, pady=80)
            isShow.mainloop()

        def adminbord():
            global isShow
            isShow.forget()
            isShow = Frame(frm)
            Button(isShow, text="add a new board", bg="white", height="5", width="20", font="25", command=newbord).grid(
                row=2,
                column=2,
                sticky=W,
                padx=30,
                pady=50)
            Button(isShow, text="all boards", bg="white", height="5", width="20", font="25", command=allboards).grid(
                row=3,
                column=2,
                sticky=W,
                padx=30,
                pady=50)
            Button(isShow, text="<- Back", bg="white", height="3", width="10", font="10", command=page1_admin).grid(
                row=4, column=0, padx=5, pady=80)
            isShow.pack()

        def allcat():

            def funcB(N, K):
                print(N)

                def lastFuncc():

                    '''print(numImg)
                    root = Tk()
                    canvas = Canvas(root, width=300, height=300)
                    canvas.pack()
                    im = Image.open(numImg)
                    resized = im.resize((200, 200), Image.ANTIALIAS)
                    photo1 = ImageTk.PhotoImage(resized)
                    myvar = tk.Button(root, image=photo1)
                    myvar.image = photo1
                    myvar.pack()
                    root.mainloop()

                    global isShow
                    isShow=Frame(frm)
                    isShow=imageToInsert['im1']
                '''

                    def convertToimage(name, imager):
                        if (name != None):
                            b = open(name, 'wb')
                            b.write(imager)
                            photonameList1.append(name)
                            photo1Dic[name] = PhotoImage(file=name)

                    global imageNameInasertc
                    cursor.execute("SELECT * FROM category WHERE name=?", (N,))
                    y = cursor.fetchall()
                    for n in y:
                        for i in range(1, 13, 2):
                            convertToimage(n[i], n[i + 1])
                    print(photo1Dic)
                    for i in y:
                        print(i[0])
                        Fram(N, i[1], i[3], i[5], i[7], i[9], i[11])
                    imageNameInasert['im1name'], imageNameInasert['im2name'], imageNameInasert['im3name'], \
                    imageNameInasert[
                        'im4name'] = None, None, None, None

                def Fram(name, image1=None, image2=None, image3=None, image4=None, image5=None, image6=None):

                    global isShow, catDic
                    isShow.forget()
                    isShow = Frame(frm)
                    print(image1)
                    Label(isShow, text=name, height="10", width="20", ).grid(row=0, columnspan=2, pady=20)
                    print(photo1Dic)
                    if image1:
                        b = Button(isShow, height="300", width="300", image=photo1Dic[image1])
                        b.grid(row=1, column=0)
                    if image2:
                        c = Button(isShow, height="300", width="300", image=photo1Dic[image2])
                        c.grid(row=1, column=1)
                    if image3:
                        d = Button(isShow, height="300", width="300", image=photo1Dic[image3])
                        d.grid(row=1, column=2)
                    if image4:
                        t = Button(isShow, height="300", width="300", image=photo1Dic[image4])
                        t.grid(row=2, column=0)
                    if image5:
                        t = Button(isShow, height="300", width="300", image=photo1Dic[image5])
                        t.grid(row=2, column=1)
                    if image6:
                        t = Button(isShow, height="300", width="300", image=photo1Dic[image6])
                        t.grid(row=2, column=2)
                    Button(isShow, text="<- Back", bg="white", height="3", width="10", font="10",
                           command=allcat).grid(
                        row=3, column=0, padx=5, pady=80)
                    if name in tuple(cat1Dic):
                        cat1Dic[name].append(isShow)
                        #### and insert to DB
                    else:
                        cat1Dic[name] = isShow
                    isShow = cat1Dic[name]
                    print(cat1Dic)
                    isShow.pack()

                C = Button(isShow, text=N, bg="white", height="3", width="15", font="20", command=lambda: lastFuncc())
                C.bind('<Button-1>', lambda event, frame=isShow, arg=N: bord(N))
                C.grid(row=K, column=1, padx=30, pady=20)

            global isShow, row
            isShow.forget()

            isShow = Frame(frm)

            cursor.execute("SELECT * FROM category")
            row = cursor.fetchall()
            k = 0

            for i in row:
                funcB(i[0], k)
                k += 1
                '''
                b=Button(isShow, text=y, bg="white", height="3", width="15", font="20")
                b.bind('<Button-1>', lambda event, frame=isShow, arg=y: bord(y))
                b.grid(row=k, column=1, padx=30, pady=20)
                k+=1
                '''
            Button(isShow, text="<- Back", bg="white", height="3", width="10", font="10", command=admincat).grid(
                row=k, column=0, padx=5, pady=80)

            isShow.pack()

        def newcat():

            def saveimc(num):
                if num == 1:
                    cursor.execute("UPDATE 'category' SET c1name=?,image1=? WHERE name=? ",
                                   (imageNameInasertc['im1name'], imageToInsertc['im1'], txtcat.get()))
                    conn.commit()
                elif num == 2:
                    cursor.execute("UPDATE 'category' SET c2name=?,image2=? WHERE name=? ",
                                   (imageNameInasertc['im2name'], imageToInsertc['im2'], txtcat.get()))
                    conn.commit()
                elif num == 3:
                    cursor.execute("UPDATE 'category' SET c3name=?,image3=? WHERE name=? ",
                                   (imageNameInasertc['im3name'], imageToInsertc['im3'], txtcat.get()))
                    conn.commit()
                elif num == 4:
                    cursor.execute("UPDATE 'category' SET c4name=?,image4=? WHERE name=? ",
                                   (imageNameInasertc['im4name'], imageToInsertc['im4'], txtcat.get()))
                    conn.commit()
                elif num == 5:
                    cursor.execute("UPDATE 'category' SET c5name=?,image5=? WHERE name=? ",
                                   (imageNameInasertc['im5name'], imageToInsertc['im5'], txtcat.get()))
                    conn.commit()
                elif num == 6:
                    cursor.execute("UPDATE 'category' SET c6name=?,image6=? WHERE name=? ",
                                   (imageNameInasertc['im6name'], imageToInsertc['im6'], txtcat.get()))
                    conn.commit()

                # for n in imageToInsert:
                # convertToimage(imageNameInasert['im1' + 'name'], imageToInsert['im1'])
                # Fram(name, imageNameInasert['im1name'])
                # imageNameInasert['im1name'] = None
                # ChooseBordOrCat()
                # catDic[name][0].pack()
                # isShow=catDic[name][0]

            def setImage(im, namecat):
                global imi, isShow
                counter = 0
                isShow.forget()
                imi = im
                isShow = catDic[namecat][counter]
                isShow.pack()

            def save_C():

                cursor.execute("INSERT INTO category (name) VALUES(?)", (txtcat.get(),))
                conn.commit()
                creatcat()

            def convertTbinaryc(key, name, num):
                a = open(name, 'rb')
                imageNameInasertc[key + 'name'] = name

                imageToInsertc[key] = a.read()
                saveimc(num)

            def creatcat():
                global isShow
                isShow.forget()
                isShow = Frame(frm)

                # cursor.execute("INSERT INTO boards (name) VALUES(?)", (txtbord.get(),))
                # conn.commit()
                Button(isShow, text="+1", bg="white", height="10", width="20", font="100",
                       command=lambda: convertTbinaryc('im' + str(1),
                                                       filedialog.askopenfilename(filetypes=[("Image File", '.png')]),
                                                       1)).grid(row=1, column=0, sticky=W, padx=60, pady=20)
                Button(isShow, text="+2", bg="white", height="10", width="20", font="100",
                       command=lambda: convertTbinaryc('im' + str(2),
                                                       filedialog.askopenfilename(filetypes=[("Image File", '.png')]),
                                                       2)).grid(row=1, column=3, sticky=W, padx=90, pady=20)
                Button(isShow, text="+3", bg="white", height="10", width="20", font="100",
                       command=lambda: convertTbinaryc('im' + str(3),
                                                       filedialog.askopenfilename(filetypes=[("Image File", '.png')]),
                                                       3)).grid(row=1, column=5, sticky=W, padx=60, pady=50)
                Button(isShow, text="+4", bg="white", height="10", width="20", font="100",
                       command=lambda: convertTbinaryc('im' + str(4),
                                                       filedialog.askopenfilename(filetypes=[("Image File", '.png')]),
                                                       4)).grid(row=2, column=0, sticky=W, padx=90, pady=100)
                Button(isShow, text="+5", bg="white", height="10", width="20", font="100",
                       command=lambda: convertTbinaryc('im' + str(5),
                                                       filedialog.askopenfilename(filetypes=[("Image File", '.png')]),
                                                       4)).grid(row=2, column=3, sticky=W, padx=90, pady=100)
                Button(isShow, text="+6", bg="white", height="10", width="20", font="100",
                       command=lambda: convertTbinaryc('im' + str(6),
                                                       filedialog.askopenfilename(filetypes=[("Image File", '.png')]),
                                                       4)).grid(row=2, column=5, sticky=W, padx=90, pady=100)

                Button(isShow, text="Save", bg="white", height="3", width="10", font="100",
                       command=lambda: page1_admin()).grid(row=3, column=4, sticky=W, padx=170, pady=20)
                back = tk.Button(isShow, text=" <- Back ", bg="white", height="3", width="10", font="100",
                                 command=namecat).grid(row=3, column=0, sticky=W, padx=20, pady=20)

                isShow.pack()

            def namecat():
                global isShow, txtcat
                isShow.forget()
                print(2)
                print(3)
                isShow = Frame(frm)
                B = ttk.Button(isShow, text="Enter", command=save_C)
                Label(isShow, text='catigoria name:', font=fnt).pack()
                print(4)
                txtcat = ttk.Entry(isShow)
                txtcat.config(font=fnt)
                Button(isShow, text="<- Back", bg="white", height="3", width="10", font="10", command=admincat()).grid(
                    row=4, column=0, padx=5, pady=80)

                print(5)
                txtcat.pack()
                B.pack()

                back = ttk.Button(isShow, text=" <- Back ")
                back.pack()
                isShow.pack()
                # mainframe.pack()

            namecat()

        def admincat():
            global isShow
            isShow.forget()
            isShow = Frame(frm)
            Button(isShow, text="add a new catigoria", bg="white", height="5", width="20", font="25",
                   command=newcat).grid(
                row=2,
                column=2,
                sticky=W,
                padx=30,
                pady=50)
            Button(isShow, text="all catigorias", bg="white", height="5", width="20", font="25", command=allcat).grid(
                row=3,
                column=2,
                sticky=W,
                padx=30,
                pady=50)
            Button(isShow, text="<- Back", bg="white", height="3", width="10", font="10", command=page1_admin).grid(
                row=4, column=0, padx=5, pady=80)
            isShow.pack()

        def addadmin():
            global isShow
            isShow.forget()
            isShow = Frame(frm)

            def add():
                cursor.execute("INSERT INTO admins (username,password,first_name,last_name) VALUES(?,?,?,?)",
                               (svuser.get(), svpass.get(), svfname.get(), svlname.get()))
                conn.commit()
                page1_admin()

            Label(isShow, text="Enter user name:", font=fnt).grid(row=1, column=1)
            Entry(isShow, textvariable=svuser, font=fnt).grid(row=1, column=2)
            Label(isShow, text="Enter password:", font=fnt).grid(row=2, column=1)
            Entry(isShow, textvariable=svpass, font=fnt).grid(row=2, column=2)
            Label(isShow, text="Enter first name:", font=fnt).grid(row=3, column=1)
            Entry(isShow, textvariable=svfname, font=fnt).grid(row=3, column=2)
            Label(isShow, text="Enter last name:", font=fnt).grid(row=4, column=1)
            Entry(isShow, textvariable=svlname, font=fnt).grid(row=4, column=2)
            Button(isShow, text="add", bg="white", font=1, command=add).grid(row=5, column=2, padx=10, pady=10)
            Button(isShow, text="<- Back", bg="white", height="3", width="10", font="10", command=page1_admin).grid(
                row=6, column=0, padx=5, pady=80)
            isShow.pack()

        def page1_admin():
            global isShow
            isShow.forget()
            isShow = Frame(frm)

            Button(isShow, text="Search an User", bg="white", height="5", width="20", font="25",
                   command=page2_admin).grid(
                row=2, column=1, sticky=W, padx=30, pady=50)
            Button(isShow, text="boards", bg="white", height="5", width="20", font="25", command=adminbord).grid(row=2,
                                                                                                                 column=3,
                                                                                                                 sticky=W,
                                                                                                                 padx=30,
                                                                                                                 pady=50)
            Button(isShow, text="Catigoria", bg="green", height="5", width="20", font="25", command=admincat).grid(
                row=3, column=1,
                sticky=W,
                padx=30, pady=20)
            Button(isShow, text="Update the page explain ", bg="white", height="5", width="20", font="25",
                   command=explain).grid(row=3, column=2, sticky=W, padx=30, pady=20)
            # Button(page3, text="Birthday", bg="green", height="5", width="20", font="25").grid(row=3, column=3, sticky=W, padx=30,pady=20)
            # Button(frm, text="Delete an user ", bg="green", height="5", width="20", font="25").grid(row=4, column=2, sticky=W, padx=30, pady=20)
            Button(isShow, text="My design ", bg="green", height="5", width="20", font="25").grid(row=2, column=2,
                                                                                                  sticky=W,
                                                                                                  padx=30, pady=50)
            Button(isShow, text="add admin ", bg="green", height="5", width="20", font="25", command=addadmin).grid(
                row=3, column=3, sticky=W,
                padx=30, pady=50)

            isShow.pack()

        def explain():
            global isShow
            isShow.forget
            isShow = Frame(frm)
            Label(isShow, text='enter your new explain', bg=bg, fg=fg, font=fnt).grid(row=0, column=0)
            m = Entry(isShow, bg="white", fg=fg, font=fnt)
            m.grid(row=10, column=2, padx=30, pady=120)
            Button(isShow, text="Ok", bg="green", height="5", width="20", font="25",
                   command=lambda: HelpFunc(m.get())).grid(row=2, column=2, sticky=W,
                                                           padx=30, pady=50)
            Button(isShow, text="<- Back", bg="white", height="3", width="10", font="10", command=page1_admin).grid(
                row=4, column=0, padx=5, pady=80)
            isShow.pack()

        def page4_admin():
            global isShow
            isShow.forget()
            isShow = Frame(frm)
            text1 = "Happy Birthday ya qalbiy :) "
            Button(isShow, text="Delete an user", bg="white", height="5", width="20", font="25",
                   command=lambda: delete_user(r.get())).grid(row=3, column=1, sticky=W, padx=30, pady=20)
            Button(isShow, text="Wish a Happy Birthday", bg="white", height="5", width="20", font="25",
                   command=lambda: update_massage(text1, r.get())).grid(row=5, column=1, sticky=W, padx=30, pady=20)
            Button(isShow, text="Send A massage ", bg="white", height="5", width="20", font="25",
                   command=page5_admin).grid(
                row=7, column=1, sticky=W, padx=30, pady=20)
            Button(isShow, text="<- Back", bg="white", height="3", width="10", font="10", command=page1_admin).grid(
                row=7, column=0, padx=5, pady=80)

            page4.mainloop()

        def page5_admin():
            global isShow
            isShow.forget
            isShow = Frame(frm)
            Label(isShow, text='Enter your massage thats you want to send to user ', bg=bg, fg=fg, font=fnt).grid(
                row=10,
                column=1,
                padx=30,
                pady=120)
            m = Entry(isShow, bg="white", fg=fg, font=fnt, textvariable=svmassage)
            m.grid(row=10, column=2, padx=30, pady=120)
            Button(isShow, text="Send", bg="white", height="1", width="8", font="15",
                   command=lambda: update_massage(m.get(), r.get())).grid(row=14, column=4, sticky=W, padx=30, pady=30)
            Button(isShow, text="<- Back", bg="white", height="3", width="10", font="10", command=page4_admin).grid(
                row=14, column=0, padx=5, pady=80)
            # messagebox.showinfo('', 'The massage send!')

        def login():

            global isShow, svuser
            isShow.forget()
            isShow = Frame(frm)

            def check():
                print(svuser.get(), svpass.get())
                cursor.execute("select * from 'users' where user_name=(?) and password=(?) ",
                               (svuser.get(), svpass.get()))
                print(svuser.get(), svpass.get())
                if cursor.fetchone() is None:
                    cursor.execute("select * from 'admins' where username=(?) and password=(?) ",
                                   (svuser.get(), svpass.get()))
                    if cursor.fetchone() is None:
                        messagebox.showinfo('', 'Invalid Username or password!')

                    else:
                        page1_admin()
                else:

                    global id
                    cursor.execute("SELECT * FROM 'users' ")
                    rows = cursor.fetchall()
                    for i in rows:
                        if svuser.get() == i[6] and svpass.get() == i[7]:
                            id = i[3]
                    isShow.forget()
                    mainpage()

            Label(isShow, text="Enter user name:").grid(row=1, column=1)
            Entry(isShow, textvariable=svuser).grid(row=2, column=1)
            Label(isShow, text="Enter password:").grid(row=3, column=1)
            Entry(isShow, textvariable=svpass).grid(row=4, column=1)
            '''
            lblname=ttk.Label(loginFrame,text='Enter username:').grid(row=1,column=2,padx=10,pady=10)
            txtname=ttk.Entry(loginFrame).grid(row=2,column=2,padx=10,pady=10)
            lblpass=ttk.Label(loginFrame,text='Enter the password:').grid(row=3,column=2,padx=10,pady=10)
            txtpass=ttk.Entry(loginFrame).grid(row=4,column=2,padx=10,pady=10)
    '''
            Button(isShow, text='login', bg="white", font=5, command=check).grid(row=5, column=1, padx=10, pady=10)
            Button(isShow, text="forget password", bg="white", font=1, command=forget).grid(row=5, column=2, padx=10,
                                                                                            pady=10)
            Button(isShow, text="<- Back", bg="white", height="3", width="10", font="10", command=f).grid(
                row=5, column=0, padx=5, pady=80)
            isShow.pack()

        def f():
            global isShow, frame
            if frame:
                frame.forget()
            if isShow:
                isShow.forget()
            isShow = Frame(frm)
            Label(isShow, text="Choose Login Or Register", bg="blue", width="300")
            Label(isShow, text="").pack()
            Button(isShow, text="Login", height="2", width="30", command=login).pack()
            Label(isShow, text="").pack()
            Button(isShow, text="Register", height="2", width="30", command=sign_up).pack()
            Label(isShow, text="").pack()
            isShow.pack()
            isShow.mainloop()

        f()

    account()

acceptEng()