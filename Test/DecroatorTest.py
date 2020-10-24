from Decorator.Mark import *

@logit
def Add(x, y):
    return x + y

if __name__ == '__main__':
    print(Add(1, 2))