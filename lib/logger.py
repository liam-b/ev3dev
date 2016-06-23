import time
import inspect

def callerName(skip = 2):
    stack = inspect.stack()
    start = 0 + skip
    if len(stack) < start + 1:
      return ''
    parentframe = stack[start][0]

    name = []
    module = inspect.getmodule(parentframe)
    if module:
        name.append(module.__name__)

    if 'self' in parentframe.f_locals:
        name.append(parentframe.f_locals['self'].__class__.__name__)
    codename = parentframe.f_code.co_name
    if codename != '<module>':
        name.append( codename )
    del parentframe
    if inspect.stack()[1][3] == '__init__':
        return '[init()]'
    final = '[' + ".".join(name) + '()]'
    return final.replace('_', '')

def getCurrentTime():
    return '[' + time.strftime("%d/%m/%Y %H:%M:%S") + '] '

def getCurrentFileTime():
    return time.strftime("%d:%m:%Y %H:%M:%S")

class Logger:

    def __init__(self, path):
        self.file = open(path + '/' + getCurrentFileTime() + '.log', 'w')
        self.file.write(getCurrentTime() + callerName() + ' ' + '[log] ' + 'new log started' + '\n')

    def log(self, text):
        self.file.write(getCurrentTime() + callerName() + ' ' + '[log] ' + text + '\n')

    def warn(self, text):
        self.file.write(getCurrentTime() + callerName() + ' ' + '[warn] ' + text + '\n')

    def err(self, text):
        self.file.write(getCurrentTime() + callerName() + ' ' + '[error] ' + text + '\n')
