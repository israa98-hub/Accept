from tkinter import *
from tkinter import filedialog
import sqlite3
top=Tk()
top.geometry('771x870')
image=filedialog.askopenfilename(filetypes=[("Image File",'.png')])
print(image.split('/')[-1::][0])
conn = sqlite3.connect("Accept.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS pic (name TEXT)")
cursor.execute("INSERT INTO pic (name)VALUES (?)",(image.split('/')[-1::][0],))
conn.commit()
im=PhotoImage(file=image)
Label(top,image=im).pack()
top.mainloop
#input("enter")
