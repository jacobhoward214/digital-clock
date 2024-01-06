from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# btn = ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# print(btn.configure().keys())
# print(set(btn.configure().keys()) - set(frm.configure().keys()))
# print(dir(btn))
# print(set(dir(btn)) - set(dir(frm)))
root.mainloop()
