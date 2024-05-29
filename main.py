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

## CASO QUIERE COPIAR, ESTAN TODOS LOS FILES, Y QUIERE CARPETA // OK
# mfm = FileMover()

# mfm.setJpgsPath(jpgs_path)
# mfm.setRawsPath(raws_path)

# mfm.wantFolder()
# mfm.setFolderName(raw_folder_name)

# mfm.moveRaws()
#############################################################################

## CASO QUIERE MOVER, ESTAN TODOS LOS FILES, Y NO QUIERE CARPETA // OK
# mfm = FileMover()

# mfm.setJpgsPath(jpgs_path)
# mfm.setRawsPath(raws_path)

# mfm.setDumpDest(jpgs_path)
# mfm.dontWantDump()
# mfm.dontWantFolder()

# mfm.setFolderName(raw_folder_name) # Esto es ignorado OK

# mfm.moveRaws()
###############################################################################

## CASO QUIERE MOVER, NO ESTAN TODOS LOS RAWS // OK!!!
# mfm = FileMover()
# mfm.setJpgsPath(jpgs_path)
# mfm.setRawsPath(raws_path)

# mfm.wantFolder()

# mfm.setFolderName(raw_folder_name)
# mfm.moveRaws()

###############################################################################

## CASO QUIERE COPIAR, ESTAN TODOS (aunque no esten funciona ahora OK!!!)
# mfm = FileMover()

# mfm.setJpgsPath(jpgs_path)
# mfm.setRawsPath(raws_path)
# mfm.setDumpDest(jpgs_path)
# mfm.setFolderName(raw_folder_name)
# mfm.setJpgExt(jpg_ext)
# mfm.setRawExt(raw_ext)

# mfm.wantDump()
# mfm.wantFolder()
# mfm.dontWantCopy()

# mfm.moveRaws()

###############################################################################
# SE AGREGO PARA DEFINIR LAS EXTENSIONES Y SETEAR SI QUIERO O NO DUMP, CHECKEAR
# REacomodar la clase
# mfm = FileMover()
# mfm.setJpgsPath(jpgs_path)
# mfm.setRawsPath(raws_path)

# mfm.wantFolder()
# mfm.wantCopy()

# mfm.setJpgExt(jpg_ext)
# mfm.setRawExt(raw_ext)

# mfm.setFolderName(raw_folder_name)
# mfm.moveRaws()