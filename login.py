import tkinter
from tkinter import ttk
import mysql.connector
log = tkinter.Tk()
log.title('login')
lblname = ttk.Label(log, text='your username')
txtname = ttk.Entry(log)
lblname.pack()
txtname.pack()

lblpass = ttk.Label(log, text='your password')
txtpass = ttk.Entry(log)
lblpass.pack()
txtpass.pack()

def log1():
    print('safaa')
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='userpython',
            passwd='123456',
            database='accept user'
        )
        cum = conn.cursor()
        sql = "SELECT (user name) from emp"
        cum.execute(sql)
        for i in cum:
            if i == txtname.get():
                if cum.execute("SELECT (password) FROM emp WHERE (user name) '%s'" % (i)):
                    print("log in")


        conn.commit()

    except mysql.connector.Error as e:
        print(e)


btn = ttk.Button(log, text='login', command=log1)
btn.pack()

log.mainloop()

