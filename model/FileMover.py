import os
import shutil
import filecmp

class FileMover():
    def __init__(self):
        self._jpgsPath = None
        self._rawsPath = None
        self._wantsFolder = False
        self._finalFolderName = ""
        self._rawEnding = ".dng"
        self._jpgEnding = ""

    def _getJpgsNames(self, path):
        jpgFileNames = set(
            filter(lambda x: ".jpg" in x, os.listdir(path))
        )
        return jpgFileNames

    def _extractJpgName(self, fullPath):
        name = ""
        fullPath = fullPath[:-4] # .jpg out
        for i in range(len(fullPath)-1, -1, -1):
            c = fullPath[i]
            if c == "/": break
            name += c
    
        return name[::-1]
        
    def _getRawPaths(self, path, jpgsSet):
        # Now gotta grab from / (...) .jpg
        # And compose path + (...) + .dng/raw/etc

        rawsPaths = []

        for jpgPath in jpgsSet:
            jpgName = self._extractJpgName(jpgPath)
            rawPath = path + jpgName + self._rawEnding
            rawsPaths.append(rawPath)

        return rawsPaths

    def _getDestRawPath(self, oriRawPath, finalDirectoryPath):
        fileName = ""

        for i in range(len(oriRawPath) - 1, -1, -1):
            c = oriRawPath[i]
            if c == "/": break
            fileName += c
    
        return finalDirectoryPath + "/" + fileName[::-1]
            
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
        oriRawsPathList = self._getRawPaths(self._rawsPath, jpgsSet)
        finalPath = self._jpgsPath

        if self._wantsFolder:
            finalPath = os.path.join(finalPath, self._finalFolderName)
            if not os.path.exists(finalPath):
                os.mkdir(finalPath)

        for oriRawImgPath in oriRawsPathList:
            shutil.copy2(oriRawImgPath, finalPath)
            safe_counter = 0
            destRawImgpath = self._getDestRawPath(oriRawImgPath, finalPath)

            while not filecmp.cmp(oriRawImgPath, destRawImgpath):
                if os.path.exists(finalPath):
                    os.remove(finalPath)
                shutil.copy2(oriRawImgPath, finalPath)
                safe_counter += 1
                if safe_counter == 20: 
                    raise IOError
            
            # It's checked that the files are the same, delete the original
            os.remove(oriRawImgPath)
        