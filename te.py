from tkinter import *
import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import os

root = Tk()
root.title("Untitled - Notepad")
root.geometry('800x500')
root.resizable(0, 0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

icon =PhotoImage(file="tim\pnote.png")
root.iconphoto(False,icon)

def open_file():
   file = fd.askopenfilename(defaultextension='.txt', filetypes=[('All Files', '*.*'), ("Text File", "*.txt*")])
   if file != '':
       root.title(f"{os.path.basename(file)}")
       text_area.delete(1.0, END)
       with open(file, "r") as file_:
           text_area.insert(1.0, file_.read())
           file_.close()
   else:
       file = None
def open_new_file():
   root.title("Notepad")
   text_area.delete(1.0, END)
def save_file():
    
    filepath = fd.asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = text_area.get(1.0, tk.END)
        output_file.write(text)
    root.title(f"Text Editor Application - {filepath}")

def exit_application():
   root.destroy()

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=False, activebackground='DodgerBlue')
file_menu.add_command(label="New", command=open_new_file)
file_menu.add_command(label="Open File", command=open_file)
file_menu.add_command(label="Save As", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Close File", command=exit_application)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

text_area = Text(root, font=("Times New Roman", 12))
text_area.grid(sticky=NSEW)
scroller = Scrollbar(text_area, orient=VERTICAL)
scroller.pack(side=RIGHT, fill=Y)
scroller.config(command=text_area.yview)
text_area.config(yscrollcommand=scroller.set)

root.update()
root.mainloop()