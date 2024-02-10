from tkinter import *
from tkinter import filedialog

def openFile():
  path = filedialog.askopenfilename(initialdir="D:\\codes\\practice", 
  title="Choose file", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
  # print(path)
  file = open(path, 'r')
  print(file.read())
  file.close()

window = Tk()

button = Button(window,
                text="Open File",
                command=openFile)
button.pack()

window.mainloop()