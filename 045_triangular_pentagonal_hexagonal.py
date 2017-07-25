'''
Created on 25 Jul 2017

@author: fgurkov1
'''
from math import sqrt
from pprint import pprint
import sys

class Hexagonal(object):

    def __init__(self, start = 1):
        self.index = start
        
    def __iter__(self):
        return self
    
    def __next__(self):
        return self.next()
    
    def next(self):
        index = self.index
        self.index += 1
        return index * (2 * index - 1)

class Triangular(object):
    
    @staticmethod
    def is_triangular(v: int) -> int:
        '''
        n (n+1) / 2 = v
        n^2 + n - 2v = 0
        D = 1 + 8v
        n = (-1 + sqrt(D)) / 2
        '''
        n = int((sqrt(8*v + 1) - 1) / 2)
        if n * (n + 1) // 2 == v:
            return n
        else:
            return -1

class Pentagonal(object):
    
    @staticmethod
    def is_pentagonal(v: int) -> int:
        '''
        n (3n-1) / 2 = v
        3n^2 - n - 2v = 0
        D = 1 + 24v
        n = (1 + sqrt(D)) / 6
        '''
        n = int((sqrt(24*v + 1) + 1) / 6)
        if n * (3 * n - 1) // 2 == v:
            return n
        else:
            return -1 

if __name__ == '__main__':
    for v in Hexagonal(166):
        p = Pentagonal.is_pentagonal(v)
        if p > 0:
            print(f'Found next pentagonal number [{p}]: {v}')
            t = Triangular.is_triangular(v)
            if t > 0:
                print(f'Found next triangular number [{t}]: {v}')
                pprint((t, p, v))
                sys.exit()