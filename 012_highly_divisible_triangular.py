'''
Created on 10 Jun 2017

@author: fgurkov1
'''
from math import sqrt
from builtins import int

class TriangularNumber(object):
    
    def __init__(self):
        self.n = 1
        self.t = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        return self.next()
        
    def next(self):
        self.t += self.n
        self.n += 1
        return self.t

def count_divisors(number):
    count = 0 
    s = int(sqrt(number))
    for d in range(1, s + 1):
        if number % d == 0:
            count += 2
    if number % s == 0:
        count -= 1
    return count

def find_first(limit:int):
    triangular = TriangularNumber()
    for t in triangular:
        if count_divisors(t) >= limit:
            return t

if __name__ == '__main__':
    print(find_first(500))