from tkinter import *

foods = ['pizza', 'burger', 'chips']


def display():
  if(x.get() == 0):
    print("You ordered pizza!")
  elif(x.get() == 1):
    print("You ordered burger!")
  else:
    print("You ordered chips!")

window = Tk()

window.geometry("420x420")

x = IntVar()

for i in range(0, len(foods)):
  radioButton = Radiobutton(window,
                            text=foods[i],
                            variable=x,
                            value= i,
                            indicatoron=0,
                            width=325,
                            command=display
                            )
  radioButton.pack(anchor=W)                            

window.mainloop()