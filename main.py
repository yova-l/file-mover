from model.FileMover import FileMover
from view.FileMover import FileMoverGUI

jpgs_path = "./jpgs/"
raws_path = "./raws/"
raw_folder_name = "MyRaws"
jpg_ext = ".jpg"
raw_ext = ".dng"
dump_path = "./"

mfm = FileMover()

FileMoverGUI(mfm)

#No tengo seteado los bools de dump por ej => no deberia checkear...

# /home/giovanni/Desktop/github-repos/file-mover/tests/jpgs Asi lo da opendiag, cambiar para que no explote...
#SI OSI LO DEL ARRIBA

#AGREGAR BOTTON EN/ESP

# CAN't invoke grab commnad ??

