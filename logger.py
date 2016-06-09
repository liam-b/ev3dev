from time import strftime, sleep

def getCurrentTime():
    return '[' + strftime("%d/%m/%Y %H:%M:%S") + '] '

class Logger:
    
    def __init__(self, path):
        self.file = open(path, 'w')
        
    def log(self, text):
        self.file.write(getCurrentTime() + '[log] ' + text + '\n')
    
    def warn(self, text):
        self.file.write(getCurrentTime() + '[warn] ' + text + '\n')
        
    def err(self, text):
        self.file.write(getCurrentTime() + '[error] ' + text + '\n')