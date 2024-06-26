import tkinter as tk
from tkinter import messagebox

from .components.menu import create_menu
from .components.paths_grid import create_paths_grid
from .components.params_grid import create_params_grid
from .components.language_selector import create_lang_selector
from .components.progress_bar import prompt_progress_windows

from .constants import ALL_TEXT

LANGUAGES = {"Español": 0, "English": 1}

# Original Development Resolution
DEV_RES_WIDTH = 3840
DEV_WINDOW_WIDTH = 1000
DEV_WINDOW_HEIGHT = 1100

class FileMoverGUI:
    current_lang_index = 1

    def __init__(self, file_mover_model):
        self.file_mover_model = file_mover_model

        self.root = tk.Tk()

        current_screen_width = self.root.winfo_screenwidth()
        current_screen_width = current_screen_width if current_screen_width <= DEV_RES_WIDTH else DEV_RES_WIDTH
        
        scale_factor =  current_screen_width / DEV_RES_WIDTH * 1.10

        self.root.title(ALL_TEXT["main_window_title"]) 

        # Windows sizing 
        width = int(DEV_WINDOW_WIDTH * scale_factor)
        height = int(DEV_WINDOW_HEIGHT * scale_factor)
        self.root.geometry(f"{width}x{height}")

        # Language selector
        self.lang_selector = create_lang_selector(self.root, self.switch_lang)
    
        # Menu -------------------------------------------------------------------
        self.menubar = tk.Menu(self.root)
        self.filemenu = create_menu(self.menubar, self.current_lang_index)
        self.menubar.add_cascade(menu=self.filemenu, label=ALL_TEXT["menu"][self.current_lang_index])
        self.root.config(menu=self.menubar)
        # ------------------------------------------------------------------------

        # Application Title
        self.label = tk.Label(self.root, 
                              text=ALL_TEXT["title"][self.current_lang_index],
                              font=("Px ToshibaLCD 8x16", int(40*scale_factor)))
        self.label.pack(padx=int(10*scale_factor), pady=int(40*scale_factor))

        # Paths Grid
        self.paths_grid = create_paths_grid(self.root, self.current_lang_index, scale_factor) # Already packed 

        # Params grid
        self.params_grid = create_params_grid(self.root, self.current_lang_index, scale_factor) # Already packed

        # Main Button
        self.button = tk.Button(self.root, text=ALL_TEXT["button"],
                                font=("Agave, Bold", int(20*scale_factor)),
                                command=self.move_raws,
                                fg="lightgoldenrodyellow",
                                bg="lemonchiffon4",
                                width=int(25*scale_factor),
                                height=2)
        self.button.pack(padx=int(10*scale_factor), pady=int(10*scale_factor))

        self.lang_selector.pack(padx=int(10*scale_factor), pady=int(10*scale_factor))

        self.root.mainloop()

    def switch_lang(self, *args, **kwargs):
        self.root.destroy()
        str_var = self.lang_selector.get_str_var()
        lang_val_str = str_var.get()
        self.current_lang_index = LANGUAGES[lang_val_str]
        self.__init__(self.file_mover_model)

    def move_raws(self):
        # Strs
        jpg_path = self.paths_grid.nametowidget("proxPath").get()
        raw_path = self.paths_grid.nametowidget("rawsPath").get()
        dump_path = self.paths_grid.nametowidget("dumpPath").get()

        # Strs
        prox_ext = self.params_grid.nametowidget("proxExtension").get()
        raw_ext = self.params_grid.nametowidget("rawExtension").get()
        folder_name = self.params_grid.nametowidget("folderName").get()

        # Booleans
        wants_folder = 'selected' in self.params_grid.nametowidget("moveIntoFolder").state() 
        wants_dump_file = 'selected' in self.params_grid.nametowidget("wantsDumpFile").state()
        wants_copy = 'selected' in self.params_grid.nametowidget("itsCopy").state()
        
        # A method to process all this settings might be better but Ok for now
        self.file_mover_model.setWantCopy(wants_copy)
        self.file_mover_model.setWantDump(wants_dump_file)
        self.file_mover_model.setWantFolder(wants_folder)

        self.file_mover_model.setJpgExt(prox_ext)
        self.file_mover_model.setRawExt(raw_ext)
        self.file_mover_model.setDumpDest(dump_path)
        self.file_mover_model.setFolderName(folder_name)
        self.file_mover_model.setJpgsPath(jpg_path)
        self.file_mover_model.setRawsPath(raw_path)
    
        messagebox.showwarning(title=ALL_TEXT["warn_precopy_title"][self.current_lang_index], message=ALL_TEXT["warn_precopy_text"][self.current_lang_index])

        prompt_progress_windows(self.file_mover_model.moveRaws)

