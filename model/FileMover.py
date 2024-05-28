import os
import shutil
import filecmp
import platform

OS = platform.system()

class FileMover():
    def __init__(self):
        self._jpgsPath = "./"
        self._rawsPath = "./"
        self._dumpPath = "./"
        self._wantsFolder = True
        self._wantsDump = True
        self._finalFolderName = "MyRaws"
        self._rawExtension = ".dng"
        self._jpgExtension = ".jpg"
        self._notFounded = []
        self._isCopy = True

    # Setters
    def setJpgExt(self, extension: str) -> None: self._jpgExtension = extension
    def setRawExt(self, extension: str) -> None: self._rawExtension = extension
    def setFolderName(self, name: str) -> None: self._finalFolderName = name
    def setJpgsPath(self, path: str) -> None: self._jpgsPath = path
    def setRawsPath(self, path: str) -> None: self._rawsPath = path
    def wantFolder(self) -> None: self._wantsFolder = True
    def dontWantFolder(self) -> None: self._wantsFolder = False
    def wantCopy(self) -> None: self._isCopy = True
    def dontWantCopy(self) -> None: self._isCopy = False
    def wantDump(self) -> None: self._wantsDump = True
    def dontWantDump(self) -> None: self._wantsDump = False
    def setDumpDest(self, path: str): self._dumpPath = path

    def _dumpNotFounded(self):
        if len(self._notFounded) == 0 or not self._wantsDump: return

        with open(f"{self._dumpPath}dump.txt", "w") as f:
            for path in self._notFounded:
                # Writing data to a file
                f.write(f"Not founded: {os.path.abspath(path)}\n")
 
        self._notFounded = []

    def _getJpgsNames(self, path: str) -> set:
        """
        It will search for the files that meet the set extension in the already set folder.
        Returns a set containing all the corresponding paths
        """
        jpgFileNames = set(
            filter(lambda x: f"{self._jpgExtension}" in x, os.listdir(path))
        )
        return jpgFileNames

    def _extractJpgName(self, fullPath: str):
        # fullPath is going to be somthing like: /home/Desktop/pics/jpg/selection/yes/123456.jpeg
        name = ""
        point_index = len(fullPath) - 1

        # Dismiss the file extension
        for i in range(point_index, -1, -1):
            if fullPath[i] == ".": break
            point_index -= 1

        # Extract the filename
        for i in range(point_index-1, -1, -1):
            c = fullPath[i]
            if c == "/" or c == "\\": break
            name += c
    
        return name[::-1]
        
    def _getRawPaths(self, path: str, jpgsSet: set) -> list:
        """Given a set of jpgs paths, it will search for all the raw corresponding pairs and return them 
        in a list.
        """
        rawsPaths = []

        for jpgPath in jpgsSet:
            jpgName = self._extractJpgName(jpgPath)
            rawPath = path + jpgName + self._rawExtension
            rawsPaths.append(rawPath)

        return rawsPaths

    def _getDestinationRawPath(self, oriRawPath, finalDirectoryPath):
        fileName = ""

        for i in range(len(oriRawPath) - 1, -1, -1):
            c = oriRawPath[i]
            if c == "/" or c == "\\": break
            fileName += c

        # WHAT IF WE ARE ON WIDNOWS?? Check the above OS variable might be a solution, test it after
        return finalDirectoryPath + "/" + fileName[::-1]
            
    def moveRaws(self):
        jpgsSet = self._getJpgsNames(self._jpgsPath)
        originRawsPathList = self._getRawPaths(self._rawsPath, jpgsSet)
        finalPath = self._jpgsPath

        if self._wantsFolder:
            finalPath = os.path.join(finalPath, self._finalFolderName)
            if not os.path.exists(finalPath):
                os.mkdir(finalPath)

        for originRawImgPath in originRawsPathList:
            if not os.path.exists(originRawImgPath): # Is the raw in the expected folder?
                self._notFounded.append(originRawImgPath)
                continue

            shutil.copy2(originRawImgPath, finalPath)
            safe_counter = 0
            destinationRawImgPath = self._getDestinationRawPath(originRawImgPath, finalPath)
            succesfull_copy = filecmp.cmp(originRawImgPath, destinationRawImgPath)

            while not succesfull_copy:
                if os.path.exists(finalPath):
                    os.remove(finalPath)
                shutil.copy2(originRawImgPath, finalPath)
                safe_counter += 1
                if safe_counter == 20: 
                    raise IOError
                succesfull_copy = filecmp.cmp(originRawImgPath, destinationRawImgPath)
            
            # It's checked that the files are the same, delete the original (only if it's not a copy)
            if not self._isCopy:
                os.remove(originRawImgPath)

        self._dumpNotFounded()
         
        