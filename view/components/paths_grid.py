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

        l1 = tk.Label(my_grid, 
                      text = "Proxies path:", 
                      font=(FONT_LABEL, FONT_SIZE_LABEL))
        l2 = tk.Label(my_grid, 
                      text = "Raws path:", 
                      font=(FONT_LABEL, FONT_SIZE_LABEL))
        l3 = tk.Label(my_grid, 
                      text = "Dump file:", 
                      font=(FONT_LABEL, FONT_SIZE_LABEL))

        e1 = tk.Entry(my_grid, fg="grey", name="proxPath", width=40)
        e1.insert(0, "/home/giovanni/Desktop/github-repos/file-mover/tests/jpgs/") 
        e2 = tk.Entry(my_grid, fg="grey", name="rawsPath", width=40)
        e2.insert(0, "/home/giovanni/Desktop/github-repos/file-mover/tests/raws/")
        e3 = tk.Entry(my_grid, fg="grey", name="dumpPath", width=40)
        e3.insert(0, "/home/giovanni/Desktop/github-repos/file-mover/tests/")

        #command=
        btn1 = tk.Button(my_grid, text=BUTTONS_TEXT, font=(FONT_BUTTONS, BUTTONS_FONT_SIZE), command=lambda: open_dialog_path(e1))
        btn2 = tk.Button(my_grid, text=BUTTONS_TEXT, font=(FONT_BUTTONS, BUTTONS_FONT_SIZE), command=lambda: open_dialog_path(e2))
        btn3 = tk.Button(my_grid, text=BUTTONS_TEXT, font=(FONT_BUTTONS, BUTTONS_FONT_SIZE), command=lambda: open_dialog_path(e3))

        l1.grid(row = 1, column = 0, sticky = tk.W, pady = (0,20), padx = 2)
        l2.grid(row = 3, column = 0, sticky = tk.W, pady = (0,20), padx = 2)
        l3.grid(row = 5, column = 0, sticky = tk.W, pady = (0,20), padx = 2)

        e1.grid(row = 0, column = 0, sticky = tk.W)
        e2.grid(row = 2, column = 0, sticky = tk.W)
        e3.grid(row = 4, column = 0, sticky = tk.W)
   
        btn1.grid(row = 0, column = 1, sticky = tk.W)
        btn2.grid(row = 2, column = 1, sticky = tk.W)
        btn3.grid(row = 4, column = 1, sticky = tk.W)

        my_grid.pack(pady=20)

        return my_grid