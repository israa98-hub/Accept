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

frame = None
catDic = {}
cat1Dic = {}
photonameList = []
lista = []
photoDic = {}
bordDic = {}
photonameList1 = []
photo1Dic = {}
lann=None
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



frm = tk.Tk()

fnt = ('tahoma', 60)
bg = '#ffffff'
bgtxt = '#00ff00'
fg = '#000000'
fw = 2000
fh = 800
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
svnpass=StringVar()
sv2=StringVar()
# svprofile = StringVar()
svanswer = StringVar()
svmassage = StringVar()
svlan = StringVar()


def Database():
    global conn, cursor
    conn = sqlite3.connect("Accept2.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS admins (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, first_name TEXT,last_name TEXT, massage TEXT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, first_name TEXT, last_name TEXT, id TEXT,responsible_name TEXT,Email Text,user_name TEXT, password TEXT,phone TEXT,gander TEXT,massage TEXT,answer TEXT,nameprofile TEXT,dataprofile TEXT,language TEXT)")
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS boards(name text,nameim1 text,sound1 blob,image1 text,nameim2 text,sound2 blob,image2 text,nameim3 text,sound3 blob,image3 text,nameim4 text,sound4 blob,image4 text,username text) ')
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS category(name text,c1name text,image1 text,c2name text,image2 text,c3name text,image3 text,c4name text,image4 text,c5name text,image5 text,c6name text,image6 text) ')

    conn.commit()


Database()
#cursor.execute("DROP TABLE users;")


def insert_board(name, id):
    cursor.execute("INSERT INTO boards (name,id) VALUES(?,?)", (name, id))
    conn.commit()


def delete_user(id):
    cursor.execute("DELETE FROM 'users' WHERE id=?", (id,))
    conn.commit()


i = IntVar()


def logout(frame):
    # Save in Data Base()
    svuser.set('')
    svpass.set('')
    frame.destroy()


def insert_user(first_name, last_name,id,responsible_name,Email,user_name, password,  gander, phone, answer,nameprofile, dataprofile):
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

import English as lang
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
        isShow.forget()
        isShow = Frame(frm)
        Label(isShow, text=lang.a, bg=bg, fg=fg, font='tahoma 20').grid(row=0, column=0, pady=20)
        Label(isShow, text=lang.b, bg=bg, fg=fg, font='tahoma 20').grid(row=3, column=0,
                                                                                            pady=20)
        Label(isShow, text=lang.c, bg=bg, fg=fg, font='tahoma 20').grid(row=5, column=0,
                                                                                           pady=20)
        Label(isShow, text=lang.d, bg=bg, fg=fg, font='tahoma 20').grid(row=7, column=0, pady=20)
        Label(isShow, text=lang.e, bg=bg, fg=fg, font='tahoma 20').grid(row=9, column=0, pady=20)
        Label(isShow, text=lang.f, bg=bg, fg=fg, font='tahoma 20').grid(row=11, column=0,
                                                                                           pady=20)
        Label(isShow, text=lang.g, bg=bg, fg=fg, font='tahoma 20').grid(row=13, column=0,
                                                                                                 pady=20)
        # Label(frame, text='The profile of the Autistic :', bg=bg, fg=fg, font=fnt).grid(row=9, column=0)
        # Label(top, image=im).pack()
        Entry(isShow, bg=bgtxt, fg=fg, font='tahoma 20', textvariable=svuser).grid(row=0, column=2)
        Entry(isShow, bg=bgtxt, fg=fg, font='tahoma 20', textvariable=svfname).grid(row=3, column=2)
        Entry(isShow, bg=bgtxt, fg=fg, font='tahoma 20', textvariable=svlname).grid(row=5, column=2)
        Entry(isShow, bg=bgtxt, fg=fg, font='tahoma 20', textvariable=svpass).grid(row=7, column=2)
        Entry(isShow, bg=bgtxt, fg=fg, font='tahoma 20', textvariable=svrname).grid(row=9, column=2)
        Entry(isShow, bg=bgtxt, fg=fg, font='tahoma 20', textvariable=svmail).grid(row=11, column=2)
        Entry(isShow, bg=bgtxt, fg=fg, font='tahoma 20', textvariable=svphone).grid(row=13, column=2)
        # txtprofile = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svprofile).grid(row=15,column=2)
        Button(isShow, text=lang.mainpage, bg="white", height="1", width="10", command=mainpage).grid(row=20, column=1,
                                                                                                     pady=20, padx=0)
        Button(isShow, text=lang.back, bg="white", height="3", width="10", command=settingpage).grid(row=20,
                                                                                                    column=0,
                                                                                                    pady=20,
                                                                                                    padx=0)
        Button(isShow, text=lang.update, bg="white", height="1", width="5", command=upusername).grid(row=0, column=4,
                                                                                                  pady=20, padx=10)
        Button(isShow, text=lang.update, bg="white", height="1", width="5", command=upfname).grid(row=3, column=4,
                                                                                               pady=20,
                                                                                               padx=10)
        Button(isShow, text=lang.update, bg="white", height="1", width="5", command=uplname).grid(row=5, column=4,
                                                                                               pady=20,
                                                                                               padx=10)
        Button(isShow, text=lang.update, bg="white", height="1", width="5", command=uppass).grid(row=7, column=4,
                                                                                              pady=20,
                                                                                              padx=10)
        Button(isShow, text=lang.update, bg="white", height="1", width="5", command=uprname).grid(row=9, column=4,
                                                                                               pady=20,
                                                                                               padx=10)
        Button(isShow, text=lang.update, bg="white", height="1", width="5", command=upmail).grid(row=11, column=4,
                                                                                              pady=20,
                                                                                              padx=10)
        Button(isShow, text=lang.update, bg="white", height="1", width="5", command=upphone).grid(row=13, column=4,
                                                                                               pady=20, padx=10)

        isShow.pack()
        isShow.mainloop()

    def create():
        global i,isShow,fr
        isShow.forget()
        if i.get() == 0:
            insert_user(svfname.get(), svlname.get(), svId.get(), svrname.get(), svmail.get(), svuser.get(),
                        svpass.get(), svgender.get(), svphone.get(), svanswer.get(), np, dp)
            fr.destroy()
            f()
        else:
            messagebox.showinfo('', "you want to agree the terms")

    def HelpFunc2():
        global isShow
        isShow.forget()
        isShow = Frame(frm)
        Label(isShow, text=exp, bg=bg, fg=fg, font=fnt).grid(row=2, column=2)
        Button(isShow, text=lang.back, bg="white", height="3", width="10", font="10", command=settingpage).grid(
            row=4, column=0, padx=5, pady=80)

        isShow.pack()

    def HelpFunc(texthelp):
        global isShow
        isShow.forget()
        isShow = Frame(frm)
        Label(isShow, text=lang.h, bg=bg, fg=fg, font=fnt).grid(row=3, column=0, pady=20)
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
            global fr
            ttt =lang.tt
            fr = tk.Tk()
            fnt = ('tahoma', 12)
            bg = 'white'
            bgtxt = 'white'
            fg = 'black'
            fw = 650
            fh = 400
            x = (frm.winfo_screenwidth() - fw) / 2
            y = (frm.winfo_screenheight() - fh) / 2 - 50
            pad = 10

            fr.geometry('%dx%d+%d+%d' % (fw, fh, x, y))
            fr.title('Users')
            fr.config(bg=bg)
            Label(fr, text=ttt, bg=bg, fg=fg, font=fnt).grid(row=0, column=0)
            c = Checkbutton(fr, text=lang.i, variable=i, onvalue="checked").grid(
                row=11, column=0, pady=pad)
            Button(fr, text=lang.j, command=create).grid(row=13, column=3, pady=pad)
            fr.mainloop()

    def sendmess():
        global isShow
        isShow.forget()
        isShow = Frame(frm)

        def send():
            cursor.execute("UPDATE admins SET massage=?", (svmassage.get(),))
            conn.commit()
            mainpage()

        Label(isShow, text=lang.k, font=fnt).grid(row=1, column=1)
        Entry(isShow, font=fnt, textvariable=svmassage).grid(row=2, column=1)
        Button(isShow, text=lang.l, bg="white", height="3", width="10", font=fnt, command=send).grid(row=4,
                                                                                                     column=2,
                                                                                                     padx=100,
                                                                                                     pady=20)
        Button(isShow, text=lang.back, bg="white", height="3", width="10", font="10", command=settingpage).grid(
            row=4, column=0, padx=5, pady=80)
        isShow.pack()

    def lang1():
        global isShow, svlan
        isShow.forget()
        isShow = Frame(frm)

        def chooslan():
            isShow.forget()
            if svlan.get() == 'English':
                cursor.execute("UPDATE users SET language=? WHERE user_name=? ",('English',svuser.get()))
                conn.commit()
                acceptEng()
            elif svlan.get() == 'Arabic':
                cursor.execute("UPDATE users SET language=? WHERE user_name=? ", ('Arabic', svuser.get()))
                conn.commit()
                acceptArab()
            elif svlan.get() == 'Hebrew':
                cursor.execute("UPDATE users SET language=? WHERE user_name=? ", ('Hebrew', svuser.get()))
                conn.commit()
                acceptHeb()

        txtlan = ttk.Combobox(isShow, values=(lang.eng, lang.arab, lang.heb), textvariable=svlan,
                              state='readonly').grid(row=1, column=1, pady=pad)
        Button(isShow, text=lang.m, bg="white", height="3", width="10", font="10", command=chooslan).grid(
            row=3, column=1, padx=5, pady=80)
        Button(isShow, text=lang.back, bg="white", height="3", width="10", font="10", command=settingpage).grid(
            row=4, column=0, padx=5, pady=80)
        isShow.pack()

    def acceptEng():
        global lang
        import English as lang
        settingpage()

    def acceptArab():
        global lang
        import Arabic as lang
        account()

    def acceptHeb():
        global lang
        import Hebrew as lang
        settingpage()




    def settingpage():
        global isShow
        isShow.forget()
        isShow = Frame(frm)

        Button(isShow, text=lang.n, bg="white", height="6", width="30", font='tahoma 10', command=lambda: lang1()).grid(
            row=4, column=1,
            padx=100, pady=20)
        Button(isShow, text=lang.o, bg="white", height="6", width="30", font='tahoma 10', command=sendmess).grid(row=6,
                                                                                                            column=1,
                                                                                                            padx=100,
                                                                                                            pady=20)
        Button(isShow, text=lang.update, bg="white", height="6", width="30", font='tahoma 10', command=updatepro).grid(row=8,
                                                                                                            column=1,
                                                                                                            padx=100,
                                                                                                            pady=20)
        Button(isShow, text=lang.p, bg="white", height="6", width="30", font='tahoma 10', command=HelpFunc2).grid(row=2,
                                                                                                            column=1,
                                                                                                            padx=100,
                                                                                                            pady=20)
        # Button(isShow, text="Edit Profile", bg="white", height="6", width="30", font="50",command=updatepro).grid(row=0, column=1, padx=100, pady=20)
        Button(isShow, text=lang.back, bg="white", height="3", width="10", font="10", command=mainpage).grid(
            row=10, column=0, padx=5, pady=80)

        isShow.pack()

    def sign_up():
        isShow.forget()
        global frame, txtuser, txtid, txtfname, txtlname, txtpass, txtgender, txtrname, txtmail, txtphone, txtprofile, txtanswer
        frame = Frame(frm, bg=bg)
        Label(frame, text='user name:', bg=bg, fg=fg, font='tahoma 20').grid(row=0, column=0)
        Label(frame, text='Autistic ID number:', bg=bg, fg=fg, font='tahoma 20').grid(row=1, column=0)
        Label(frame, text='The first name of the autistic :', bg=bg, fg=fg, font='tahoma 20').grid(row=2, column=0)
        Label(frame, text='The last name of the autistic :', bg=bg, fg=fg, font='tahoma 20').grid(row=3, column=0)
        Label(frame, text='The password :', bg=bg, fg=fg, font='tahoma 20').grid(row=4, column=0)
        Label(frame, text='The gender of the autistic: ', bg=bg, fg=fg, font='tahoma 20').grid(row=5, column=0)
        Label(frame, text='The name of the responsible :', bg=bg, fg=fg, font='tahoma 20').grid(row=6, column=0)
        Label(frame, text='The E-mail of the responsible :', bg=bg, fg=fg, font='tahoma 20').grid(row=7, column=0)
        Label(frame, text='The number phone of the responsible :', bg=bg, fg=fg, font='tahoma 20').grid(row=8, column=0)
        Label(frame, text='what your Primary School? ', bg=bg, fg=fg, font='tahoma 20').grid(row=9, column=0)
        txtuser = Entry(frame, bg="WHITE", fg=fg, font='tahoma 20', textvariable=svuser)
        txtid = Entry(frame, bg="WHITE", fg=fg, font='tahoma 20', textvariable=svId)
        txtfname = Entry(frame, bg="WHITE", fg=fg, font='tahoma 20', textvariable=svfname)
        txtlname = Entry(frame, bg="WHITE", fg=fg, font='tahoma 20', textvariable=svlname)
        txtpass = Entry(frame, bg="WHITE", fg=fg, font='tahoma 20', textvariable=svpass)
        txtgender = ttk.Combobox(frame, values=('Male', 'Female'), font='tahoma 10',textvariable=svgender, state='readonly')
        txtrname = Entry(frame, bg="WHITE", fg=fg, font='tahoma 20', textvariable=svrname)
        txtmail = Entry(frame, bg="WHITE", fg=fg, font='tahoma 20', textvariable=svmail)
        txtphone = Entry(frame, bg="WHITE", fg=fg, font='tahoma 20', textvariable=svphone)
        txtanswer = Entry(frame, bg="WHITE", fg=fg, font='tahoma 20', textvariable=svanswer)
        btns = ttk.Style()
        btns.configure('TButton', font='tahoma 20', pady=pad, padding=pad)
        ttk.Button(frame, text=lang.q,
                   command=lambda: saveprofile(filedialog.askopenfilename(filetypes=[("Image File", '.png')]))) \
            .grid(row=10, column=0, pady=15)
        # ttk.Button(frame, text='Create new account', command=create).grid(row=11, column=1, pady=pad)
        # ttk.Button(frm, text='Exit Now', command=frm.destroy).grid(row=9, column=2, pady=pad)
        ttk.Button(frame, text=lang.back, command=f).grid(row=13, column=0, pady=8)
        ttk.Button(frame, text=lang.r, command=pageif).grid(row=13, column=3, pady=8)
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
                            Button(isShow2, text=lang.back, bg="white", height="3", width="10", font="10",
                                   command=allcat).grid(
                                row=3, column=0, padx=5, pady=80)
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
                    Button(isShow2, text=lang.back, bg="white", height="3", width="10", font="10",
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

                Button(isShow2, text=lang.s, bg="white", height="5", width="20", font="25", command=cat).grid(
                    row=2, column=2, sticky=W, padx=30, pady=50)
                Button(isShow2, text=lang.t, bg="white", height="5", width="20", font="25",
                       command=comp).grid(row=3, column=2, sticky=W, padx=30, pady=50)
                Button(isShow2, text=lang.back, bg="white", height="3", width="10", font="10",
                       command=lambda: insertimag(num)).grid(row=4, column=0, padx=5, pady=80)
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
            Label(isShow, text=lang.u,  fg=fg, font='tahoma 30').grid(row=0, column=2)
            nameim = ttk.Entry(isShow)
            nameim.config(font='tahoma 30')
            nameim.grid(row=1, column=2)

            Button(isShow, text=lang.v, bg="white", height="5", width="10", font='tahoma 30',
                   command=lambda: funcVoice("x" + str(num) + txtbord.get() + ".wav")).grid(row=2,
                                                                                            column=2,
                                                                                            sticky=W,
                                                                                            padx=9,
                                                                                            pady=6)

            Button(isShow, text=lang.w, bg="white", height="5", width="10", font='tahoma 30',
                   command=lambda: choosepic(num)).grid(row=4, column=2, sticky=W, padx=9, pady=6)
            ok = tk.Button(isShow, text=lang.x, bg="white", height="3", width="5", font='tahoma 20',
                           command=saveimb).grid(row=5, column=1, sticky=W, padx=20, pady=20)
            back = tk.Button(isShow, text=lang.back, bg="white", height="3", width="5", font="20",
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
            Button(isShow, text="+1", bg="white", height="10", width="25", font="100",
                   command=lambda: insertimag(1)).grid(row=1, column=1, sticky=W, padx=10, pady=5)
            Button(isShow, text="+2", bg="white", height="10", width="25", font="100",
                   command=lambda: insertimag(2)).grid(row=1, column=4, sticky=W, padx=10, pady=5)
            Button(isShow, text="+3", bg="white", height="10", width="25", font="100",
                   command=lambda: insertimag(3)).grid(row=2, column=1, sticky=W, padx=10, pady=5)
            Button(isShow, text="+4", bg="white", height="10", width="25", font="100",
                   command=lambda: insertimag(4)).grid(row=2, column=4, sticky=W, padx=10, pady=5)
            Button(isShow, text=lang.x, bg="white", height="3", width="10", font="100",
                   command=lambda: adminoruser()).grid(row=3, column=4, sticky=W, padx=10, pady=10)
            back = tk.Button(isShow, text=lang.back, bg="white", height="3", width="10", font="100",
                             command=namebord).grid(row=3, column=0, sticky=W, padx=10, pady=10)

            isShow.pack()

        def namebord():
            global isShow, txtbord
            isShow.forget()
            isShow = Frame(frm)
            Button(isShow, text=lang.y,font=fnt, command=save_B).grid(row=6,column=1)
            Label(isShow, text=lang.z, font=fnt).grid(row=2,column=1)
            txtbord = ttk.Entry(isShow)
            txtbord.config(font=fnt)
            txtbord.grid(row=4,column=1)

            Button(isShow, text=lang.back, bg="white", height="3", width="10", font="10", command=mainpage).grid(row=8, column=0)
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
        isShow.pack()

    def allboards():

        def funcB(N, K):
            print(N)

            def lastFunc():
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
                Label(isShow, text=name,font='tahoma 40').grid(row=0, columnspan=2, pady=20)
                if image1:
                    b = Button(isShow, height="300", width="300", image=photoDic[image1], command=lambda: voice(1))
                    b.grid(row=1, column=0,padx=10,pady=10)
                if image2:
                    c = Button(isShow, height="300", width="300", image=photoDic[image2], command=lambda: voice(2))
                    c.grid(row=1, column=1)
                if image3:
                    d = Button(isShow, height="300", width="300", image=photoDic[image3], command=lambda: voice(3))
                    d.grid(row=2, column=0)
                if image4:
                    t = Button(isShow, height="300", width="300", image=photoDic[image4], command=lambda: voice(4))
                    t.grid(row=2, column=1)
                Button(isShow, text=lang.back, bg="white", height="3", width="10", font="10",command=allboards).grid(
                    row=3, column=0, padx=5, pady=10)
                isShow.pack()
            C = Button(isShow, text=N, bg="white", height="3", width="50", font='tahoma 10', command=lambda: lastFunc())
            C.bind('<Button-1>', lambda event, frame=isShow, arg=N: bord(N))
            C.grid(row=K, column=1, padx=5, pady=5)
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
        Button(isShow, text=lang.back, bg="white", height="3", width="10", font="10", command=mainpage).grid(
            row=k, column=0, padx=5, pady=80)
        isShow.pack()

    def mainpage():
        global isShow,lann
        if lann=='English':
            acceptEng()
        if lann=='Hebrew':
            acceptHeb()
        if lann=='Arabic':
            acceptArab()
        isShow.forget()
        isShow = Frame(frm)
        cursor.execute("SELECT * FROM users WHERE user_name=?", (svuser.get(),))
        row = cursor.fetchall()
        for i in row:
            proimg = i[12]
        Label(isShow, bg="white", font=fnt, height=200, width=250, image=convp()).grid(row=2, column=1, padx=300,
                                                                                       pady=10)
        Button(isShow, text=lang.aa, bg="white", font='tahoma 40', command=settingpage).grid(row=8, column=1, padx=300,
                                                                                       pady=10)
        Button(isShow, text=lang.bb, bg="white", font='tahoma 40', command=newbord).grid(row=6, column=1,
                                                                                               padx=300, pady=10)
        Button(isShow, text=lang.cc, bg="white", font='tahoma 40', command=allboards).grid(row=4, column=1,
                                                                                                padx=200, pady=10)
        Button(isShow, text=lang.logout, bg="white", font='tahoma 40',command=lambda: logout(frm)).grid(row=10, column=1,padx=20,pady=10)
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

                if svnpass.get() == sv2.get():
                    print(svId.get())
                    print(svnpass.get())
                    cursor.execute("UPDATE 'users' SET password=? WHERE id=?", (sv2.get(), svId.get()))
                    conn.commit()
                    f()
                else:
                    messagebox.showinfo('', 'The passwords not matched!')
                    svnpass.focus()
                    sv2.focus()

            Label(isShow, text=lang.dd, font='impact 50').grid(row=0, column=1, padx=5, pady=10)

            lblnew = ttk.Label(isShow, text=lang.ee,font=fnt).grid(row=1, column=1, padx=5, pady=10)
            txtnew = ttk.Entry(isShow,font=fnt,textvariable=svnpass).grid(row=2, column=1, padx=5, pady=10)
            lbl2 = ttk.Label(isShow, text=lang.ff,font=fnt).grid(row=3, column=1, padx=5, pady=10)
            txt2 = ttk.Entry(isShow,font=fnt, textvariable=sv2).grid(row=4, column=1, padx=5, pady=10)
            Button(isShow, text=lang.gg,bg="white",height="3", width="15",font="20", command=checkpass).grid(row=5, column=1, padx=5, pady=10)
            Button(isShow, text=lang.back, bg="white", height="3", width="10", font="10", command=question).grid(row=5, column=0, padx=5, pady=80)

            isShow.pack()

        def question():
            global isShow
            isShow.forget()
            isShow = Frame(frm)

            def forgetpass():

                cursor.execute("SELECT * FROM 'users' ")
                rows = cursor.fetchall()
                for i in rows:
                    if svId.get() == i[3] and svanswer.get() == i[11]:
                        returnpass()

            Label(isShow, text=lang.hh, font='impact 50').grid(row=0, column=1, padx=5, pady=10)
            lbl1 = tk.Label(isShow, text=lang.ii,font=fnt).grid(row=1, column=1, padx=5, pady=10)
            lbl = tk.Label(isShow, text=lang.jj,font=fnt).grid(row=3, column=1, padx=5, pady=10)
            txtanswer =ttk.Entry(isShow,font=fnt,textvariable=svanswer).grid(row=4, column=1, padx=5, pady=10)
            txtid = ttk.Entry(isShow,font=fnt,textvariable=svId).grid(row=2, column=1, padx=5, pady=10)
            Button(isShow, text=lang.back, bg="white", height="5", width="12", font="10", command=login).grid(row=5, column=0, padx=5, pady=10)
            Button(isShow, text=lang.kk,bg=bg,height="5", width="15", font="14", command=forgetpass).grid(row=5, column=1, padx=5, pady=10)


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
                page4_admin()
            if checkuser(text) == False:
                messagebox.showinfo('', 'Not found user!')
        isShow.forget()
        isShow = Frame(frm)
        Label(isShow, text=lang.ll, bg=bg, fg=fg, font=fnt).grid(row=10, column=1,
                                                                                              padx=30,
                                                                                              pady=120)
        r = Entry(isShow, bg="white", fg=fg, font=fnt, textvariable=svuser)
        r.grid(row=10, column=2, padx=30, pady=120)

        Button(isShow, text=lang.mm, bg="white", height="1", width="8", font="15", command=funAzr).grid(row=14,
                                                                                                          column=4,
                                                                                                          sticky=W,
                                                                                                          padx=30,
                                                                                                          pady=30)
        Button(isShow, text=lang.back, bg="white", height="3", width="10", font="10", command=page1_admin).grid(
            row=14, column=0, padx=5, pady=80)
        isShow.mainloop()

    def adminbord():
        global isShow
        isShow.forget()
        isShow = Frame(frm)
        Button(isShow, text=lang.nn, bg="white", height="5", width="20", font="25", command=newbord).grid(
            row=2,
            column=2,
            sticky=W,
            padx=30,
            pady=50)
        Button(isShow, text=lang.oo, bg="white", height="5", width="20", font="25", command=allboards).grid(
            row=3,
            column=2,
            sticky=W,
            padx=30,
            pady=50)
        Button(isShow, text=lang.back, bg="white", height="3", width="10", font="10", command=page1_admin).grid(
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
                Button(isShow, text=lang.back, bg="white", height="3", width="10", font="10",
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
        Button(isShow, text=lang.back, bg="white", height="3", width="10", font="10", command=admincat).grid(
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
            Button(isShow, text=lang.x, bg="white", height="3", width="10", font="100",
                   command=lambda: page1_admin()).grid(row=3, column=4, sticky=W, padx=170, pady=20)
            back = tk.Button(isShow, text=lang.back, bg="white", height="3", width="10", font="100",
                             command=namecat).grid(row=3, column=0, sticky=W, padx=20, pady=20)
            isShow.pack()
        def namecat():
            global isShow, txtcat
            isShow.forget()
            isShow = Frame(frm)
            B = ttk.Button(isShow, text=lang.y, command=save_C)
            Label(isShow, text=lang.pp, font=fnt).pack()
            print(4)
            txtcat = ttk.Entry(isShow)
            txtcat.config(font=fnt)
            Button(isShow, text=lang.back, bg="white", height="3", width="10", font="10", command=admincat()).grid(
                row=4, column=0, padx=5, pady=80)
            txtcat.pack()
            B.pack()
            back = ttk.Button(isShow, text=lang.back)
            back.pack()
            isShow.pack()
        namecat()

    def admincat():
        global isShow
        isShow.forget()
        isShow = Frame(frm)
        Button(isShow, text=lang.qq, bg="white", height="5", width="20", font="25",
               command=newcat).grid(
            row=2,
            column=2,
            sticky=W,
            padx=30,
            pady=50)
        Button(isShow, text=lang.rr, bg="white", height="5", width="20", font="25", command=allcat).grid(
            row=3,
            column=2,
            sticky=W,
            padx=30,
            pady=50)
        Button(isShow, text=lang.back, bg="white", height="3", width="10", font="10", command=page1_admin).grid(
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

        Label(isShow, text=lang.ss, font=fnt).grid(row=1, column=1)
        Entry(isShow, textvariable=svuser, font=fnt).grid(row=1, column=2)
        Label(isShow, text=lang.tt, font=fnt).grid(row=2, column=1)
        Entry(isShow, textvariable=svpass, font=fnt).grid(row=2, column=2)
        Label(isShow, text=lang.uu, font=fnt).grid(row=3, column=1)
        Entry(isShow, textvariable=svfname, font=fnt).grid(row=3, column=2)
        Label(isShow, text=lang.vv, font=fnt).grid(row=4, column=1)
        Entry(isShow, textvariable=svlname, font=fnt).grid(row=4, column=2)
        Button(isShow, text=lang.ww, bg="white", font=1, command=add).grid(row=5, column=2, padx=10, pady=10)
        Button(isShow, text=lang.back, bg="white", height="3", width="10", font="10", command=page1_admin).grid(
            row=6, column=0, padx=5, pady=80)
        isShow.pack()

    def page1_admin():
        global isShow
        isShow.forget()
        isShow = Frame(frm)

        Button(isShow, text=lang.xx, bg="white", height="5", width="20", font="25",
               command=page2_admin).grid(
            row=2, column=1, sticky=W, padx=30, pady=50)
        Button(isShow, text=lang.yy, bg="white", height="5", width="20", font="25", command=adminbord).grid(row=2,
                                                                                                             column=3,
                                                                                                             sticky=W,
                                                                                                             padx=30,
                                                                                                             pady=50)
        Button(isShow, text=lang.zz, bg="green", height="5", width="20", font="25", command=admincat).grid(
            row=3, column=1,
            sticky=W,
            padx=30, pady=20)
        Button(isShow, text=lang.aaa, bg="white", height="5", width="20", font="25",
               command=explain).grid(row=3, column=2, sticky=W, padx=30, pady=20)
        # Button(page3, text="Birthday", bg="green", height="5", width="20", font="25").grid(row=3, column=3, sticky=W, padx=30,pady=20)
        # Button(frm, text="Delete an user ", bg="green", height="5", width="20", font="25").grid(row=4, column=2, sticky=W, padx=30, pady=20)
        Button(isShow, text=lang.bbb, bg="green", height="5", width="20", font="25").grid(row=2, column=2,
                                                                                              sticky=W,
                                                                                              padx=30, pady=50)
        Button(isShow, text=lang.ccc, bg="green", height="5", width="20", font="25", command=addadmin).grid(
            row=3, column=3, sticky=W,
            padx=30, pady=50)

        isShow.pack()

    def explain():
        global isShow
        isShow.forget
        isShow = Frame(frm)
        Label(isShow, text=lang.ddd, bg=bg, fg=fg, font=fnt).grid(row=0, column=0)
        m = Entry(isShow, bg="white", fg=fg, font=fnt)
        m.grid(row=10, column=2, padx=30, pady=120)
        Button(isShow, text=lang.eee, bg="green", height="5", width="20", font="25",
               command=lambda: HelpFunc(m.get())).grid(row=2, column=2, sticky=W,
                                                       padx=30, pady=50)
        Button(isShow, text=lang.back, bg="white", height="3", width="10", font="10", command=page1_admin).grid(
            row=4, column=0, padx=5, pady=80)
        isShow.pack()

    def page4_admin():
        global isShow
        isShow.forget()
        isShow = Frame(frm)
        text1 = lang.fff
        Button(isShow, text=lang.ggg, bg="white", height="5", width="20", font="25",
               command=lambda: delete_user(r.get())).grid(row=3, column=1, sticky=W, padx=30, pady=20)
        Button(isShow, text=lang.hhh, bg="white", height="5", width="20", font="25",
               command=lambda: update_massage(text1, r.get())).grid(row=5, column=1, sticky=W, padx=30, pady=20)
        Button(isShow, text=lang.iii, bg="white", height="5", width="20", font="25",
               command=page5_admin).grid(
            row=7, column=1, sticky=W, padx=30, pady=20)
        Button(isShow, text=lang.back, bg="white", height="3", width="10", font="10", command=page1_admin).grid(
            row=7, column=0, padx=5, pady=80)

        isShow.mainloop()

    def page5_admin():
        global isShow
        isShow.forget
        isShow = Frame(frm)
        Label(isShow, text=lang.jjj, bg=bg, fg=fg, font=fnt).grid(
            row=10,
            column=1,
            padx=30,
            pady=120)
        m = Entry(isShow, bg="white", fg=fg, font=fnt, textvariable=svmassage)
        m.grid(row=10, column=2, padx=30, pady=120)
        Button(isShow, text=lang.kkk, bg="white", height="1", width="8", font="15",
               command=lambda: update_massage(m.get(), r.get())).grid(row=14, column=4, sticky=W, padx=30, pady=30)
        Button(isShow, text=lang.back, bg="white", height="3", width="10", font="10", command=page4_admin).grid(
            row=14, column=0, padx=5, pady=80)
        # messagebox.showinfo('', 'The massage send!')

    def login():

        global isShow, svuser,frame
        isShow.forget()
        if frame:
            frame.forget()
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

                global id,lann
                cursor.execute("SELECT * FROM 'users' ")
                rows = cursor.fetchall()
                for i in rows:
                    if svuser.get() == i[6] and svpass.get() == i[7]:
                        id = i[3]
                        lann=i[14]

                isShow.forget()

                mainpage()

        Label(isShow, text=lang.lll,font=fnt).grid(row=1, column=1)
        Entry(isShow, textvariable=svuser,font=fnt).grid(row=2, column=1)
        Label(isShow, text=lang.mmm,font=fnt).grid(row=3, column=1)
        Entry(isShow, textvariable=svpass,font=fnt).grid(row=4, column=1)
        Button(isShow, text=lang.nnn, bg="white",font=fnt, command=check).grid(row=5, column=1, padx=5, pady=10)
        Button(isShow, text=lang.ooo, bg="white", font='tahoma 30', command=forget).grid(row=5, column=2, padx=5,
                                                                                        pady=10)
        Button(isShow, text=lang.back, bg="white", height="3", width="10", font='tahoma 30', command=f).grid(
            row=5, column=0, padx=5, pady=80)
        isShow.pack()

    def f():
        global isShow, frame
        if frame:
            frame.forget()
        if isShow:
            isShow.forget()
        isShow = Frame(frm)
        Label(isShow, text=lang.ppp, bg="blue", width="300",font=fnt).pack()
        Label(isShow, text="").pack()
        Button(isShow, text=lang.qqq, height="2", width="15",font=fnt, command=login).pack()
        Label(isShow, text="").pack()
        Button(isShow, text=lang.rrr, height=2, width="15",font=fnt, command=sign_up).pack()
        Label(isShow, text="").pack()
        isShow.pack()
        isShow.mainloop()

    f()


account()