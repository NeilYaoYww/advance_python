# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 14:28:27 2017

@author: Weiwei
"""

import abc
import datetime

dt_str = datetime.datetime.now().strftime('Y-%m-%d %H:%M')

class WriteFile(object):
    
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def write(self):
        return
    
    def __init__(self, filename):
        self.filename = filename
    
    def write_line(self, text):
        fh = open(self.filename, 'a')
        fh.write(text + '\n')
        fh.close()

class LogFile(WriteFile):
    
    def
        
class DelimFile(WriteFile):
    
    
open('test.txt', 'w')

w1