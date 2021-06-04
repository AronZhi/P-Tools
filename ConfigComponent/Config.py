import yaml

class Config(object):
    def __init__(self, path):
        fread = open(path, 'r', encoding='utf-8')
        config = yaml.safe_load(fread.read())
        self.__dict__.update(config)

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getattr__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]
        raise None
