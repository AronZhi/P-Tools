from DataHandleComponent.WordCloud import *


def main():
    wcAssistant = WordCloud()

    with open(os.getcwd() + '\\Resource\\minister.txt', 'r', encoding='utf8') as fp:
        text = fp.read()
        wcAssistant.Generate(text = text, backgroundFile = os.getcwd() + '\\Resource\\test1.jpg', isChines = True)


if __name__ == '__main__':
    main()
        