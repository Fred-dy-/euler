'''
Created on 28 Jul 2017

@author: fgurkov1
'''
from math import sqrt

'''

a+b = c
b+d = a
b = a-d

2a - d = c

a-b = d

b, d < a

'''
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
        return n * (3 * n - 1) // 2 == v

    @staticmethod
    def pentagonal(n: int) -> int:
        return n * (3 * n - 1) // 2

def solve() -> int:
    pentagonals = set([Pentagonal.pentagonal(i) for i in range (1, 1000000)])
    index_b = 2
    while True:
        b = Pentagonal.pentagonal(index_b)
        for index_d in range(1, index_b + 1):
            d = Pentagonal.pentagonal(index_d)
            a = b + d
            if a in pentagonals:
                if (a + b) in pentagonals:
                    return d
                elif (a + d) in pentagonals:
                    return b 
        index_b += 1
    

if __name__ == '__main__':
    print(solve())