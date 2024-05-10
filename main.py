from model.FileMover import FileMover

jpgs_path = "/home/giovanni/Desktop/github-repos/file-mover/jpgs/"
raws_path = "/home/giovanni/Desktop/github-repos/file-mover/raws/"
raw_folder_name = "MyRaws"

mfm = FileMover()
mfm.setJpgsPath(jpgs_path)
mfm.setRawsPath(raws_path)
mfm.wantFolder()
mfm.setFolderName(raw_folder_name)
mfm.moveRaws()

