from tkinter import *

def click():
  print("You clicked on the button!")

window = Tk()

window.geometry("420x420")

button = Button(window, text="Click me", command=click, 
            background='red',
            padx=10,
            pady=10,
            )
button.place(x=210, y=20)

window.mainloop()