import wordcloud
import PIL
import numpy
import jieba
import matplotlib
import os

from .BaseChart import *

class WordCloud(BaseChart):
    def __init__(self):
        """
        HandleData函数传入文本数据
        """
        BaseChart.__init__(self)
        self.args = dict()
    
    def SetParam(self, **kwargs):
        """
        backgroundColor: 背景颜色,默认白色
        backgroundFile: 背景图片,默认为空
        fontPath: 字体路径
        chinse: 是否是中文，如果是中文，需要设置中文fontPath
        save: 是否保存生成的图片
        output: 生成图片的保存路径, 默认当前路径
        show: 是否显示生成的图片
        """
        BaseChart.SetParam(self)
        self.args['background_color'] = kwargs.get('backgroundColor', 'white')
        if kwargs.get('fontPath', None):
            self.args['font_path'] = kwargs['fontPath']
        if kwargs.get('backgroundFile', None):
            if os.path.exists(kwargs['backgroundFile']):
                image = PIL.Image.open(kwargs['backgroundFile'])
                mask = numpy.array(image)
                self.args['mask'] = mask
        if kwargs.get('chinse', False):
            wordLst = jieba.cut(self.data)
            self.data = ' '.join(wordLst)
    
    def Generate(self):
        cloud = wordcloud.WordCloud(**self.args).generate(self.data)
        if 'mask' in self.args:
            image_color = wordcloud.ImageColorGenerator(self.args['mask'])
            cloud.recolor(color_func = image_color)
        image_produce = cloud.to_image()
        if self.show:
            image_produce.show()
        if self.save:
            cloud.to_file(self.output)
