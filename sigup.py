from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
import mysql.connector
import os
frm = tk.Tk()
fnt = ('tahoma', 16)
bg = '#ffffff'
bgtxt = '#00ff00'
fg = '#000000'
fw = 900
fh = 800
x = (frm.winfo_screenwidth() - fw) / 2
y = (frm.winfo_screenheight() - fh) / 2 - 50
pad = 10

frm.geometry('%dx%d+%d+%d' % (fw, fh, x, y) )
frm.title('Users')
frm.config(bg=bg)

Label(frm, text='User Data', bg='navy', fg='lightblue', font=fnt).pack(pady=pad)
frame = Frame(frm, bg=bg)
frame.pack(pady=pad)

Label(frame, text='user name:', bg=bg, fg=fg, font=fnt).grid(row=0, column=0)
Label(frame, text='Autistic ID number:', bg=bg, fg=fg, font=fnt).grid(row=1, column=0)
Label(frame, text='The first name of the autistic :', bg=bg, fg=fg, font=fnt).grid(row=2, column=0)
Label(frame, text='The last name of the autistic :', bg=bg, fg=fg, font=fnt).grid(row=3, column=0)
Label(frame, text='The password :', bg=bg, fg=fg, font=fnt).grid(row=4, column=0)
Label(frame, text='The gender of the autistic: ', bg=bg, fg=fg, font=fnt).grid(row=5, column=0)
Label(frame, text='The name of the responsible :', bg=bg, fg=fg, font=fnt).grid(row=6, column=0)
Label(frame, text='The E-mail of the responsible :', bg=bg, fg=fg, font=fnt).grid(row=7, column=0)
Label(frame, text='The number phone of the responsible :', bg=bg, fg=fg, font=fnt).grid(row=8, column=0)

svuser = StringVar()
svId = StringVar()
svfname = StringVar()
svlname = StringVar()
svpass = StringVar()
svgender = StringVar()
svrname = StringVar()
svmail = StringVar()
svphone = StringVar()

txtuser = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svuser)
txtid = Entry(frame,bg=bgtxt, fg=fg, font=fnt, textvariable=svId)
txtfname = Entry(frame,bg=bgtxt, fg=fg, font=fnt, textvariable=svfname)
txtlname = Entry(frame,bg=bgtxt, fg=fg, font=fnt, textvariable=svlname)
txtpass = Entry(frame, bg=bgtxt, fg=fg, font=fnt, textvariable=svpass)
txtgender = ttk.Combobox(frame,values=('Male','Female'),state='readonly')
#txtdate = datetime.date
txtrname = Entry(frame,bg=bgtxt, fg=fg, font=fnt, textvariable=svrname)
txtmail = Entry(frame,bg=bgtxt, fg=fg, font=fnt, textvariable=svmail)
txtphone = Entry(frame,bg=bgtxt, fg=fg, font=fnt, textvariable=svphone)

txtuser.grid(row=0, column=1, pady=pad)
txtid.grid(row=1, column=1, pady=pad)
txtfname.grid(row=2,column=1,pady=pad)
txtlname.grid(row=3,column=1, pady=pad)
txtpass.grid(row=4, column=1, pady=pad)
txtgender.grid(row=5,column=1,pady=pad)
txtrname.grid(row=6, column=1, pady=pad)
txtmail.grid(row=7, column=1, pady=pad)
txtphone.grid(row=8, column=1, pady=pad)

def create():

    '''if svId.get().strip()=='':
        messagebox.showinfo('', 'The number of id is Empty!')
        txtid.focus()'''
    if svId.get().strip()=='':
        messagebox.showinfo('', 'The number of id is Empty!')
        txtid.focus()
    elif svfname.get().strip()=='':
        messagebox.showinfo('', 'The first name of the autistic is Empty!')
        txtfname.focus()
    elif svlname.get().strip()=='':
        messagebox.showinfo('', 'The last name of the autistic is Empty!')
        txtlname.focus()
    elif svgender=='':
        messagebox.showinfo('', 'the gender is Empty!')
        txtgender.focus()
    elif svrname.get().strip()=='':
        messagebox.showinfo('', 'The name of the responsible is Empty!')
        txtrname.focus()
    elif svmail.get().strip()=='':
        messagebox.showinfo('', 'The E-mail of the responsible is Empty!')
        txtmail.focus()
    elif svphone.get().strip()=='':
        messagebox.showinfo('', 'The number phone of the responsible is Empty!')
        txtphone.focus()
    else:
          try:
                conn = mysql.connector.connect(
                    host='localhost',
                    user='userpython',
                    passwd='123456',
                    database='accept user'
                )
                cum = conn.cursor()
                cum.execute("insert into emp values ('%s', %d ,'%s', '%s', %s, %s, '%s', '%s',%d)"
                            % (txt.get(),txtid.get(),txtfname.get(),txtlname.get(),txtpass.get(),txtgender.get(),txtrname.get(),
                            txtmail.get(),txtphone.get()))
                conn.commit()

          except mysql.connector.Error as e:
                    print(e)
        svId.set('')
        svfname.set('')
        svlname.set('')
        svrname.set('')
        svmail.set('')
        svphone.set('')
        messagebox.showinfo('', 'user file is created...')'''

        def signup(request):
            if request.method == 'POST':
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    username = form.cleaned_data.get('username')
                    raw_password = form.cleaned_data.get('password1')
                    user = authenticate(username=username, password=raw_password)
                    login(request, user)
                    return redirect('home')

        def log_in():
            username = input("Enter a username")
            ID = input("Enter an Autistic ID number: ")
            Fristname = input("Enter a first name of the autistic :")
            lastname = input("Enter a last name of the autistic :")
            password = input("Enter your password: ")
            gender = input("Enter a gender of the autistic: ")
            birthday = input(datetime.date)
            nameofresponsible = input("Enter a name of the responsible :")
            email = input("Enter the email: ")
            phone = input("Enter the number phone: ")


            messagebox.showinfo('', 'user file is created...')

            #print("Successful login")

btns = ttk.Style()
btns.configure('TButton', font=fnt, pady=pad, padding=pad)
ttk.Button(frm, text='Create user file Now', command=create).pack(pady=pad)
ttk.Button(frm, text='Exit Now', command=frm.destroy).pack(pady=pad)

frm.mainloop()

input('press enter to exit...')







'''
def log_in():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    #check()


'''

'''def check():
    if username == open("username").read(): and passsword == open("password").read():
        print("Successful login")
    else:
        print('Incorrect')'''