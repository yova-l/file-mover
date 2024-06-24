import os
import filecmp

def copy_file_with_progress(guiUpdater, src, dst, filename, current_fumber, total_files):
    total_size = os.path.getsize(src)
    copied_size = 0
    
    with open(src, 'rb') as src_file:
        with open(dst, 'wb') as dst_file:
            while True:
                chunk = src_file.read(1024 * 1024)  # Read in 1MB chunks
                if not chunk:
                    break
                dst_file.write(chunk)
                copied_size += len(chunk)
                
                # Calculate progress
                progress_value = (copied_size / total_size) * 100
   
                guiUpdater.update_progress_bar(progress_value)
                guiUpdater.update_current_file(filename, f"{current_fumber}/{total_files}")

class FileMover():
    def __init__(self):
        self._jpgsPath = ""
        self._rawsPath = ""
        self._dumpPath = ""
        self._wantsFolder = True
        self._wantsDump = True
        self._finalFolderName = ""
        self._rawExtension = ""
        self._jpgExtension = ""
        self._notFounded = []
        self._isCopy = True

    # Setters
    def setJpgExt(self, extension: str) -> None: self._jpgExtension = extension
    def setRawExt(self, extension: str) -> None: self._rawExtension = extension
    def setFolderName(self, name: str) -> None: self._finalFolderName = name
    def setWantFolder(self, value: bool) -> None: self._wantsFolder = value
    def setWantCopy(self, value: bool) -> None: self._isCopy = value
    def setWantDump(self, value: bool) -> None: self._wantsDump = value
    def setJpgsPath(self, path: str) -> None: self._jpgsPath = path if path.endswith("/") else (path + "/")
    def setRawsPath(self, path: str) -> None: self._rawsPath = path if path.endswith("/") else (path + "/")
    def setDumpDest(self, path: str): self._dumpPath = path if path.endswith("/") else (path + "/")

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
        rawsNames = []

        for jpgPath in jpgsSet:
            jpgName = self._extractJpgName(jpgPath)
            rawName = jpgName + self._rawExtension
            rawPath = path + rawName
            rawsPaths.append(rawPath)
            rawsNames.append(rawName)

        return rawsPaths, rawsNames

    def _getDestinationRawPath(self, oriRawPath, finalDirectoryPath):
        fileName = ""
        for i in range(len(oriRawPath) - 1, -1, -1):
            c = oriRawPath[i]
            if c == "/" or c == "\\": break
            fileName += c
        return finalDirectoryPath + "/" + fileName[::-1]
            
    def moveRaws(self, guiUpdater):
        jpgsSet = self._getJpgsNames(self._jpgsPath)

        if len(jpgsSet) == 0: return

        originRawsPathList, originRawsNames = self._getRawPaths(self._rawsPath, jpgsSet)
        finalPath = self._jpgsPath

        if len(originRawsPathList) != 0 and self._wantsFolder:
            finalPath = os.path.join(finalPath, self._finalFolderName)
            if not os.path.exists(finalPath):
                os.mkdir(finalPath)

        for i in range(len(originRawsPathList)):
            originRawImgPath = originRawsPathList[i]
            originRawName = originRawsNames[i]

            if not os.path.exists(originRawImgPath): # Is the raw in the expected folder?
                self._notFounded.append(originRawImgPath)
                continue
            
            destinationRawImgPath = self._getDestinationRawPath(originRawImgPath, finalPath)
            if os.path.exists(destinationRawImgPath) and filecmp.cmp(originRawImgPath, destinationRawImgPath):
                continue # The file is already in the destination folder
            
            # If we are here, the file is not in the destination folder or the copy was interrupted
            copy_file_with_progress(guiUpdater, originRawImgPath, destinationRawImgPath, originRawName, i+1, len(originRawsPathList))
            safe_counter = 0
            succesfull_copy = filecmp.cmp(originRawImgPath, destinationRawImgPath)

            while not succesfull_copy:
                if os.path.exists(finalPath):
                    os.remove(finalPath)
                copy_file_with_progress(guiUpdater, originRawImgPath, destinationRawImgPath, originRawName, i+1, len(originRawsPathList))
                safe_counter += 1
                if safe_counter == 20: 
                    raise IOError
                succesfull_copy = filecmp.cmp(originRawImgPath, destinationRawImgPath)
            
            # It's checked that the files are the same, delete the original (only if it's not a copy)
            if not self._isCopy:
                os.remove(originRawImgPath)

        self._dumpNotFounded()