import tkinter as tk
from tkinter import messagebox

from components.menu import create_menu

WINDOW_TITLE = "FileMover"
TITLE = "Welcome FileMover! Set the settings accordingly to your needs and let the magic happen!"
FONT = "Px ToshibaLCD 8x16"
TITLE_FONT_SIZE = 18

class FileMoverGUI:
    def __init__(self):
        self.root = tk.Tk()

        # Menu -------------------------------------------------------------------
        self.menubar = tk.Menu(self.root)

        self.filemenu = create_menu(self.menubar)

        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.root.config(menu=self.menubar)
        # ------------------------------------------------------------------------

        # Windows Title
        self.root.title(WINDOW_TITLE) 

        # Application Title
        self.label = tk.Label(self.root, text=TITLE, font=(FONT, TITLE_FONT_SIZE))
        self.label.pack(padx=10, pady=10)
        
        #FROM HERE
        # this will create a label widget
        l1 = Label(master, text = "First:")
        l2 = Label(master, text = "Second:")
        
        # grid method to arrange labels in respective
        # rows and columns as specified
        l1.grid(row = 0, column = 0, sticky = W, pady = 2)
        l2.grid(row = 1, column = 0, sticky = W, pady = 2)
        
        # entry widgets, used to take entry from user
        e1 = Entry(master)
        e2 = Entry(master)
        
        # this will arrange entry widgets
        e1.grid(row = 0, column = 1, pady = 2)
        e2.grid(row = 1, column = 1, pady = 2)

        #######
        my_entry = tk.Entry(self.root)
        my_entry.pack()

        self.check_state =  tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=("Px ToshibaLCD 8x16", 12), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show meesage", font=("Px ToshibaLCD 8x16", 15), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.clearbtn = tk.Button(self.root, text="Clear", font=("Px ToshibaLCD 8x16", 15), command=self.clear)
        self.clearbtn.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()

    # def about_message(self):
    #     messagebox.showinfo(title="About FileMover", message=ABOUT_MESSAGE)

    # def donate_web(self):
    #     messagebox.showinfo(title="About FileMover", message=ABOUT_MESSAGE)

    def clear(self):
        self.textbox.delete("1.0", tk.END)

    def on_closing(self):
        wanna_leave = messagebox.askyesno(title="Yleaving?", message="Sure you wanna leave bud?")

        if wanna_leave:
            messagebox.showinfo(title="Fuck", message="Bye friend")
            self.root.destroy()
        
        else:
            messagebox.showinfo(title="Nice", message="Glad u stayed bud")
        

    def shortcut(self, event):
        # print(event) # You can see what are the values of the attributes to further checks and code the behaviuor
        # print(event.state)
        # print(event.keysym)
        if event.state == 20 and event.keysym == "Return":
            # ctrl + enter was pressed
            print("crtl+enter was pressed, launching show message")
            self.show_message()

    def show_message(self):
        state = self.check_state.get()
        all_text = self.textbox.get('1.0', tk.END) # Get everything
            
        if state == 0:
            print(all_text)

        else:
            messagebox.showinfo(title="Message", message=all_text)
    
FileMoverGUI()