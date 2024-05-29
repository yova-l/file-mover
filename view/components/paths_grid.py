import tkinter as tk
from tkinter import filedialog as fd

FONT_LABEL = "Agave"
FONT_SIZE_LABEL = 12

FONT_BUTTONS = "Agave, Bold"
BUTTONS_TEXT = "Choose folder..."
BUTTONS_FONT_SIZE = 9

def open_dialog_path(entry): 
        # Specify the file types 
        # ('text files', '*.txt')
        #filetypes = (('All files', '*.*')) 

        # Show the open file dialog by specifying path 
        #(filetypes=filetypes, initialdir="./")
        path = fd.askdirectory() 

        # Insert the text extracted from file in a textfield 
        entry.delete(0, tk.END)
        entry.insert(0, path)

def create_paths_grid(parent) -> tk.Frame:
        my_grid = tk.Frame(parent)
        my_grid.columnconfigure(0, weight=1)
        my_grid.columnconfigure(1, weight=1)
        my_grid.columnconfigure(2, weight=1)

        l1 = tk.Label(my_grid, 
                      text = "Proxies path:", 
                      font=(FONT_LABEL, FONT_SIZE_LABEL),
                      pady=20)
        l2 = tk.Label(my_grid, 
                      text = "Raws path:", 
                      font=(FONT_LABEL, FONT_SIZE_LABEL),
                      pady=20)
        l3 = tk.Label(my_grid, 
                      text = "Dump file:", 
                      font=(FONT_LABEL, FONT_SIZE_LABEL),
                      pady=20)

        e1 = tk.Entry(my_grid, fg="grey")
        e1.insert(0, "proj/jpgs/yes/final/")
        e2 = tk.Entry(my_grid, fg="grey")
        e2.insert(0, "proj/raws/")
        e3 = tk.Entry(my_grid, fg="grey")
        e3.insert(0, "proj/")

        #command=
        btn1 = tk.Button(my_grid, text=BUTTONS_TEXT, font=(FONT_BUTTONS, BUTTONS_FONT_SIZE), command=lambda: open_dialog_path(e1))
        btn2 = tk.Button(my_grid, text=BUTTONS_TEXT, font=(FONT_BUTTONS, BUTTONS_FONT_SIZE), command=lambda: open_dialog_path(e2))
        btn3 = tk.Button(my_grid, text=BUTTONS_TEXT, font=(FONT_BUTTONS, BUTTONS_FONT_SIZE), command=lambda: open_dialog_path(e3))

        l1.grid(row = 0, column = 0, sticky = tk.W, pady = 2, padx = 2)
        l2.grid(row = 1, column = 0, sticky = tk.W, pady = 2, padx = 2)
        l3.grid(row = 2, column = 0, sticky = tk.W, pady = 2, padx = 2)

        e1.grid(row = 0, column = 1, sticky = tk.E, pady = 2, padx = 2)
        e2.grid(row = 1, column = 1, sticky = tk.E, pady = 2, padx = 2)
        e3.grid(row = 2, column = 1, sticky = tk.E, pady = 2, padx = 2)
   
        btn1.grid(row = 0, column = 2, sticky = tk.W, pady = 2, padx = 2)
        btn2.grid(row = 1, column = 2, sticky = tk.W, pady = 2, padx = 2)
        btn3.grid(row = 2, column = 2, sticky = tk.W, pady = 2, padx = 2)

        my_grid.pack(pady=20)

        return my_grid