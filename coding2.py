def page5():
    frm = tk.Tk()
    window = tk.Toplevel(frm)
    fnt = ('tahoma', 30)
    fw = 900
    fh = 800
    x = (frm.winfo_screenwidth() - fw) / 2
    y = (frm.winfo_screenheight() - fh) / 2 - 50
    frm.geometry('%dx%d+%d+%d' % (fw, fh, x, y))
    frm.title('Users')
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
    frm.title('Users')
    frm.config(bg="white")

    Button(frm, text="Language", bg="white", height="6", width="30", font="").grid(row=4, column=1, padx=100,pady=20)
    Button(frm, text="Help!", bg="white", height="6", width="30", font="50").grid(row=2, column=1, padx=100,pady=20)
    Button(frm, text="Edit Profile", bg="white", height="6", width="30", font="50").grid(row=0, column=1,padx=100, pady=20)
    Button(frm, text="<- Back", bg="white", height="3", width="10", font="10").grid(row=10, column=0, padx=5, pady=80)

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

page6()



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
    frm.config(bg=bg)
    Label(frm, text='name of image:', bg="white", fg=fg, font=" impact 25").grid(row=0, column=2)
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
    x = (frm.winfo_screenwidth() - fw) / 2
    y = (frm.winfo_screenheight() - fh) / 2 - 50
    frm.geometry('%dx%d+%d+%d' % (fw, fh, x, y))
    frm.title('main page for admin')
    frm.config(bg=bg)
    Button(page3, text="Search an User", bg="white", height="5", width="20", font="25",command=page2_admin).grid(row=2, column=1, sticky=W, padx=30,pady=50)
    Button(page3, text="Add a new board", bg="white", height="5", width="20", font="25").grid(row=2, column=3, sticky=W, padx=30,pady=50)
    Button(page3, text="Add a new Catigoria", bg="green", height="5", width="20", font="25").grid(row=3, column=1, sticky=W, padx=30,pady=20)
    Button(page3, text="Update the page explain ", bg="white", height="5", width="20", font="25").grid(row=3, column=2, sticky=W, padx=30,pady=20)
    Button(page3, text="Birthday", bg="green", height="5", width="20", font="25").grid(row=3, column=3, sticky=W, padx=30,pady=20)
    #Button(frm, text="Delete an user ", bg="green", height="5", width="20", font="25").grid(row=4, column=2, sticky=W, padx=30, pady=20)
    Button(page3, text="My design ", bg="green", height="5", width="20", font="25").grid(row=2, column=2, sticky=W, padx=30, pady=50)
    back = tk.Button(page3, text=" <- Back ", bg="white", height="3", width="10", font="100").grid(row=5, column=1,sticky=W, padx=20,pady=20)
    page3.mainloop()
