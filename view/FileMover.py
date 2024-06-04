import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from .components.menu import create_menu
from .components.paths_grid import create_paths_grid
from .components.params_grid import create_params_grid
from .components.language_selector import create_lang_selector

from constants import get_texts

WINDOW_TITLE = "FileMover"

TITLE_FONT = "Px ToshibaLCD 8x16"
TITLE = "Welcome to FileMover!"
TITLE_FONT_SIZE = 35

MAIN_WINDOW_SIZE = "1280x1280"

APP_DESC = "Feel free to just paste the directories or just navigate trough it by pressing the choose folder buttons and select the corresponding locations."

FONT_SIZE = 14
APP_DESC_FONT_SIZE = 11
DEFAULT_FONT = "Agave" 
FONT_BUTTONS = "Agave, Bold"

class FileMoverGUI:
    def __init__(self, file_mover_model):
        self.file_mover_model = file_mover_model # In main we plug both logic and GUI

        self.root = tk.Tk()

        # Windows Title
        self.root.title(WINDOW_TITLE) 

        # Windows sizing
        self.root.geometry(MAIN_WINDOW_SIZE)

        # Language selector
        self.lang_selector = create_lang_selector(self.root)
        texts = get_texts(create_lang_selector.) # NECESITO TRAERME EL STREING VAR

        # Menu -------------------------------------------------------------------
        self.menubar = tk.Menu(self.root)

        self.filemenu = create_menu(self.menubar)

        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.root.config(menu=self.menubar)
        # ------------------------------------------------------------------------

        # Application Title
        self.label = tk.Label(self.root, 
                              text=TITLE, 
                              font=(TITLE_FONT, TITLE_FONT_SIZE))
        self.label.pack(padx=10, pady=50)

        # App description
        self.label = tk.Label(self.root, 
                              text=APP_DESC, 
                              font=(DEFAULT_FONT, APP_DESC_FONT_SIZE),
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
                                font=(FONT_BUTTONS, FONT_SIZE),
                                command=self.move_raws,
                                fg="lightgoldenrodyellow",
                                bg="lemonchiffon4",
                                width=15,
                                height=2)
        self.button.pack(padx=10, pady=10)


        #self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.lang_selector.pack(padx=10, pady=10)

        self.root.mainloop()

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

