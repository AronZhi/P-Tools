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


    def Generate(self, text: str,  backgroundFile: str = '', isChines: bool = False):
        if isChines:
            text = self.TransCn(text)

        if backgroundFile:
            image = PIL.Image.open(backgroundFile)
            mask = numpy.array(image)

            cloud = wordcloud.WordCloud(
                font_path = self.fontPath,
                background_color=self.backgroundColor,
                mask = mask
                ).generate(text)
            
            image_color = wordcloud.ImageColorGenerator(mask)
            cloud.recolor(color_func=image_color)
            image_produce = cloud.to_image()
            image_produce.show()
            cloud.to_file(self.output)
        else:
            cloud = wordcloud.WordCloud(font_path = self.fontPath,
                background_color=self.backgroundColor).generate(text)
            
            image_produce = cloud.to_image()
            image_produce.show()
            cloud.to_file(self.output)
               
