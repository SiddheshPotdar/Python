from tkinter import *

window = Tk()

window.geometry("420x420")

label = Label(window, text = "Hello world!",
              font=('Arial', 16, 'bold'), fg='green')
label.pack()

window.mainloop()