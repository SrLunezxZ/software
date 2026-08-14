import tkinter as tk
from tkinter import messagebox
#=============================
# Creating the window object
#=============================
w=tk.Tk()
w.title("Creating data From GUI controls")
w.geometry("300x250")
w.resizable(False, False)

#=============================
# Window title object
#=============================
lbl_title=tk.Label(
    w,
    text="Getting data from UI controls",
)
lbl_title.grid(row=0, column=0, padx=10, pady=2, sticky="w")

#=============================
# function get data
#=============================
def showData():
    name=txt_name.get()
    age=txt_age.get()
    messagebox.showinfo("Warning","Data: "+name+" "+age)

#=======================================
# Name widget and properties
#=======================================
lbl_name=tk.Label(
    w,
    text="Type your name: ",
    anchor="w"
).grid(row=1, column=0, padx=10, pady=5, sticky="w")

txt_name=tk.Entry(w, width=15)
txt_name.grid(row=1, column=1, padx=10, pady=5, sticky="w")

#========================================
# Age widget and properies
#========================================
lbl_age=tk.Label(
    w,
    text="Type your age: ",
    anchor="w"
).grid(row=2, column=0, padx=10, pady=5, sticky="w")

txt_age=tk.Entry(w, width=15)
txt_age.grid(row=2, column=1, padx=10, pady=5, sticky="w")

#========================================
# buttons and propieties
#========================================

btn=GetData=tk.Button(
    w,
    text="show data",
    width=15,
    command=showData
).grid(row=3, column=0, padx=10, pady=10, sticky="w")

btn_Close=tk.Button(
    w,
    text="close windows",
    command=w.destroy
).grid(row=3, column=1, padx=10, pady=5, sticky="w")

w.mainloop()