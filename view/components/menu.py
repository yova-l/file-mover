import tkinter as tk
from tkinter import messagebox
from ..constants import ALL_TEXT

ABOUT_WINDOW_TITLE = "About FileMover"

def about_message(lang_index):
    messagebox.showinfo(title=ABOUT_WINDOW_TITLE, message=ALL_TEXT["about_text"][lang_index])
    # el message box deberia tener el hipervinculo

def donate_web():
    # messagebox.showinfo(title="About FileMover", message=ABOUT_MESSAGE)
    pass # Launchea el link tree
"""
Bind the label to "<Button-1>" event. When it is raised the callback is executed resulting in a new page opening in your default browser.

from tkinter import *
import webbrowser

def callback(url):
    webbrowser.open_new(url)

root = Tk()
link1 = Label(root, text="Hyperlink", fg="blue", cursor="hand2")
link1.pack()
link1.bind("<Button-1>", lambda e: callback("http://www.example.com"))

link2 = Label(root, text="Hyperlink", fg="blue", cursor="hand2")
link2.pack()
link2.bind("<Button-1>", lambda e: callback("http://www.example.org"))

root.mainloop()
You can also open files by changing the callback to:

webbrowser.open_new(r"file://c:\test\test.csv")
"""

def create_menu(parent, lang_index):
    menu = tk.Menu(parent, tearoff=0)
    menu.add_command(label=ALL_TEXT["about_menu"], command=lambda: about_message(lang_index))
    menu.add_separator()
    menu.add_command(label=ALL_TEXT["donate_menu"][lang_index], command=donate_web)
    return menu