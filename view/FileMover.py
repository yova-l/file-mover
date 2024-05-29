import tkinter as tk
from tkinter import messagebox

from .components.menu import create_menu
from .components.paths_grid import create_paths_grid
from .components.params_grid import create_params_grid

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

#AGREGAR BOTTON EN/ESP

class FileMoverGUI:
    def __init__(self, file_mover_model):
        self.file_mover_model = file_mover_model # In main we plug both logic and GUI

        self.root = tk.Tk()

        # Windows Title
        self.root.title(WINDOW_TITLE) 

        # Windows sizing
        self.root.geometry(MAIN_WINDOW_SIZE)

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

        self.button = tk.Button(self.root, text="MoveRaws!",
                                font=(FONT_BUTTONS, FONT_SIZE),
                                command=self.move_raws,
                                fg="lightgoldenrodyellow",
                                bg="lemonchiffon4",
                                width=15,
                                height=2)
        self.button.pack(padx=10, pady=10)


        #self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()

    def move_raws(self):
        # Tengo que obtener las variables ... y luego.
        """
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
        #self.file_mover_model.moveRaws()
        messagebox.showinfo(title="Success", message="Success bb")

