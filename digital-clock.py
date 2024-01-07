from tkinter import *
from tkinter import ttk
import datetime

root = Tk()
frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

lab = Label(root)
lab.pack()


def clock():
    time = datetime.datetime.now().strftime("Time: %H:%M:%S")
    lab.config(text=time)
    root.after(1000, clock)


clock()
# lbl = ttk.Label(frm, text=datetime.now()).grid(column=0, row=1)


# Get list of configuration options
# print(lbl.configure().keys())

# Get specific configuration options by comparing to a simpler widget
# print(set(lbl.configure().keys()) - set(frm.configure().keys()))

# Get all methods and you can identify spific methods for the widget class
# print(dir(lbl))
# print(set(dir(lbl)) - set(dir(frm)))
root.mainloop()
