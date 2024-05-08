import os
import shutil
import filecmp

jpgs_path = "/home/giovanni/Desktop/github-repos/file-mover/jpgs/"
raws_path = "/home/giovanni/Desktop/github-repos/file-mover/raws/"
raw_folder_name = "MyRaws"

class FileMover():
    def __init__(self):
        self._jpgsPath = None
        self._rawsPath = None
        self._wantsFolder = False
        self._finalFolderName = ""
        self._rawEnding = ".dng"
        self._jpgEnding = ""

    def _getJpgsNames(path):
        jpgFileNames = set(
            filter(lambda x: ".jpg" in x, os.listdir(path))
        )
        return jpgFileNames

    def _extractJpgName(fullPath):
        name = ""
        fullPath = fullPath[:-4] # .jpg out
        for i in range(len(fullPath)-1, -1, -1):
            c = fullPath[i]
            if c == "/": break
            name += c
        return reversed(name)
        
    def _getRawPaths(self, path, jpgsSet):
        # Now gotta grab from / (...) .jpg
        # And compose path + (...) + .dng/raw/etc

        rawsPaths = []

        for jpgPath in jpgsSet:
            jpgName = self._extractJpgName(jpgPath)
            rawPath = path + jpgName + self._rawEnding
            raws_path.append(rawPath)

        return raws_path



    def setFolderName(self, name):
        self._finalFolderName = name
    
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
    
    # def copyRaws(self):
    #     pass

    def moveRaws(self):
        jpgsSet = self._getJpgsNames(self._jpgsPath)
        rawsPathList = self._getRawPaths(self._rawsPath, jpgsSet)
        finalPath = self._jpgsPath

        if self.wantFolder:
            finalPath = os.path.join(finalPath, self._finalFolderName)
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
mfm.setJpgsPath(jpgs_path)
mfm.setRawsPath(raws_path)
mfm.wantFolder()
mfm.setFolderName(raw_folder_name)
mfm.moveRaws()

