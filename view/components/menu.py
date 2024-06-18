import tkinter as tk
from tkinter import messagebox
from ..constants import ALL_TEXT

import webbrowser

ABOUT_WINDOW_TITLE = "About FileMover"

def about_message(lang_index):
    wants_to_visit = messagebox.askyesno(title=ABOUT_WINDOW_TITLE, message=ALL_TEXT["about_text"][lang_index])
    
    if wants_to_visit:
        webbrowser.open_new(ALL_TEXT["linktree_link"])

def donate_web():
    webbrowser.open_new(ALL_TEXT["linktree_link"])

def help_message(lang_index):
    messagebox.showinfo(title="Help", message=ALL_TEXT["app_desc"][lang_index])

def create_menu(parent, lang_index):
    menu = tk.Menu(parent, tearoff=0)
    menu.add_command(label=ALL_TEXT["about_menu"], command=lambda: about_message(lang_index))
    menu.add_separator()
    menu.add_command(label=ALL_TEXT["donate_menu"][lang_index], command=donate_web)
    menu.add_separator()
    menu.add_command(label=ALL_TEXT["help_menu"][lang_index], command=lambda: help_message(lang_index))
    return menu