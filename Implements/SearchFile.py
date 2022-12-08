import os


def allFiles(dir)->str:
    for root, ds, fs in os.walk(dir):
        for f in fs:
            file_path = os.path.join(root, f)
            yield file_path

def main():
    dir = input("input dir path: ")
    target_file = input("input file name: ")
    for f in allFiles(dir):
        if f.find(target_file) >= 0:
            print(f)


if __name__ == "__main__":
    main()