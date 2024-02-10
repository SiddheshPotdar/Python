from tkinter import *

window = Tk()

def click():
  input = text.get("1.0", END)
  print(input)

text = Text(window,
            font=("Ink Free", 12),
            bg="light yellow",
            fg="purple",
            height=12,
            width=25)
text.pack()

button = Button(window,
                text="Click",
                command=click)
button.pack()

window.mainloop()
