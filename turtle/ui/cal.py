import tkinter as tk
 
def add():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    result = num1 + num2
    result_label.config(text=result)
 
# create the main window
root = tk.Tk()
root.title("Add Two Numbers")