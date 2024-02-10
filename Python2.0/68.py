from tkinter import *

def submit():
  username = entry.get()
  print(f"Hello {username}!")
  entry.delete(0, END)

def delete():
  entry.delete(0, END )

window = Tk()

entry = Entry(window, font=("Arial", 50),
              fg="white",
              bg="black"
              , show='*')

entry.pack(side=LEFT)

submit_button = Button(window, text="Submit", padx=10, pady=10, font=('Arial', 20, 'bold'), background='green', command=submit)

submit_button.pack(side=RIGHT)


delete_button = Button(text="Delete", padx=10, pady=10, font=('Arial', 20, 'bold'), background='red', command=delete)

delete_button.pack(side=RIGHT)

window.mainloop()