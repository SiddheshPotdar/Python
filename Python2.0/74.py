from tkinter import *
from tkinter import colorchooser

def click():
  color = colorchooser.askcolor()
  colorHex = color[1]
  print(color)
  window.config(bg = colorHex)


window = Tk()

window.geometry("420x420")

button = Button(window, text="Click me", command=click)
button.pack() 

window.mainloop()