from lib.logger import *
import time

output = Logger('log/')

output.log('hello')

def func():
    output.log('hello again')

func()
