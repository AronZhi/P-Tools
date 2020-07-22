import site

MyPackFile = '\\mypkt.pth'

def AddSourceRoot(rootPath: str)->bool:
    path = site.getsitepackages()
    if path is None or len(path) < 2:
        return False
    
    global MyPackFile
    packFilePath = path[1] + MyPackFile
    try:
        with open(packFilePath, 'r+') as packFile:
            text = packFile.read()
            if text.find(rootPath) >= 0:
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


def main():
    rootPath = input()
    ret = AddSourceRoot(rootPath)
    print(ret)

if __name__ == '__main__':
    main()