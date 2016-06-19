import time

def getCurrentTime():
    # return '[' + time.strftime("%d/%m/%Y %H:%M:%S") + '] '
    return '[16/5/2016 3:45:20] '

class Logger:
    
    def __init__(self, path):
        self.file = open(path, 'w')
        
    def log(self, text):
        self.file.write(getCurrentTime() + '[log] ' + text + '\n')
    
    def warn(self, text):
        self.file.write(getCurrentTime() + '[warn] ' + text + '\n')
        
    def err(self, text):
        self.file.write(getCurrentTime() + '[error] ' + text + '\n')