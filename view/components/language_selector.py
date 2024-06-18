# Import module 
import tkinter as tk
  
LANGUAGE_OPTIONS = ["Español", "English"]

class OptionMenuPers(tk.OptionMenu):
    def __init__(self, parent, tracer_func):
        self.clicked = tk.StringVar()
        self.clicked.set(LANGUAGE_OPTIONS[0])
        self.clicked.trace_add("write", tracer_func) 
        super().__init__(parent, self.clicked , *LANGUAGE_OPTIONS)

    def get_str_var(self):
        return self.clicked
    
def create_lang_selector(parent, tracer_func) -> OptionMenuPers:
    return OptionMenuPers(parent, tracer_func)