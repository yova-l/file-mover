import os

or_path = "/home/giovanni/Desktop/github-repos/file-mover/origin"
des_path = "/home/giovanni/Desktop/github-repos/file-mover/dest"

class FileMover():
    def __init__(self, opath=None, dpath=None) -> None:
        self.origin = opath
        self.dest = dpath
    
    def set_or(self, path):
        self.origin = path

    def set_dest(self, path):
        self.dest = path

    def get_or(self):
        return self.origin

    def get_dest(self):
        return self.dest
    
my_fyle_mover = FileMover(or_path, des_path) # Can initiate only with 1 param why?
#my_fyle_mover.set_dest = des_path

dest_list = os.listdir(my_fyle_mover.get_dest())
print("Files and directories in Destination:")
print(dest_list)

or_list = os.listdir(my_fyle_mover.get_or())
print("Files and directories in Origin:")
print(or_list)