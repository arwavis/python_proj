from tkinter import *
import tkinter as tk
from bookstorebackend import Database

# Object for the class Database

database = Database()


def get_selected_row(event):
    try:
        global selected_tuple
        index = listbox.curselection()[0]
        selected_tuple = listbox.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except:
        pass


def view_command():
    listbox.delete(0, END)
    for row in database.view():
        listbox.insert(END, row)


def search_command():
    listbox.delete(0, END)
    for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        listbox.insert(END, row)


def add_command():
    database.insert(
        title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    listbox.delete(0, END)
    listbox.insert(END, (title_text.get(), author_text.get(),
                   year_text.get(), isbn_text.get()))


def delete_command():
    database.delete(selected_tuple[0])


def update_command():
    database.update(
        selected_tuple[0], title_text.get(), author_text.get(),
        year_text.get(), isbn_text.get())


window = Tk()
window.title("BookStore")

"""
Label Fields
"""

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)
l2 = Label(window, text="Author")
l2.grid(row=0, column=2)
l3 = Label(window, text="Year")
l3.grid(row=1, column=0)
l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

"""
Entry Fields
"""


title_text = StringVar()
author_text = StringVar()
year_text = StringVar()
isbn_text = StringVar()

e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

"""
List Box
"""
listbox = Listbox(window, height=6, width=35)
listbox.grid(row=2, column=0, rowspan=6, columnspan=2)


"""
Scroll Bar
"""

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

"""
This helps configure the listbox and scrollbar so when you scroll the code know it needs o scroll vertically in the listbox.
"""

listbox.configure(yscrollcommand=sb1.set)
sb1.configure(command=listbox.yview)

listbox.bind('<<ListboxSelect>>', get_selected_row)

"""
Button Fields
Refer https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/grid.html to learn about usage of sticky. 
This helps stretch the button window.
"""


b1 = Button(window, text="View All", command=view_command)
b1.grid(row=2, column=3, sticky=tk.W+tk.E)
b2 = Button(window, text="Search Entry", command=search_command)
b2.grid(row=3, column=3, sticky=tk.W+tk.E)
b3 = Button(window, text="Add Entry", command=add_command)
b3.grid(row=4, column=3, sticky=tk.W+tk.E)
b4 = Button(window, text="Update selected", command=update_command)
b4.grid(row=5, column=3, sticky=tk.W+tk.E)
b5 = Button(window, text="Delete selected", command=delete_command)
b5.grid(row=6, column=3, sticky=tk.W+tk.E)
b6 = Button(window, text="Close", command=window.destroy)
b6.grid(row=7, column=3, sticky=tk.W+tk.E)


window.mainloop()
