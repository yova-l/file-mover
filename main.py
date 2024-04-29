import os

or_path = "/home/giovanni/Desktop/github-repos/file-mover/origin"
des_path = "/home/giovanni/Desktop/github-repos/file-mover/dest"

class FileMover():
    def __init__(self):
        self.origin = None
        self.dest = None
        self.wantsFolder = False
    
    def setOr(self, path):
        self.origin = path

    def setDest(self, path):
        self.dest = path

    def getOr(self):
        return self.origin

    def getDest(self):
        return self.dest
    
    def wantFolder(self):
        self.wantsFolder = True
    
    def moveToDest(self):
        # Pending...
        return "OK"
    
    
mfm = FileMover()
mfm.setOr(or_path)
mfm.setDest(des_path)

# TEST
print(f"Files in origin: { os.listdir(mfm.getOr()) }")
print(f"Files in dest: { os.listdir(mfm.getDest()) }")