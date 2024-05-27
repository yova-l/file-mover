from model.FileMover import FileMover

jpgs_path = "./jpgs/"
raws_path = "./raws/"
raw_folder_name = "MyRaws"


## CASO QUIERE MOVER, ESTAN TODOS LOS FILES, Y QUIERE CARPETA // OK
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
# mfm.setFolderName(raw_folder_name) # Esto es ignorado OK
# mfm.moveRaws()
###############################################################################

## CASO QUIERE MOVER, NO ESTAN TODOS LOS RAWS // OK!!!
# mfm = FileMover()
# mfm.setJpgsPath(jpgs_path)
# mfm.setRawsPath(raws_path)

# mfm.wantFolder()
# mfm.dontWantFolder()

# mfm.setFolderName(raw_folder_name)
# mfm.moveRaws()

###############################################################################

## CASO QUIERE COPIAR, ESTAN TODOS (aunque no esten funciona ahora OK!!!)
# mfm = FileMover()
# mfm.setJpgsPath(jpgs_path)
# mfm.setRawsPath(raws_path)

# mfm.wantFolder()
# mfm.wantCopy()
# mfm.dontWantCopy()

# mfm.setFolderName(raw_folder_name)
# mfm.moveRaws()

###############################################################################
# SE AGREGO PARA DEFINIR LAS EXTENSIONES Y SETEAR SI QUIERO O NO DUMP, CHECKEAR
# REacomodar la clase
