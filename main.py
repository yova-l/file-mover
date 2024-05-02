import os
import shutil
import filecmp

or_path = "/home/giovanni/Desktop/github-repos/file-mover/origin/"
des_path = "/home/giovanni/Desktop/github-repos/file-mover/dest/"
RAW_FOLDER_NAME = "raws"

class FileMover():
    def __init__(self):
        self._jpgsPath = None
        self._rawsPath = None
        self._wantsFolder = False
    
    def setJpgsPath(self, path):
        self._jpgsPath = path

    def setRawsPath(self, path):
        self._rawsPath = path

    def getJpgsPath(self):
        return self._jpgsPath

    def getRawsPath(self):
        return self._rawsPath
    
    def wantFolder(self):
        self._wantsFolder = True
    
    def dontWantFolder(self):
        self._wantsFolder = False
    
    def _getJpgsNames(path):
        jpgFileNames = set(
            filter(lambda x: ".jpg" in x, os.listdir(path))
        )


    def _getRawPaths(path, jpgsSet):
        pass

    def copyRaws(self):
        pass

    def moveRaws(self):
        jpgsSet = self._getJpgsNames(self._jpgsPath)
        rawsPathList = self._getRawPaths(self._rawsPath, jpgsSet)
        finalPath = self._jpgsPath

        if self.wantFolder:
            finalPath = os.path.join(finalPath, RAW_FOLDER_NAME)
            if not os.path.exists(finalPath):
                os.mkdir(finalPath)

        for rawImgPath in rawsPathList:
            shutil.copy2(rawImgPath, finalPath)
            safe_counter = 0

            while not filecmp.cmp(rawImgPath, finalPath):
                if os.path.exists(finalPath):
                    os.remove(finalPath)
                shutil.copy2(rawImgPath, finalPath)
                safe_counter += 1
                if safe_counter == 20: 
                    raise IOError
            
            # It's checked that the files are the same, delete the original
            os.remove(rawImgPath)
        


    
mfm = FileMover()
mfm.setOr(or_path)
mfm.setDest(des_path)

# TEST
print(f"Files in origin: { os.listdir(mfm.getOr()) }")
print(f"Files in dest: { os.listdir(mfm.getDest()) }")