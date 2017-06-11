'''
Created on 11 Jun 2017

@author: fgurkov1
'''
from typing import List
from tkinter.constants import CURRENT
from pprint import pprint

class LexPerm(object):
    
    def __init__(self, elements:List):
        self.elements = elements
        self.elements.sort()
        self.current = self.elements
        self.stacks = []
        for i in len(self.elements):
            self.stacks[i] = self.elements[i:]

    def __iter__(self):
        return self
    
    def __next__(self):
        return self.next()
    
    def next(self):
        result = self.current
        self.permutate()
        return result

perm_count = 0

def permutate(elements:List, previous:List, limit:int):
    global perm_count
    if perm_count >= limit:
        return
    if len(elements) == 0:
        perm_count += 1
        if perm_count == limit:
            pprint(previous)
            return
    else:
        for i in range(len(elements)):
            permutate(elements[0:i] + elements[i+1:], previous + [elements[i]], limit)
        
if __name__ == '__main__':
    permutate([i for i in range(10)], [], 1000000)