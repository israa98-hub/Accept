from tkinter import filedialog
from tkinter import *
a=Tk()
def mfileopen():
    file1=filedialog.askopenfile()
    label=Label(text=file1).pack()

button=Button(text="Update your explanation",width=30,command=mfileopen)
button.pack()



a.mainloop()
