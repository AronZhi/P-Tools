import wordcloud
import PIL
import numpy
import jieba
import matplotlib
import os

class WordCloudAssistant(object):
    def __init__(self):
        self.fontPath = 'C:\\Windows\\Fonts\\simsun.ttc'
        self.output = os.getcwd() + '\\output.png'
        self.backgroundColor = 'white'

    
    def SetParam(self, font: str = '', backgroundColor: str = '', output: str = ''):
        self.fontPath = font
        self.backgroundColor = backgroundColor
        self.output = output


    def TransCn(self, text):
        wordLst = jieba.cut(text)
        res = ' '.join(wordLst)
        return res


    def Generate(self, text: str,  backgroundFile: str = '', isChines: bool = False, 
        isSave: bool = False):
        
        if isChines:
            text = self.TransCn(text)

        arags = {}
        arags['font_path'] = self.fontPath
        arags['background_color'] = self.backgroundColor
        if backgroundFile:
            image = PIL.Image.open(backgroundFile)
            mask = numpy.array(image)
            arags['mask'] = mask

        cloud = wordcloud.WordCloud(**arags).generate(text)
        
        if backgroundFile:
            image_color = wordcloud.ImageColorGenerator(arags['mask'])
            cloud.recolor(color_func = image_color)

        image_produce = cloud.to_image()
        image_produce.show()
        if isSave:
            cloud.to_file(self.output)
