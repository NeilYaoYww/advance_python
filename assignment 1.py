# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 17:27:04 2017

@author: Weiwei
"""


class MaxSizeList(object):
    def __init__(self, value):
        self.max_list_size = value
        self.lis = []

    
    def push(self, item):
        self.lis.append(item)
        if len(self.lis) > self.max_list_size:
            self.lis.pop(0)
    
    def get_list(self):
        return (self.lis)

A = MaxSizeList(2)
A.push('Hey')
A.push('how')
A.push('are')
A.push('you')
print(A.get_list())

