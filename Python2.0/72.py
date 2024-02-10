from tkinter import *

def submit():
  #print(listbox.get(listbox.curselection()))
  foods = []
  for i in listbox.curselection():
    foods.insert(i, listbox.get(i))

  for i in foods:
    print(i)

def add():
  listbox.insert(listbox.size(), entrybox.get())
  listbox.config(height=listbox.size())

def delete():
  for i in listbox.curselection():
    listbox.delete(i)

  listbox.config(height=listbox.size())
  

window = Tk()

window.geometry("420x420")

listbox = Listbox(window,
                  bg="#f7ffde",
                  font="Constantia",
                  width=12,
                  selectmode=MULTIPLE)
listbox.config(height=listbox.size())
                
listbox.insert(1, "pizza")
listbox.insert(2, "pasta")
listbox.insert(3, "garlic bread")
listbox.insert(4, "soup")
listbox.insert(5, "salad")

listbox.pack()

submit_button = Button(window, 
                text="Submit",
                font=("Constantia", 12),
                command=submit)
submit_button.pack()

entrybox = Entry(window)
entrybox.pack()

add_button = Button(window,
                    text="Add",
                    font=("Constantia", 12),
                    command=add)
add_button.pack()

delete_button = Button(window, 
                       text="Delete",
                       font=("Constantia", 12),
                       command=delete)
delete_button.pack()

window.mainloop() 