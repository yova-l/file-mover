# Import module 
import tkinter as tk
  
LANGUAGE_OPTIONS = ["Español", "English"]

class OptionMenuPers(tk.OptionMenu):
    # clicked = tk.StringVar()
    # clicked.set(LANGUAGE_OPTIONS[0]) 

    def __init__(self, parent):
        self.clicked = tk.StringVar()
        self.clicked.set(LANGUAGE_OPTIONS[0]) 
        super().__init__(parent, self.clicked , *LANGUAGE_OPTIONS)

    def get_str_var(self):
        return self.clicked
    
def create_lang_selector(parent) -> OptionMenuPers:
    return OptionMenuPers(parent)
    
# def create_lang_selector(parent, tracer_func) -> tk.OptionMenu:

#     clicked = tk.StringVar(parent, name="language_val") 
#     clicked.set(LANGUAGE_OPTIONS[0]) 
#     clicked.trace_add("write", tracer_func)
    
#     # Create Dropdown menu 
#     drop = tk.OptionMenu(parent, clicked , *LANGUAGE_OPTIONS) 

    
#     return drop
    
