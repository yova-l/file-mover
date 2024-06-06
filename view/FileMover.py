import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from .components.menu import create_menu
from .components.paths_grid import create_paths_grid
from .components.params_grid import create_params_grid
from .components.language_selector import create_lang_selector

from .constants import ALL_TEXT, CONFIGS

WINDOW_TITLE = "FileMover"
LANGUAGES = {"Español": 0, "English": 1}
CURRENT_LANG_INDEX = 1

# Afuera tener un seguidor de lenguaje, cuando cambie desencana el destroy e init
def switi():
    print("HEYYYY")

class FileMoverGUI:
    current_lang_index = 1

    def __init__(self, file_mover_model):
        self.file_mover_model = file_mover_model # In main we plug both logic and GUI

        self.root = tk.Tk()

        # Windows Title
        self.root.title(WINDOW_TITLE) 

        # Windows sizing
        self.root.geometry(CONFIGS["main_window_default_size"])

        # Language selector
        self.lang_selector = create_lang_selector(self.root)
        #self.lang_val = self.lang_selector.getvar("language_val") # NECESITO TRAERME EL STREING VAR
        self.lang_val = self.lang_selector.get_str_var()
        self.lang_val.trace_add("write", self.switch_lang)
    

        # Menu -------------------------------------------------------------------
        self.menubar = tk.Menu(self.root)

        self.filemenu = create_menu(self.menubar)

        self.menubar.add_cascade(menu=self.filemenu, label="File") #CAmbiar file depende idioma
        self.root.config(menu=self.menubar)
        # ------------------------------------------------------------------------

        print(f"Reborned, lang_ind_val is {self.current_lang_index}")
        # Application Title
        self.label = tk.Label(self.root, 
                              text=ALL_TEXT["title"][self.current_lang_index], #por el moemnto hardcodeamos a english
                              font=(CONFIGS["title_font"], CONFIGS["title_font_size"]))
        self.label.pack(padx=10, pady=50)

        # App description
        self.label = tk.Label(self.root, 
                              text=ALL_TEXT["app_desc"][self.current_lang_index], 
                              font=(CONFIGS["default_font"], CONFIGS["app_desc_font_size"]),
                              width=60,
                              height=7,
                              borderwidth=5,
                              relief="ridge",
                              wraplength=800)
        self.label.pack(padx=10, pady=10)
        
        # Paths Grid
        self.paths_grid = create_paths_grid(self.root) # Already packed 

        # Params grid
        self.params_grid = create_params_grid(self.root) # Already packed

        # Main Button
        self.button = tk.Button(self.root, text="MoveRaws!",
                                font=(CONFIGS["buttons_font"], CONFIGS["font_size"]),
                                command=self.move_raws,
                                fg="lightgoldenrodyellow",
                                bg="lemonchiffon4",
                                width=15,
                                height=2)
        self.button.pack(padx=10, pady=10)


        #self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.lang_selector.pack(padx=10, pady=10)

        self.root.mainloop()

    def switch_lang(self, *args, **kwargs):
        self.root.destroy()
        lang_val_str = self.lang_val.get()
        # print(lang_val_str)
        self.current_lang_index = LANGUAGES[lang_val_str]
        # print(CURRENT_LANG_INDEX)
        self.__init__(self.file_mover_model)

    def move_raws(self):
        """
            FileMover Model current interface
                def setJpgExt(self, extension: str) -> None: self._jpgExtension = extension
                def setRawExt(self, extension: str) -> None: self._rawExtension = extension
                def setFolderName(self, name: str) -> None: self._finalFolderName = name
                def setJpgsPath(self, path: str) -> None: self._jpgsPath = path
                def setRawsPath(self, path: str) -> None: self._rawsPath = path
                def wantFolder(self) -> None: self._wantsFolder = True
                def dontWantFolder(self) -> None: self._wantsFolder = False
                def wantCopy(self) -> None: self._isCopy = True
                def dontWantCopy(self) -> None: self._isCopy = False
                def wantDump(self) -> None: self._wantsDump = True
                def dontWantDump(self) -> None: self._wantsDump = False
                def setDumpDest(self, path: str): self._dumpPath = path
        """
        # Strs
        jpg_path = self.paths_grid.nametowidget("proxPath").get()
        raw_path = self.paths_grid.nametowidget("rawsPath").get()
        dump_path = self.paths_grid.nametowidget("dumpPath").get()

        # Strs
        prox_ext = self.params_grid.nametowidget("proxExtension").get()
        raw_ext = self.params_grid.nametowidget("rawExtension").get()
        folder_name = self.params_grid.nametowidget("folderName").get()

    
        # ttk.Checkbutton().state() = ('selected','focused')
        # Booleans
        wants_folder = 'selected' in self.params_grid.nametowidget("moveIntoFolder").state() 
        wants_dump_file = 'selected' in self.params_grid.nametowidget("wantsDumpFile").state()
        wants_copy = 'selected' in self.params_grid.nametowidget("itsCopy").state()
        
        # A method to process all this args might be better but Ok for now
        self.file_mover_model.setWantCopy(wants_copy)
        self.file_mover_model.setWantDump(wants_dump_file)
        self.file_mover_model.setWantFolder(wants_folder)

        self.file_mover_model.setJpgExt(prox_ext)
        self.file_mover_model.setRawExt(raw_ext)
        self.file_mover_model.setDumpDest(dump_path)
        self.file_mover_model.setFolderName(folder_name)
        self.file_mover_model.setJpgsPath(jpg_path)
        self.file_mover_model.setRawsPath(raw_path)
        
        messagebox.showwarning(title="Attention", message="This might take a while, please wait until the success warning pops up")
        # IT WOULD TAKE A WHILE HOW TO PROMT THE USER THE WAITING TIME

        self.file_mover_model.moveRaws()

        messagebox.showinfo(title="Success", message="Success bb")

