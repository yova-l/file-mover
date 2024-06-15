from model.FileMover import FileMover
from view.FileMover import FileMoverGUI

mfm = FileMover()

FileMoverGUI(mfm)

# Cancel program in the middle of a copy? # handle this properly, if you cancel but 
# then try another copy, it shluod check that is not in destination, if it is continue, if not copy

#raro que no se cierra bien la ventana de progreso, no popea el siguiente succes

# TO EXE
# TEST ON WINDWOS/LIN/MAC


# CREAR MINI WEB CV CON LINKS A PROYECTOS