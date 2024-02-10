from tkinter import *

def submit():
  print(f"The temprature is {scale.get()} degrees.")

window = Tk()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient= VERTICAL,
              showvalue=0,
              tickinterval=10)
scale.pack()

button = Button(window,
                text="Submit",
                command=submit)
button.pack()              

window.mainloop()