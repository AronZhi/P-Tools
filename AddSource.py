import site

MyPackFile = '\\mypkt.pth'

def AddSourceRoot()->bool:
    path = site.getsitepackages()
    if path is None or len(path) < 2:
        return False
    
    global MyPackFile
    packFilePath = path[1] + MyPackFile
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
    path = site.getsitepackages()
    if path is None or len(path) < 2:
        return
    
    global MyPackFile
    packFilePath = path[1] + MyPackFile

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