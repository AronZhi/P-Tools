from Decorator.Mark import *

@LogInterface
def Add(x, y):
    return x + y

if __name__ == '__main__':
    Add(1, 2)
    
    from LogComponent.LogMember import g_main_log
    SetPrintTool(g_main_log)
    Add(1, 2)