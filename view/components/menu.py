import tkinter as tk
from tkinter import messagebox

ABOUT_MESSAGE = """ 
Thanks for using FileMover, for any suggestion or to see the code you can visit the website. Feel free to reach me 
out trough any of my social media. Also it would be lovely if you can contribute with a donation so I can keep making
free and open source software on demand. Also leave your ideas so I can consider it as my next project.
"""

def about_message():
    messagebox.showinfo(title="About FileMover", message=ABOUT_MESSAGE)

def donate_web():
    messagebox.showinfo(title="About FileMover", message=ABOUT_MESSAGE)

def create_menu(parent):
    menu = tk.Menu(parent, tearoff=0)
    menu.add_command(label="About", command=about_message)
    menu.add_separator()
    menu.add_command(label="Donate", command=donate_web)
    return menu