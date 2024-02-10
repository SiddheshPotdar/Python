from tkinter import *
from tkinter import messagebox

def click():
#  messagebox.showerror(title="Error!", message="You are getting error!")
    messagebox.showwarning(title="Warning!", message="Please wear your seat belt")

window = Tk()

button = Button(window, text="Click me", command=click)
button.pack()

window.mainloop() 