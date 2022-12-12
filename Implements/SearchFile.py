import os


def allFiles(dir) -> str:
    for root, _, fs in os.walk(dir):
        for f in fs:
            yield os.path.join(root, f)

def main():  # sourcery skip: avoid-builtin-shadow
    dir = input("input dir path: ")
    target_file = input("input file name: ")
    for f in allFiles(dir):
        if f.find(target_file) >= 0:
            print(f)


if __name__ == "__main__":
    main()