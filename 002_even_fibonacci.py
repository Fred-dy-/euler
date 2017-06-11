'''
Created on 9 Jun 2017

@author: FGurkov1
'''
from builtins import int
from pprint import pprint

class fibonacci(object):
    def __init__(self, limit:int):
        self.limit = limit
        self.previous = 0
        self.current = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        return self.next()
    
    def next(self):
        if self.current < self.limit:
            result, self.previous, self.current = self.current, self.current, self.previous + self.current
            return result
        else:
            raise StopIteration()

if __name__ == '__main__':
    pprint(sum([f for f in fibonacci(4000000) if f % 2 == 0]))