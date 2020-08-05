import logging
from logging.handlers import RotatingFileHandler

class LogHandler(logging.Logger):
    def __init__(self, name: str, filename = ''):
        # super init
        logging.Logger.__init__(self, name)
        if filename == '':
            filename = name + '.log'
    
        # create format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # set console log output format
        try:
            consoleHd = logging.StreamHandler()
            consoleHd.setLevel(logging.INFO)
            consoleHd.setFormatter(formatter)
            self.addHandler(consoleHd)
        except Exception as reason:
            self.error("set console output error: %s" % reason)

        # set file log output format        
        try:
            fileHd = logging.FileHandler(filename)
            fileHd.setLevel(logging.INFO)
            fileHd.setFormatter(formatter)
            self.addHandler(fileHd)
        except Exception as reason:
            self.error("set file output error: %s" % reason)        

        """
        # set rotat handle
        try:
            rtfHandler = RotatingFileHandler(filename, maxBytes=10*1024*1024, backupCount=5)
            self.addHandler(rtfHandler)
        except Exception as reason:
            self.error("set rotat error: %s" % reason)
        """