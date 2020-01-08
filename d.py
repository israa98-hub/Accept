from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import filedialog
import os

top = Tk()
top.geometry('900x900')
catDic = {}
photonameList = []
lista = []
photoDic = {}
bordDic={}
isShow = None  # the frame
image_name=''
bords_name=''
'''for i in photonameList:
    photoDic[i]=PhotoImage(file=i)'''
im1=StringVar()
im2=StringVar()
im3=StringVar()
im4=StringVar()
imi=''
ica=StringVar()
image_names={'im1':im1,'im2':im2,'im3':im3,'im4':im4}
bo1=StringVar()
bords_names={'ob1':bo1}
def database():
    global conn,curser
    conn = sqlite3.connect('admns.db')
    conn.row_factory = sqlite3.Row
    curser = conn.cursor()

    curser.execute(
        'CREATE TABLE IF NOT EXISTS  bord (name text,b1name text,data1 blob,b2name text,data2 blob,b3name text,data3 blob,b4name text,data4 blob) ')
    curser.execute(
        'CREATE TABLE IF NOT EXISTS  bord1 (name text,b1name text,b2name text,b3name text,b4name text) ')



imageNameInasert={'im1name':None,'im2name':None,'im3name':None,'im4name':None}
imageToInsert={'im1':None,'im2':None,'im3':None,'im4':None}

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


##after a chose image, back to creat bord
def saveImageName(name):
    global image_names
    image_names[imi].set(name)
    isShow.forget()
    bord()
'''**chose image'''
def setImage(im):
    global imi,isShow
    isShow.forget()
    imi=im
    isShow=catDic['food'][counter]
    isShow.pack()
def choosFrame():
    global isShow
    isShow.forget()
    a = Frame(top, height=20, width=20)
    a.grid(row=1, column=0)
    Entry(a, textvariable=bo1).pack()
    frame=Frame(top)
    a = Button(frame,text="add bord", height=20, width=20, command=lambda: bord())
    f = Frame(frame, height=20, width=20).pack()
    a = Button(frame, text="show  bord", height=20, width=10, command=lambda: bord())
    #a = Button(frame, text="add cat", height=20, width=20, command=lambda: )
    #a = Button(frame, text="show cat", height=20, width=20,command=lambda : Fram())

    isShow=frame
    isShow.pack()
def savebord(name):
    database()
    isShow.forget()
    curser.execute('insert into bord1 (name,b1name,b2name,b3name,b4name) VALUES (?,?,?,?,?)',(name,im1.get(),im2.get(),im3.get(),im4.get()))
    conn.commit()
    F=Frame(top)
    Label(F,text=name+ 'bord').grid(row=0,columnspan=3)
    Button(F,image=photoDic[im1.get()]).grid(row=1, column=0)
    Button(F, image=photoDic[im2.get()]).grid(row=1, column=2)
    Button(F,image=photoDic[im3.get()]).grid(row=2, column=0)
    Button(F, image=photoDic[im4.get()]).grid(row=2, column=2)
    bordDic[name]=F
    bordDic[name].pack()
    im1.set('')
    im2.set('')
    im3.set('')
    im4.set('')

def bord():
    global isShow
    frm = Frame(top)
    x = Frame(frm, height=20, width=20)
    x.grid(row=0, column=0)
    Label(x,text='Enter name of bord:').pack()
    newbord=Entry(x,textvariable=bo1).pack()
    a = Frame(frm, height=20, width=20)
    a.grid(row=1, column=0)
    Entry(a,textvariable=im1).pack()
    Button(a,text='get image from cat',width="25",command=lambda:setImage('im1')).pack()
    b = Frame(frm, height=20, width=20)
    b.grid(row=1, column=1)
    Entry(b,textvariable=im2).pack()
    Button(b,text='get image from cat',width="25",command=lambda:setImage('im2')).pack()
    c = Frame(frm, height=20, width=20)
    c.grid(row=2, column=0)
    Entry(c,textvariable=im3,).pack()
    Button(c,text='get image from cat',width="25",command=lambda:setImage('im3')).pack()
    d = Frame(frm, height=20, width=20)
    d.grid(row=2, column=1)
    Entry(d,textvariable=im4).pack()
    Button(d,text='get image from cat',width="25",command=lambda:setImage('im4')).pack()
    Label(frm).grid(row=3,columnspan=3)
    Label(frm).grid(row=4, columnspan=3)
    Button(frm,text='save bord',width="30",command=lambda: savebord(bo1.get())).grid(row=4,columnspan=3)
    isShow = frm
    frm.pack()


def Fram(name, image1=None, image2=None, image3=None, image4=None):
    frm = Frame(top)
    Label(frm, text=name).grid(row=0, columnspan=2, pady=20)
    if image1:
        b = Button(frm,text='image1',image=photoDic[image1],command=lambda: saveImageName(b['text']))
        b.grid(row=1, column=0)

    if image2:
        c = Button(frm, image=photoDic[image2],text="image2", command=lambda: saveImageName(c['text']))
        c.grid(row=1, column=1)
    if image3:
        d = Button(frm, image=photoDic[image3],text="image3", command=lambda: saveImageName(d['text']))
        d.grid(row=2, column=0)
    if image4:
        e = Button(frm, image=photoDic[image4],text="image4", command=lambda: saveImageName(e['text']))
        e.grid(row=2, column=1)
    Button(frm,text='next',command=lambda :next(name)).grid(row=4,columnspan=3)
    if name in tuple(catDic):
        catDic[name].append(frm)
        #### and insert to DB
    else:
        catDic[name] = [frm]

def saveCat(name):
    database()

    curser.execute(
        "insert into bord (name,b1name,data1,b2name,data2,b3name,data3,b4name,data4)values (?,?,?,?,?,?,?,?,?)",
        (name, imageNameInasert['im1name'], imageToInsert['im1'], imageNameInasert['im2name'], imageToInsert['im2'], imageNameInasert['im3name'], imageToInsert['im3'], imageNameInasert['im4name'],imageToInsert['im4']))
    conn.commit()
    Fram(name, imageNameInasert['im1name'], imageNameInasert['im2name'], imageNameInasert['im3name'], imageNameInasert['im4name'])
    imageNameInasert['im1name'],imageNameInasert['im2name'],imageNameInasert['im3name'],imageNameInasert['im4name']=None,None,None,None
    #for n in imageToInsert:
        #convertToimage(imageNameInasert[n+'name']),imageToInsert[n]
    catDic[name][0].pack()

def category():
    global isShow

    frm = Frame(top)

    x = Frame(frm, height=20, width=20)
    x.pack()

    c1= Frame(frm, height=20, width=20)
    c1.pack()

    Entry(x,textvariable=ica).pack()
    Button(x,text='Enter a name category:', width="25").pack()

    b1= Button(c1, text='Enter a name category:', width="25", command=lambda: convertTbinary('im1',filedialog.askopenfilename(filetypes=[("Image File", '.png')])))
    b1.grid(row=0,column=0)
    b2= Button(c1, text='Enter a name category:', width="25", command=lambda: convertTbinary('im2',filedialog.askopenfilename(filetypes=[("Image File", '.png')])))
    b2.grid(row=0,column=1)
    b3= Button(c1, text='Enter a name category:', width="25", command=lambda: convertTbinary('im3',filedialog.askopenfilename(filetypes=[("Image File", '.png')])))
    b3.grid(row=1,column=1)
    b4= Button(c1, text='Enter a name category:', width="25", command=lambda: convertTbinary('im4',filedialog.askopenfilename(filetypes=[("Image File", '.png')])))
    b4.grid(row=1,column=0)
    savecat= Button(frm, text='save', width="30", command=lambda:saveCat(ica.get()))
    savecat.pack()
    frm.pack()
    isShow=frm

database()


def ChooseBordOrCat():
    global isShow
    frm = Frame(top)
    if isShow is not None:
        isShow.forget()
    h = Frame(frm, height="20", width="20")
    h.pack()
    Label(h, text="Choose Bord or Category:").pack()
    bu1 = Button(h, text="BORD", width="25", command=lambda: bord())
    bu1.pack()
    bu2 = Button(h, text="Category", width="25", command=lambda: category())
    bu2.pack()
    frm.pack()
    isShow = frm
database()
'''im1name, imi1 = convertTbinary('m.png')
im2name, imi2 = convertTbinary('mm.png')
im3name, imi3 = convertTbinary('banana.png')
im4name, imi4 = convertTbinary('ques.png')
curser.execute("insert into bord (name,b1name,data1,b2name,data2,b3name,data3,b4name,data4)values (?,?,?,?,?,?,?,?,?)",
               ('food', im1name, imi1, im2name, imi2, im3name, imi3, im4name, imi4))'''
conn.commit()
c = curser.execute('select * from bord ')
for i in c:
    convertToimage(i['b1name'], i['data1'])
    convertToimage(i['b2name'], i['data2'])
    convertToimage(i['b3name'], i['data3'])
    convertToimage(i['b4name'], i['data4'])
    photonameList.append(i['b1name'])
    photonameList.append(i['b2name'])
    photonameList.append(i['b3name'])
    photonameList.append(i['b4name'])
    lista.append([i['name'], i['b1name'], i['b2name'], i['b3name'], i['b4name']])
''' base_folder = os.path.dirname(__file__)
     image_path = os.path.join(base_folder, n)
    photo = PhotoImage(file=image_path)'''
for c in lista:
    Fram(c[0], c[1], c[2], c[3], c[4])
counter = 0
#bord()
#category()
ChooseBordOrCat()



def next(catname):
    global counter, isShow
    isShow.forget()
    if counter == len(catDic[catname]):
        counter = len(catDic['food']) - 1
    isShow = catDic[catname][counter]
    counter += 1
    isShow.pack()

curser.close()
conn.close()
top.mainloop()
