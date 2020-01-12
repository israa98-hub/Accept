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
im1=StringVar()
im2=StringVar()
im3=StringVar()
im4=StringVar()
imi=''

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
    cursor.execute('CREATE TABLE IF NOT EXISTS bord(name text,b1name text,b2name text,b3name text,b4name text) ')
    cursor.execute('CREATE TABLE IF NOT EXISTS category(name text,c1name text,data1 blob,c2name text,data2 blob,c3name text,data3 blob,c4name text,data4 blob) ')
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
    cursor.execute("UPDATE 'users' SET first_name=?,last_name=?,password=?,user_name=?,Email=?,responsible_name=?,phone=? WHERE id=id ",(name,last_name,password,user_name,email,responsible_name,phone))
    conn.commit()

photonameList = []
photoDic = {}
imageNameInasert={'im1name':None,'im2name':None,'im3name':None,'im4name':None}
imageToInsert={'im1':None,'im2':None,'im3':None,'im4':None}
def account():
    global a
    a=Frame(frm)

    
    def updatepro():
        def upusername():
                cursor.execute("UPDATE 'users' SET user_name=? WHERE id=? ",(svuser.get(),id))
                conn.commit()
                print(77)
        def upfname():
                cursor.execute("UPDATE 'users' SET first_name=? WHERE id=? ",(svfname.get(),id))
                conn.commit()
                print(88)
        def uplname():
                cursor.execute("UPDATE 'users' SET last_name=? WHERE id=? ",(svlname.get(),id))
                conn.commit()
        def uppass():
                cursor.execute("UPDATE 'users' SET password=? WHERE id=? ",(svpass.get(),id))
                conn.commit()
        def uprname():
                cursor.execute("UPDATE 'users' SET responsible_name=? WHERE id=? ",(svrname.get(),id))
                conn.commit()
        def upphone():
                cursor.execute("UPDATE 'users' SET phone=? WHERE id=? ",(svphone.get(),id))
                conn.commit()
        def upmail():
                cursor.execute("UPDATE 'users' SET Email=? WHERE id=? ",(svmail.get(),id))
                conn.commit()
        

        
        settingframe.forget()
        global updateframe
        updateframe=Frame(frm)
        Label(updateframe, text='user name:', bg=bg, fg=fg, font=fnt).grid(row=0, column=0,pady=20)
        Label(updateframe, text='The first name of the autistic :', bg=bg, fg=fg, font=fnt).grid(row=3, column=0,pady=20)
        Label(updateframe, text='The last name of the autistic :', bg=bg, fg=fg, font=fnt).grid(row=5, column=0,pady=20)
        Label(updateframe, text='The password :', bg=bg, fg=fg, font=fnt).grid(row=7, column=0,pady=20)
        Label(updateframe, text='The name of the responsible :', bg=bg, fg=fg, font=fnt).grid(row=9, column=0,pady=20)
        Label(updateframe, text='The E-mail of the responsible :', bg=bg, fg=fg, font=fnt).grid(row=11, column=0,pady=20)
        Label(updateframe, text='The number phone of the responsible :', bg=bg, fg=fg, font=fnt).grid(row=13, column=0,pady=20)
        # Label(frame, text='The profile of the Autistic :', bg=bg, fg=fg, font=fnt).grid(row=9, column=0)
        # Label(top, image=im).pack()
        Entry(updateframe, bg=bgtxt, fg=fg, font=fnt, textvariable=svuser).grid(row=0,column=2)
        Entry(updateframe, bg=bgtxt, fg=fg, font=fnt, textvariable=svfname).grid(row=3,column=2)
        Entry(updateframe, bg=bgtxt, fg=fg, font=fnt, textvariable=svlname).grid(row=5,column=2)
        Entry(updateframe, bg=bgtxt, fg=fg, font=fnt, textvariable=svpass).grid(row=7,column=2)
        Entry(updateframe, bg=bgtxt, fg=fg, font=fnt, textvariable=svrname).grid(row=9,column=2)
        Entry(updateframe, bg=bgtxt, fg=fg, font=fnt, textvariable=svmail).grid(row=11,column=2)
        Entry(updateframe, bg=bgtxt, fg=fg, font=fnt, textvariable=svphone).grid(row=13,column=2)
        #txtprofile = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svprofile).grid(row=15,column=2)
        Button(updateframe, text='<-Back',bg="white",height="3",width="10").grid(row=20, column=0, pady=20,padx=10)

        Button(updateframe, text='update',bg="white",height="1",width="5",command=upusername).grid(row=0, column=4, pady=20,padx=10)
        Button(updateframe, text='update',bg="white",height="1",width="5",command=upfname).grid(row=3, column=4, pady=20,padx=10)
        Button(updateframe, text='update',bg="white",height="1",width="5",command=uplname).grid(row=5, column=4, pady=20,padx=10)
        Button(updateframe, text='update',bg="white",height="1",width="5",command=uppass).grid(row=7, column=4, pady=20,padx=10)
        Button(updateframe, text='update',bg="white",height="1",width="5",command=uprname).grid(row=9, column=4, pady=20,padx=10)
        Button(updateframe, text='update',bg="white",height="1",width="5",command=upmail).grid(row=11, column=4, pady=20,padx=10)
        Button(updateframe, text='update',bg="white",height="1",width="5",command=upphone).grid(row=13, column=4, pady=20,padx=10)

        updateframe.grid()
        updateframe.mainloop()





    def settingpage():
        mainframe.forget()
        global settingframe
        settingframe=Frame(frm)

        Button(settingframe, text="Language", bg="white", height="6", width="30", font=fnt).grid(row=4, column=1, padx=100,pady=20)
        Button(settingframe, text="Help!", bg="white", height="6", width="30", font="50").grid(row=2, column=1, padx=100,pady=20)
        Button(settingframe, text="Edit Profile", bg="white", height="6", width="30", font="50",command=updatepro).grid(row=0, column=1,padx=100, pady=20)
        Button(settingframe, text="<- Back", bg="white", height="3", width="10", font="10",command=mainpage).grid(row=10, column=0, padx=5, pady=80)

        settingframe.pack()

    def sign_up():
        a.forget()
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
        ttk.Button(frame, text='profile pic',command=lambda: saveprofile(filedialog.askopenfilename(filetypes=[("Image File", '.png')]))).grid(row=10, column=0, pady=15)
        ttk.Button(frame, text='Create new account', command=create).grid(row=11, column=1, pady=pad)
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
        txtanswer.grid(row=9,column=1,pady=pad)

        frame.pack(pady=pad)
    def saveprofile(name):
             a = open(name, 'rb')
             global pp
             pp=a.read()
             print(5)

    def newbord():
        print(1)
        mainframe.forget()
        def convertTbinary(key,name):
             a = open(name, 'rb')
             imageNameInasert[key+'name']=name
             imageToInsert[key]= a.read()

        def convertToimage(name, imager):
             if (name != None):
                 b = open(name, 'wb')
                 b.write(imager)
                 photonameList.append(name)
                 photoDic[name]=PhotoImage(file=name)
        def insertimag():
            creatframe.forget()
            global creatimframe
            creatimframe = Frame(frm)
            Label(creatimframe, text='name of image:', bg="white", fg=fg, font=" impact 25").grid(row=0, column=2)
            lbl = ttk.Label(creatimframe, text='name of the pic?')
            lbl.config(font=fnt)
            x = ttk.Entry(creatimframe)
            x.config(font=fnt)
            x.grid(row=1, column=2)


            Button(creatimframe, text="Add voice  ", bg="white", height="5", width="10", font="20").grid(row=2, column=2, sticky=W, padx=90,pady=60)


            Button(creatimframe, text="Add pic ", bg="white", height="5", width="10", font="20",command=lambda: convertTbinary('im1',filedialog.askopenfilename(filetypes=[("Image File", '.png')]))).grid(row=4, column=2, sticky=W, padx=90,pady=60)

            ok = tk.Button(creatimframe, text=" ok ", bg="white", height="3", width="5", font="20",command=lambda: saveCat(txtbord.get())).grid(row=5, column=1, sticky=W, padx=20,pady=20)

            back = tk.Button(creatimframe, text=" <- Back ", bg="white", height="3", width="5", font="20").grid(row=5, column=0, sticky=W, padx=20,pady=20)
            creatimframe.pack()
        def saveCat(name):
           global isShow
           Database()
           #print(imageToInsert['im1'])
           
           # isShow.forget()
           cursor.execute("insert into category (name,c1name,data1)values (?,?,?)",(name, imageNameInasert['im1name'], imageToInsert['im1']))
           conn.commit()
           
           #for n in imageToInsert:
           convertToimage(imageNameInasert[im1+'name'], imageToInsert[im1])
           Fram(name, imageNameInasert['im1name'])
           imageNameInasert['im1name'] = None
               #ChooseBordOrCat()
              # catDic[name][0].pack()
              # isShow=catDic[name][0]

        def setImage(im,namecat):
            global imi,isShow
            counter=0
            isShow.forget()
            imi=im
            isShow=catDic[namecat][counter]
            isShow.pack()
        def creatbord():
            bordframe.forget()
            global creatframe
            creatframe = Frame(frm)
          
            Button(creatframe, text="+", bg="white", height="10", width="20", font="100",command=insertimag).grid(row=1, column=1,sticky=W, padx=60,pady=20)
            Button(creatframe, text="+", bg="white", height="10", width="20", font="100",command=insertimag).grid(row=1, column=4, sticky=W,padx=90, pady=20)
            Button(creatframe, text="+", bg="white", height="10", width="20", font="100",command=insertimag).grid(row=2, column=1, sticky=W,padx=60, pady=50)
            Button(creatframe, text="+", bg="white", height="10", width="20", font="100",command=insertimag).grid(row=2, column=4, sticky=W,padx=90, pady=100)
            Button(creatframe, text="Save", bg="white", height="3", width="10", font="100").grid(row=3, column=4, sticky=W,padx=170, pady=20)
            back=tk.Button(creatframe, text=" <- Back ", bg="white", height="3", width="10", font="100").grid(row=3, column=0, sticky=W,padx=20, pady=20)
            creatframe.pack()
        def namebord():
            print(2)
            print(3)
            global bordframe,txtbord
            bordframe = Frame(frm)
            B=ttk.Button(bordframe, text="Enter",command=creatbord)
            Label(bordframe, text='board name:', font=fnt).pack()
            print(4)
            txtbord=ttk.Entry(bordframe)
            txtbord.config(font=fnt)
            print(5)
            txtbord.pack()
            B.pack()
            
     
            back = ttk.Button(bordframe, text=" <- Back ")
            back.pack()
            bordframe.pack()
            #mainframe.pack()
        namebord()
        

    def mainpage():
        a.forget()
        global mainframe
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
        
        create=ttk.Button(mainframe,text='Create a new board!')
        Button(mainframe, text="Setting", bg="white", font=fnt,command=settingpage).grid(row=6,column=1,padx=300,pady=10)
        Button(mainframe, text="Create a new board!",bg="white", font=fnt,command= newbord).grid(row=4,column=1,padx=300,pady=10)
        Button(mainframe, text="An existing boards", bg="white", font=fnt).grid(row=2,column=1,padx=200,pady=10)
        Button(mainframe, text="Profile", bg="white" ,font=fnt).grid(row=0,column=1,padx=200,pady=20)
        Button(mainframe, text="<- Back", bg="white", font=fnt).grid(row=8,column=1,padx=30,pady=20)
        
        mainframe.pack()
    def forget():
        loginFrame.forget()
        
        
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
            print(svuser.get(),svpass.get())
            cursor.execute("select * from 'users' where user_name=(?) and password=(?) ",(svuser.get(),svpass.get()))
            print(svuser.get(),svpass.get())
            if cursor.fetchone() is None:
                 cursor.execute("select * from 'admins' where username=(?) and password=(?) ",(svuser.get(),svpass.get()))
                 if cursor.fetchone() is None:
                     messagebox.showinfo('', 'Invalid Username or password!')
                    
                 #else:
                     #صفحة المنهيل
            else:
                 
                 global id
                 cursor.execute("SELECT * FROM 'users' ")
                 rows=cursor.fetchall()
                 for i in rows:
                    if svuser.get()==i[6] and svpass.get()==i[7]:
                        id=i[3]                 
                 loginFrame.forget()
                 mainpage()
        Label(loginFrame,text="Enter user name:").grid(row=1,column=1)
        Entry(loginFrame,textvariable=svuser).grid(row=2,column=1)
        Label(loginFrame, text="Enter password:").grid(row=3, column=1)
        Entry(loginFrame, textvariable=svpass).grid(row=4,column=1)
        '''
        lblname=ttk.Label(loginFrame,text='Enter username:').grid(row=1,column=2,padx=10,pady=10)
        txtname=ttk.Entry(loginFrame).grid(row=2,column=2,padx=10,pady=10)
        lblpass=ttk.Label(loginFrame,text='Enter the password:').grid(row=3,column=2,padx=10,pady=10)
        txtpass=ttk.Entry(loginFrame).grid(row=4,column=2,padx=10,pady=10)

'''
        Button(loginFrame,text='login',bg="white",font=5,command=check).grid(row=5,column=1,padx=10,pady=10)
        Button(loginFrame, text="forget password",bg="white", font=1,command=forget).grid(row=5,column=2,padx=10,pady=10)
        loginFrame.pack()
        loginFrame.mainloop()
                

        


    def f():
        Label(a,text="Choose Login Or Register", bg="blue", width="300")
        Label(a,text="").pack()
        Button(a,text="Login",height="2",width="30",command=login).pack()
        Label(a,text="").pack()
        Button(a,text="Register",height="2",width="30",command=sign_up).pack()
        Label(a,text="").pack()
        a.pack()
    f()
    




'''
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
