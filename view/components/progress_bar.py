import tkinter as tk
from tkinter import ttk

class ProgressWindowUpdater:
    def __init__(self, progress, windowRoot, current_filename, current_file_number):
        self.progress = progress
        self.windowRoot = windowRoot
        self.current_filename = current_filename
        self.current_file_number = current_file_number

    def _refresh_root(self):
        self.windowRoot.update_idletasks()
        self.windowRoot.update()

    def update_progress_bar(self, value):
        self.progress['value'] = value
        self._refresh_root()
    
    def update_current_file(self, filename, file_number):
        self.current_filename.config(text = filename)
        self.current_file_number.config(text = file_number)
        self._refresh_root()

def prompt_progress_windows(function_to_run):
    root = tk.Tk()
    root.geometry("500x600")

    current_file_name_label = tk.Label(root,text="templateFile001.dng",font=("Px ToshibaLCD 8x16", 20))
    current_file_name_label.pack(padx=10, pady=10)

    current_file_number = tk.Label(root,text="1/100",font=("Px ToshibaLCD 8x16", 20))
    current_file_number.pack(padx=10, pady=10)
    
    prog_bar = ttk.Progressbar(root, orient='horizontal', length=200, mode='determinate', maximum=100)
    prog_bar.pack(pady=20, padx=20)

    cancel_button = tk.Button(root, text="Cancel",
                        font=("Agave, Bold", 20),
                        command=root.destroy,
                        fg="lightgoldenrodyellow",
                        bg="lemonchiffon4",
                        width=15,
                        height=2)
    cancel_button.pack(padx=10, pady=10)

    guiUpdater = ProgressWindowUpdater(prog_bar, root, current_file_name_label, current_file_number)
    function_to_run(guiUpdater)

    root.destroy()

    root.mainloop()
