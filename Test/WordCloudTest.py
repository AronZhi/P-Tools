from WordCloudAssistant import *

def main():
    wcAssistant = WordCloudAssistant()

    with open('C:\\WorkSpace\\Spider\\Resource\\minister.txt', 'r', encoding='utf8') as fp:
        text = fp.read()
        wcAssistant.Generate(text = text, backgroundFile = 'C:\\WorkSpace\\Spider\\Resource\\test1.jpg', isChines = True)

if __name__ == '__main__':
    main()
        