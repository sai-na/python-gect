from tkinter import *
from tkinter import ttk
root = Tk(className="nai")
my_frame=ttk.Frame(root,padding=10,width=70,height=250)
my_frame.grid()
my_frame.pack()
ttk.Label(my_frame,text="Hello World").grid(column=0,row=0)
for i in range(4):
    ttk.Button(my_frame,text="Quit",command=root.destroy).grid(column=i,row=i)
root.mainloop()