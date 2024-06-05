# Import module 
import tkinter as tk
  
LANGUAGE_OPTIONS = ["English", "Español"]
DEFAULT = "English"

def create_lang_selector(parent) -> tk.OptionMenu:

    clicked = tk.StringVar(parent, name="language_val") 
    clicked.set(DEFAULT) 
    
    # Create Dropdown menu 
    drop = tk.OptionMenu(parent, clicked , *LANGUAGE_OPTIONS) 

    
    return drop
    
