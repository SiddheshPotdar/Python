from tkinter import *

def display():
  if(x.get()):
    print("You agreed!")
  else:
    print("You did not agree!")

window = Tk()

x = BooleanVar()

checkButton = Checkbutton(window, 
                          text="I agree to conditions.",
                          variable=x,
                          onvalue=True,
                          offvalue=False,
                          command=display)

checkButton.pack()                          

window.mainloop()