import os

def GetFileRoot(fileFullPath: str)->str:
    index = fileFullPath.rfind(os.altsep)
    return fileFullPath[:index]