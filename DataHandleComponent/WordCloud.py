import wordcloud
import PIL
import numpy
import jieba
import matplotlib
import os

class WordCloud(object):
    def __init__(self):
        self.fontPath = 'C:\\Windows\\Fonts\\simsun.ttc'
        self.output = os.getcwd() + '\\output.png'
        self.backgroundColor = 'white'


    def SetParam(self, **args):
        if args.get('fontPath', None):
            self.fontPath = args['font']
        if args.get('backgroundColor', None):
            self.backgroundColor = args['backgroundColor']
        if args.get('output', None):
            self.output = args['output']


    def __TransCn(self, text):
        wordLst = jieba.cut(text)
        res = ' '.join(wordLst)
        return res


    def Generate(self, text: str,  backgroundFile: str = '', isChines: bool = False, 
        isSave: bool = False):
        
        if isChines:
            text = self.__TransCn(text)

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

