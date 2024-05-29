import tkinter as tk

FONT_BUTTONS = "Agave, Bold"
FONT_LABEL = "Agave"
FONT_SIZE_LABEL = 11
BUTTONS_TEXT = "Choose folder..."
BUTTONS_FONT_SIZE = 13

def create_params_grid(parent) -> tk.Frame:
        my_grid = tk.Frame(parent)
        my_grid.columnconfigure(0, weight=1)
        my_grid.columnconfigure(1, weight=1)

        # Some lightgrey styling would be great
        e1 = tk.Entry(my_grid, fg="grey")
        e1.insert(0, '.jpg')
        e2 = tk.Entry(my_grid, fg="grey")
        e2.insert(0, '.dng')
        e3 = tk.Entry(my_grid, fg="grey")
        e3.insert(0, 'MyRaws')

        le1 = tk.Label(my_grid, text = "e.g .jpg, .jpeg, .mp4", 
                       font=(FONT_LABEL, FONT_SIZE_LABEL))
        le2 = tk.Label(my_grid, text = "e.g, .raw, .dng, .rw2", 
                       font=(FONT_LABEL, FONT_SIZE_LABEL))
        le3 = tk.Label(my_grid, text = "e.g MyRaws", 
                       font=(FONT_LABEL, FONT_SIZE_LABEL))
        
        chb1val = tk.BooleanVar() # BUT NOW HOW CAN THE PORGRAM ACCESS THESE
        chb2val = tk.BooleanVar()
        chb3val = tk.BooleanVar()
        chb1 = tk.Checkbutton(my_grid, text="Move raws into a new folder?", variable=chb1val)
        chb2 = tk.Checkbutton(my_grid, text="Want txt with missing raws?", variable=chb2val)
        chb3 = tk.Checkbutton(my_grid, text="Keep the original raws?", variable=chb3val)

        e1.grid(row = 0, column = 0, sticky = tk.W, pady = 2, padx = 2)
        le1.grid(row = 1, column = 0, sticky = tk.W, pady = (0,20), padx = 2)

        e2.grid(row = 2, column = 0, sticky = tk.W, pady = 2, padx = 2)
        le2.grid(row = 3, column = 0, sticky = tk.W, pady = (0,20), padx = 2)

        e3.grid(row = 4, column = 0, sticky = tk.W, pady = 2, padx = 2)
        le3.grid(row = 5, column = 0, sticky = tk.W, pady = (0,20), padx = 2)

        chb1.grid(row = 1, column = 3, sticky = tk.W, pady = 5, padx = (50, 0))
        chb2.grid(row = 2, column = 3, sticky = tk.W, pady = 5, padx = (50, 0))
        chb3.grid(row = 3, column = 3, sticky = tk.W, pady = 5, padx = (50, 0))

        my_grid.pack()

        return my_grid