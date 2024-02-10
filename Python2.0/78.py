from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(defaultextension='.txt')
    filetext = str(textarea.get(1.0, END))
    file.write(filetext)
    file.close()

window = Tk()

textarea = Text(window)
textarea.pack()

button = Button(window, text='Save', command=saveFile)
button.pack()

window.mainloop()
