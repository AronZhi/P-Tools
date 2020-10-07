import site
import os

MyPackFile = 'mypkt.pth'

def GetSitePackFile()->str:
    path = site.getsitepackages()
    global MyPackFile
    if not path:
        return None
    elif len(path) == 1:
        return os.path.join(path[0], MyPackFile)
    else:
        return os.path.join(path[1], MyPackFile)


def AddSourceRoot()->bool:
    packFilePath = GetSitePackFile()
    if not packFilePath:
        return False
    
    rootPath = input('Please input root path:')
    try:
        with open(packFilePath, 'r+') as packFile:
            for line in packFile.readlines():
                if line == rootPath:
                    print('path already exist')
                    return True

            packFile.write('\n')
            packFile.write(rootPath)
    except FileNotFoundError as e:
        with open(packFilePath, 'w') as packFile:
            packFile.write(rootPath)
    except Exception as e:
        print(e)
        return False

    return True


def ViewMyPacket():
    packFilePath = GetSitePackFile()
    if not packFilePath:
        return False

    with open(packFilePath, 'r') as packFile:
            text = packFile.read()
            print(text)


def main():
    while True:
        commond = input('add source packet input 1, view packet input 2, input other exit.  ')
        if commond == '1':
            AddSourceRoot()
        elif commond == '2':
            ViewMyPacket()
        else:
            break

if __name__ == '__main__':
    main()