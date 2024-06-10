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

def create_menu(parent, lang_index):
    menu = tk.Menu(parent, tearoff=0)
    menu.add_command(label=ALL_TEXT["about_menu"], command=lambda: about_message(lang_index))
    menu.add_separator()
    menu.add_command(label=ALL_TEXT["donate_menu"], command=lambda: donate_web(lang_index))
    return menu