import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
from playsound import playsound
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from tkinter import filedialog
import datetime


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
fh = 600
x = (frm.winfo_screenwidth() - fw) / 2
y = (frm.winfo_screenheight() - fh) / 2 - 50
pad = 10

frm.geometry('%dx%d+%d+%d' % (fw, fh, x, y))
#frm.title('Users')
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

#svprofile = StringVar()
svanswer = StringVar()
svmassage=StringVar()

def Database():
    global conn, cursor
    conn = sqlite3.connect("Accept.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS admins (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, first_name TEXT,last_name TEXT, massage TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS users (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, first_name TEXT, last_name TEXT, id TEXT,responsible_name TEXT,Email Text,user_name TEXT, password TEXT,phone TEXT,gander TEXT,massage TEXT,answer TEXT)")
    cursor.execute('CREATE TABLE IF NOT EXISTS boards(name text,nameim1 text,sound1 blob,image1 blob,nameim2 text,sound2 blob,image2 blob,nameim3 text,sound3 blob,image3 blob,nameim4 text,sound4 blob,image4 blob) ')
    #cursor.execute('CREATE TABLE IF NOT EXISTS category(name text,c1name text,data1 blob,c2name text,data2 blob,c3name text,data3 blob,c4name text,data4 blob) ')
    conn.commit()
Database()
cursor.execute("INSERT INTO admins (username,password,first_name,last_name) VALUES(?,?,?,?)", ('shatha26','saaaa','shatha','arar'))
conn.commit()
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
i=IntVar()



def logout(frame):
    # Save in Data Base()
    svuser.set('')
    svpass.set('')
    frame.destroy()

def insert_user(user_name, id, first_name, last_name, password, gander, responsible_name, Email, phone,answer):
    cursor.execute("INSERT INTO users (first_name,last_name,id,responsible_name,Email,user_name,password,gander,phone,answer) VALUES(?,?,?,?,?,?,?,?,?,?)",(first_name, last_name, id, responsible_name, Email, user_name, password, gander, phone,answer))
    conn.commit()


def insert_board(name, id):
    cursor.execute("INSERT INTO boards (name,id) VALUES(?,?)", (name, id))
    conn.commit()



def delete_user(id):
    cursor.execute("DELETE FROM 'users' WHERE id=?", (id,))

def delete_user(username):
    cursor.execute("DELETE FROM 'users' WHERE user_name=?",(username,))
    conn.commit()


def delete_board(nameB):
    cursor.execute("DELETE FROM 'boards' WHERE name=?", (nameB,))
    conn.commit()


def update_massage(massage,username):
    cursor.execute("UPDATE 'users' SET massage=? WHERE user_name=?",(massage,username))
    conn.commit()



photonameList = []
photoDic = {}
imageNameInasert = {'im1name': None, 'im2name': None, 'im3name': None, 'im4name': None}
imageToInsert = {'im1': None, 'im2': None, 'im3': None, 'im4': None}


exp=0
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

        #settingframe.forget()
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
        Button(isShow, text='<-Back', bg="white", height="3", width="10").grid(row=20, column=0, pady=20, padx=10)
        Button(isShow, text='update', bg="white", height="1", width="5", command=upusername).grid(row=0, column=4,pady=20, padx=10)
        Button(isShow, text='update', bg="white", height="1", width="5", command=upfname).grid(row=3, column=4,pady=20, padx=10)
        Button(isShow, text='update', bg="white", height="1", width="5", command=uplname).grid(row=5, column=4,pady=20, padx=10)
        Button(isShow, text='update', bg="white", height="1", width="5", command=uppass).grid(row=7, column=4,pady=20, padx=10)
        Button(isShow, text='update', bg="white", height="1", width="5", command=uprname).grid(row=9, column=4,pady=20, padx=10)
        Button(isShow, text='update', bg="white", height="1", width="5", command=upmail).grid(row=11, column=4,pady=20, padx=10)
        Button(isShow, text='update', bg="white", height="1", width="5", command=upphone).grid(row=13, column=4,pady=20, padx=10)

        isShow.grid()
        isShow.mainloop()

    def create():
        global i
        if i.get() == 0:
            insert_user(txtfname.get(),txtlname.get(), txtid.get(),txtrname.get(),txtmail.get(),txtuser.get(),  txtpass.get(), txtgender.get(),  txtphone.get(), txtanswer.get())
        else:
            messagebox.showinfo('', "you want to agree the terms")
    def HelpFunc2():
        global exp
        frm = tk.Tk()
        fnt = ('tahoma', 30)
        fw = 900
        fh = 800
        x = (frm.winfo_screenwidth() - fw) / 2
        y = (frm.winfo_screenheight() - fh) / 2 - 50
        frm.geometry('%dx%d+%d+%d' % (fw, fh, x, y))

        frm.config(bg="white")
        Label(frm, text=exp, bg=bg, fg=fg, font=fnt).grid(row=2, column=2)

        frm.mainloop()

    def HelpFunc(texthelp):
        global exp
        frm = tk.Tk()

        exp = texthelp

        fnt = ('tahoma', 30)
        fw = 900
        fh = 800
        x = (frm.winfo_screenwidth() - fw) / 2
        y = (frm.winfo_screenheight() - fh) / 2 - 50
        frm.geometry('%dx%d+%d+%d' % (fw, fh, x, y))
        frm.config(bg="white")
        Label(frm, text='your explain is :', bg=bg, fg=fg, font=fnt).grid(row=3, column=0, pady=20)
        Label(frm, text=exp, bg=bg, fg=fg, font=fnt).grid(row=5, column=0, pady=20)

        frm.mainloop()

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
            ttt = 'the Termos:\n • Not allowed > upload disturbing images\n •Not allowed to extract audio > that has unsuitable words.\n• The system should be used correctly.\n• Allow managers to control my account.\n• Confirmation of saving my personal information in the system'
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
            Label(root, text=ttt, bg=bg, fg=fg, font=fnt).grid(row=0, column=0)
            c = Checkbutton(root, text="I accept the Terms of service ", variable=i, onvalue="checked").grid(
                row=11, column=0, pady=pad)
            Button(root, text='Create', command=create).grid(row=13, column=3, pady=pad)
            root.mainloop()

    def settingpage():
        global mainframe
        mainframe.forget()
        isShow = Frame(frm)

        Button(isShow, text="Language", bg="white", height="6", width="30", font=fnt).grid(row=4, column=1,
                                                                                                 padx=100, pady=20)
        Button(isShow, text="Help!", bg="white", height="6", width="30", font="50",command=HelpFunc2).grid(row=2, column=1,
                                                                                               padx=100, pady=20)
        #Button(isShow, text="Edit Profile", bg="white", height="6", width="30", font="50",command=updatepro).grid(row=0, column=1, padx=100, pady=20)
        Button(isShow, text="<- Back", bg="white", height="3", width="10", font="10", command=mainpage).grid(
            row=10, column=0, padx=5, pady=80)

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
        #txtprofile = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svprofile)
        txtanswer = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svanswer)

        btns = ttk.Style()
        btns.configure('TButton', font=fnt, pady=pad, padding=pad)
        #ttk.Button(frame, text='profile pic',
                   #command=lambda: saveprofile(filedialog.askopenfilename(filetypes=[("Image File", '.png')]))).grid(
            #row=10, column=0, pady=15)
        #ttk.Button(frame, text='Create new account', command=create).grid(row=11, column=1, pady=pad)
        # ttk.Button(frm, text='Exit Now', command=frm.destroy).grid(row=9, column=2, pady=pad)
        ttk.Button(frame, text='Back').grid(row=13, column=0, pady=8)
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
        a = open(name, 'rb')
        global pp
        pp = a.read()
        print(5)

    def convertToimage(name, imager):
        #print(imager)
        global imm
        if (name != None):
            b = open(name, 'wb')
            b.write(imager)
            #photonameList.append(name)
            imm= name
            #return ima
    def newbord():
        print(1)
        mainframe.forget()

        def convertTbinary(key, name):
            a = open(name, 'rb')
            #imageNameInasert[key + 'name'] = name
            #imageToInsert[key] = a.read()
            convertToimage('x'+str(key),a.read())



        def insertimag(num):
            def funcVoice(name):

                fs = 44100  # Sample rate
                seconds = 3  # Duration of recording
                print("seeey")
                myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
                sd.wait()  # Wait until recording is finished
                file = name
                write(file, fs, myrecording)  # Save as WAV file
                global vvo
                vvo=file
                #playsound(file)

            def saveimb():
                global isShow
                # print(imageToInsert['im1'])
                # isShow.forget()
                if num==1:
                    cursor.execute("UPDATE 'boards' SET nameim1=?,sound1=?,image1=? WHERE name=? ", (nameim.get(),vvo,imm,txtbord.get()))
                    conn.commit()
                elif num==2:
                    cursor.execute("UPDATE 'boards' SET nameim2=?,sound2=?,image2=? WHERE name=? ",(nameim.get(), vvo,imm, txtbord.get()))
                    conn.commit()
                elif num==3:
                    cursor.execute("UPDATE 'boards' SET nameim3=?,sound3=?,image3=? WHERE name=? ",(nameim.get(), vvo,imm, txtbord.get()))
                    conn.commit()
                elif num==4:
                    cursor.execute("UPDATE 'boards' SET nameim4=?,sound4=?,image4=? WHERE name=? ",(nameim.get(),vvo, imm, txtbord.get()))
                    conn.commit()
                creatimframe.forget()
                creatbord()

                # for n in imageToInsert:
                #convertToimage(imageNameInasert['im1' + 'name'], imageToInsert['im1'])
                #Fram(name, imageNameInasert['im1name'])
                #imageNameInasert['im1name'] = None
                # ChooseBordOrCat()
                # catDic[name][0].pack()
                # isShow=catDic[name][0]
            isShow.forget()
            global creatimframe
            creatimframe = Frame(frm)
            Label(creatimframe, text='name of image:', bg="white", fg=fg, font=" impact 25").grid(row=0, column=2)
            lbl = ttk.Label(creatimframe, text='name of the pic?')
            lbl.config(font=fnt)
            nameim = ttk.Entry(creatimframe)
            nameim.config(font=fnt)
            nameim.grid(row=1, column=2)

            Button(creatimframe, text="Add voice  ", bg="white", height="5", width="10", font="20",command=lambda: funcVoice("x"+str(num)+txtbord.get()+".wav")).grid(row=2,
                                                                                                         column=2,
                                                                                                         sticky=W,
                                                                                                         padx=90,
                                                                                                         pady=60)

            Button(creatimframe, text="Add pic ", bg="white", height="5", width="10", font="20",command=lambda: convertTbinary(num,filedialog.askopenfilename(filetypes=[("Image File", '.png')]))).grid(row=4, column=2, sticky=W, padx=90, pady=60)
            ok = tk.Button(creatimframe, text=" save ", bg="white", height="3", width="5", font="20",command=saveimb).grid(row=5, column=1, sticky=W, padx=20, pady=20)
            back = tk.Button(creatimframe, text=" <- Back ", bg="white", height="3", width="5", font="20").grid(row=5,column=0,sticky=W,padx=20,pady=20)
            creatimframe.pack()



        def setImage(im, namecat):
            global imi, isShow
            counter = 0
            isShow.forget()
            imi = im
            isShow = catDic[namecat][counter]
            isShow.pack()
        def save_B():

            cursor.execute("INSERT INTO boards (name) VALUES(?)", (txtbord.get(),))
            conn.commit()
            creatbord()
        def creatbord():
            global isShow
            isShow.forget()
            isShow = Frame(frm)

            #cursor.execute("INSERT INTO boards (name) VALUES(?)", (txtbord.get(),))
            #conn.commit()
            Button(isShow, text="+1", bg="white", height="10", width="20", font="100", command=lambda: insertimag(1)).grid(row=1, column=1, sticky=W, padx=60, pady=20)
            Button(isShow, text="+2", bg="white", height="10", width="20", font="100", command=lambda: insertimag(2)).grid(row=1, column=4, sticky=W, padx=90, pady=20)
            Button(isShow, text="+3", bg="white", height="10", width="20", font="100", command=lambda: insertimag(3)).grid(row=2, column=1, sticky=W, padx=60, pady=50)
            Button(isShow, text="+4", bg="white", height="10", width="20", font="100", command=lambda: insertimag(4)).grid(row=2, column=4, sticky=W, padx=90, pady=100)
            Button(isShow, text="Save", bg="white", height="3", width="10", font="100",command= lambda : mainpage()).grid(row=3, column=4,sticky=W, padx=170,pady=20)
            back = tk.Button(isShow, text=" <- Back ", bg="white", height="3", width="10", font="100",command=namebord).grid(row=3,column=0,sticky=W,padx=20,pady=20)


            isShow.pack()

        def namebord():
            global isShow,txtbord
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

            back = ttk.Button(isShow, text=" <- Back ")
            back.pack()
            isShow.pack()
            # mainframe.pack()

        namebord()

    def bord(z):

        print(z)
        def voice(num):

            for i in row:
                if i[0] == z:
                    if num == 1:
                        playsound(i[2])
                    elif num == 2:
                        playsound(i[5])
                    elif num == 3:
                        playsound(i[8])
                    elif num == 4:
                        playsound(i[11])

        global isShow
        isShow.forget()
        isShow = Frame(frm)
        cursor.execute("SELECT * FROM boards WHERE name=?", (z,))
        row = cursor.fetchall()
        #print(row)

        for i in row:
            t=open('name1.txt','w+')
            b1=Button(isShow, bg="white", height="10", width="20", font="100", image=convertToimage(t, i[3]),command=lambda: voice(1)).grid(row=1, column=1, sticky=W, padx=60, pady=20)
            b2=Button(isShow, bg="white", height="10", width="20", font="100", image=convertToimage('name2.txt', i[6]),command=lambda: voice(2)).grid(row=1, column=4, sticky=W, padx=90, pady=20)
            b3=Button(isShow, bg="white", height="10", width="20", font="100", image=convertToimage('name3.txt', i[9]),command=lambda: voice(3)).grid(row=2, column=1, sticky=W, padx=60, pady=50)
            b4=Button(isShow, bg="white", height="10", width="20", font="100", image=convertToimage('name4.txt', i[12]),command=lambda: voice(4)).grid(row=2, column=4, sticky=W, padx=90, pady=100)
            # Button(bordframe, text="Save", bg="white", height="3", width="10", font="100").grid(row=3, column=4,sticky=W, padx=170,pady=20)
            back = tk.Button(isShow, text=" <- Back ", bg="white", height="3", width="10", font="100",command=lambda: allboards()).grid(row=3,column=0,sticky=W,padx=20,pady=20)
            b1.image=convertToimage('name1.txt', i[3])
            b2.image=convertToimage('name2.txt', i[6])
            b3.image=convertToimage('name3.txt', i[9])
            b4.image=convertToimage('name4.txt', i[12])
        isShow.pack()
    def allboards():
        mainframe.forget()
        global row

        global isShow
        isShow = Frame(frm)

        cursor.execute("SELECT * FROM boards")
        row = cursor.fetchall()
        k=0


        for i in row:

            funcB((str(k)+i[0]),k)
            k+=1
            '''
            b=Button(isShow, text=y, bg="white", height="3", width="15", font="20")
            b.bind('<Button-1>', lambda event, frame=isShow, arg=y: bord(y))
            b.grid(row=k, column=1, padx=30, pady=20)
            k+=1
'''

        isShow.pack()
    def funcB(N,K):
        N=Button(isShow, text=row[K][0], bg="white", height="3", width="15", font="20")
        N.bind('<Button-1>', lambda event, frame=isShow, arg=row[K][0]: bord(row[K][0]))
        N.grid(row=K, column=1, padx=30, pady=20)


    def mainpage():

        global mainframe,isShow
        isShow.forget()
        mainframe = Frame(frm)
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

        #create = ttk.Button(mainframe, text='Create a new board!')
        Button(mainframe, text="Setting", bg="white", font=fnt, command=settingpage).grid(row=6, column=1, padx=300,
                                                                                          pady=10)
        Button(mainframe, text="Create a new board!", bg="white", font=fnt, command=newbord).grid(row=4, column=1,
                                                                                                  padx=300, pady=10)
        Button(mainframe, text="An existing boards", bg="white", font=fnt,command=allboards).grid(row=2, column=1, padx=200, pady=10)
        #Button(mainframe, text="Profile", bg="white", font=fnt).grid(row=0, column=1, padx=200, pady=20)
        Button(mainframe, text="<- Back", bg="white", font=fnt).grid(row=8, column=1, padx=30, pady=20)

        mainframe.pack()

    def forget():
        loginFrame.forget()

        def returnpass():
            forgetframe.forget()
            global newpassframe
            newpassframe = Frame(frm)

            def checkpass():

                if txtnew.get() == txt2.get():

                    newpassframe.forget()
                    account()
                else:
                    messagebox.showinfo('', 'The passwords not matched!')
                    txtnew.focus()
                    txt2.focus()

            Label(newpassframe, text='New Password', font='impact 25').pack()

            frm.geometry('600x400')
            lblnew = ttk.Label(newpassframe, text='Enter new password:')
            txtnew = ttk.Entry(newpassframe)
            lbl2 = ttk.Label(newpassframe, text='Enter the password one more time:')
            txt2 = ttk.Entry(newpassframe)
            change = ttk.Button(newpassframe, text='change password', command=checkpass)

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
                rows = cursor.fetchall()
                for i in rows:
                    if txtid.get() == i[3] and txtanswer.get() == i[12]:
                        returnpass()
                        print(txtanswer.get())

            Label(forgetframe, text='Account security', font='impact 25').pack()

            lbl1 = ttk.Label(forgetframe, text='your id:')
            lbl = ttk.Label(forgetframe, text='what your primry school?')

            txtanswer = ttk.Entry(forgetframe)
            txtanswer.config(font=fnt)
            txtid = ttk.Entry(forgetframe)
            txtid.config(font=fnt)
            lbl1.config(font=fnt)
            lbl.config(font=fnt)

            ok = ttk.Button(forgetframe, text='OK', command=forgetpass)

            lbl1.pack()
            txtid.pack()
            lbl.pack()
            txtanswer.pack()
            ok.pack()
            forgetframe.pack()

        question()

    def checkuser(name):

        cursor.execute("select * from 'users' where user_name=? ", (name,))
        if cursor.fetchone() is not None:
            return True
        return False
    def page2_admin():
        global r, m

        def funAzr():
            text = r.get()
            if checkuser(text) == True:
                # page3_admin()
                page4_admin()
                # page5_admin()

            if checkuser(text) == False:
                messagebox.showinfo('', 'Not found user!')

        page2 = tk.Tk()
        # frm.forget()
        fnt = ('tahoma', 16)
        bg = '#ffffff'
        bgtxt = '#00ff00'
        fg = '#000000'
        page2.config(bg=bg)
        Label(page2, text='Enter username you want to search:', bg=bg, fg=fg, font=fnt).grid(row=10, column=1, padx=30,
                                                                                             pady=120)
        r = Entry(page2, bg="white", fg=fg, font=fnt, textvariable=svuser)
        r.grid(row=10, column=2, padx=30, pady=120)

        Button(page2, text=" Search", bg="white", height="1", width="8", font="15", command=funAzr).grid(row=14,
                                                                                                         column=4,
                                                                                                         sticky=W,
                                                                                                         padx=30,
                                                                                                         pady=30)
        page2.mainloop()
    def page1_admin():
        global isShow
        isShow.forget()
        isShow = Frame(frm)

        Button(isShow, text="Search an User", bg="white", height="5", width="20", font="25", command=page2_admin).grid(
            row=2, column=1, sticky=W, padx=30, pady=50)
        Button(isShow, text="Add a new board", bg="white", height="5", width="20", font="25").grid(row=2, column=3,
                                                                                                   sticky=W, padx=30,
                                                                                                   pady=50)
        Button(isShow, text="Add a new Catigoria", bg="green", height="5", width="20", font="25").grid(row=3, column=1,
                                                                                                       sticky=W,
                                                                                                       padx=30, pady=20)
        Button(isShow, text="Update the page explain ", bg="white", height="5", width="20", font="25",
               command=explain).grid(row=3, column=2, sticky=W, padx=30, pady=20)
        # Button(page3, text="Birthday", bg="green", height="5", width="20", font="25").grid(row=3, column=3, sticky=W, padx=30,pady=20)
        # Button(frm, text="Delete an user ", bg="green", height="5", width="20", font="25").grid(row=4, column=2, sticky=W, padx=30, pady=20)
        Button(isShow, text="My design ", bg="green", height="5", width="20", font="25").grid(row=2, column=2, sticky=W,
                                                                                              padx=30, pady=50)
        back = tk.Button(isShow, text=" <- Back ", bg="white", height="3", width="10", font="100").grid(row=5, column=1,
                                                                                                        sticky=W,
                                                                                                        padx=20,
                                                                                                        pady=20)
        isShow.pack()

    def explain():
        explainpage = tk.Tk()

        fnt = ('tahoma', 30)
        fw = 900
        fh = 800
        x = (explainpage.winfo_screenwidth() - fw) / 2
        y = (explainpage.winfo_screenheight() - fh) / 2 - 50
        explainpage.geometry('%dx%d+%d+%d' % (fw, fh, x, y))

        explainpage.config(bg="white")
        Label(explainpage, text='enter your new explain', bg=bg, fg=fg, font=fnt).grid(row=0, column=0)
        m = Entry(explainpage, bg="white", fg=fg, font=fnt)
        m.grid(row=10, column=2, padx=30, pady=120)
        Button(explainpage, text="Ok", bg="green", height="5", width="20", font="25",
               command=lambda: HelpFunc(m.get())).grid(row=2, column=2, sticky=W,
                                                       padx=30, pady=50)

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
        Button(page4, text="Delete an user", bg="white", height="5", width="20", font="25",
               command=lambda: delete_user(r.get())).grid(row=3, column=1, sticky=W, padx=30, pady=20)
        Button(page4, text="Wish a Happy Birthday", bg="white", height="5", width="20", font="25",
               command=lambda: update_massage(text1, r.get())).grid(row=5, column=1, sticky=W, padx=30, pady=20)
        Button(page4, text="Send A massage ", bg="white", height="5", width="20", font="25", command=page5_admin).grid(
            row=7, column=1, sticky=W, padx=30, pady=20)

        page4.mainloop()

    def page5_admin():
        page5 = tk.Tk()
        # frm.forget()
        fnt = ('tahoma', 16)
        bg = '#ffffff'
        bgtxt = '#00ff00'
        fg = '#000000'
        page5.config(bg=bg)
        Label(page5, text='Enter your massage thats you want to send to user ', bg=bg, fg=fg, font=fnt).grid(row=10,
                                                                                                             column=1,
                                                                                                             padx=30,
                                                                                                             pady=120)
        m = Entry(page5, bg="white", fg=fg, font=fnt, textvariable=svmassage)
        m.grid(row=10, column=2, padx=30, pady=120)
        Button(page5, text="Send", bg="white", height="1", width="8", font="15",
               command=lambda: update_massage(m.get(), r.get())).grid(row=14, column=4, sticky=W, padx=30, pady=30)
        # messagebox.showinfo('', 'The massage send!')
    def login():


        global isShow
        isShow.forget()
        isShow = Frame(frm)

        def check():
            print(svuser.get(), svpass.get())
            cursor.execute("select * from 'users' where user_name=(?) and password=(?) ", (svuser.get(), svpass.get()))
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
        isShow.pack()

    def f():
        global isShow
        isShow=Frame(frm)
        Label(isShow, text="Choose Login Or Register", bg="blue", width="300")
        Label(isShow, text="").pack()
        Button(isShow, text="Login", height="2", width="30", command=login).pack()
        Label(isShow, text="").pack()
        Button(isShow, text="Register", height="2", width="30", command=sign_up).pack()
        Label(isShow, text="").pack()
        isShow.pack()
        isShow.mainloop()
    f()

'''
    global isShow
    isShow.forget()
    isShow=Frame(frm)
    cursor.execute("SELECT * FROM 'boards' WHERE name=?", ('last1',))
    row= cursor.fetchall()
    for i in row:
        playsound(i[2])
        Button(isShow, text="Wish a Happy Birthday", bg="white", height="5", width="20", font="25",
               command=lambda: update_massage(text1, r.get())).grid(row=5, column=1, sticky=W, padx=30, pady=20)
'''






#cursor.execute("DELETE FROM boards WHERE name='shaa'")
#conn.commit()
#w = Scale(frm, from_=0, to=42)
#w.pack()


isShow=Frame(frm)
'''
def login():
    global loginFrame
=======
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
    a=Label(loginFrame,text='',fg='red')
    a.grid(row=0,column=2, pady=20)
    Label(loginFrame,text="Enter user name:").grid(row=1,column=1)
    Entry(loginFrame,textvariable=svuser).grid(row=1,column=2)
    Label(loginFrame, text="Enter password:").grid(row=2, column=1)
    Entry(loginFrame, textvariable=svpass).grid(row=2,column=2)
    Button(loginFrame, text='login',height="2",width="30",command=lambda: check).grid(row=3, column=2, pady=20)
    loginFrame.pack()
'''

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
# =======
# >>>>>>> f6276ef1b32f148412718f5262ebf3cb265dccd0

# account()

# frm.mainloop()





#account()
#frm.mainloop()
'''
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
'''
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
    #svprofile = StringVar()
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



'''
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

'''
# <<<<<<< HEAD


#page6()




def main_page():
    idboard=StringVar()
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
    # frm.iconbitmap('icon.ico')
    frm.mainloop()

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
    global isShow
    isShow.forget()
    isShow=Frame(frm)

    Button(isShow, text="Search an User", bg="white", height="5", width="20", font="25",command=page2_admin).grid(row=2, column=1, sticky=W, padx=30,pady=50)
    Button(isShow, text="Add a new board", bg="white", height="5", width="20", font="25").grid(row=2, column=3, sticky=W, padx=30,pady=50)
    Button(isShow, text="Add a new Catigoria", bg="green", height="5", width="20", font="25").grid(row=3, column=1, sticky=W, padx=30,pady=20)
    Button(isShow, text="Update the page explain ", bg="white", height="5", width="20", font="25",command=explain).grid(row=3, column=2, sticky=W, padx=30,pady=20)
    #Button(page3, text="Birthday", bg="green", height="5", width="20", font="25").grid(row=3, column=3, sticky=W, padx=30,pady=20)
    #Button(frm, text="Delete an user ", bg="green", height="5", width="20", font="25").grid(row=4, column=2, sticky=W, padx=30, pady=20)
    Button(isShow, text="My design ", bg="green", height="5", width="20", font="25").grid(row=2, column=2, sticky=W, padx=30, pady=50)
    back = tk.Button(isShow, text=" <- Back ", bg="white", height="3", width="10", font="100").grid(row=5, column=1,sticky=W, padx=20,pady=20)
    isShow.pack()
def checkuser(name):

    cursor.execute("select * from 'users' where user_name=? ", (name,))
    if cursor.fetchone() is not None:
        return True
    return False


def update_massage(massage,username):
    cursor.execute("UPDATE 'users' SET massage=? WHERE user_name=?",(massage,username))
    conn.commit()


'''

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


    page5.mainloop()'''







account()

