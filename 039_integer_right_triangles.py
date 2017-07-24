'''
Created on 24 Jul 2017

@author: fgurkov1
'''
from pprint import pprint
from _collections import defaultdict
from math import sqrt

def squares(limit: int):
    p_map = defaultdict(lambda: 0)
    max_p = 0
    max_count = 0
    for c in range(2, limit // 2):
        for a in range(1, c):
            b = int(sqrt(c * c - a * a))
            if a >= b and a * a + b * b == c * c:
                p = a + b + c
                p_map[p] += 1
                if p_map[p] > max_count:
                    max_count = p_map[p]
                    max_p = p
    return (max_p, max_count)
                
if __name__ == '__main__':
    limit = 1000
    pprint(squares(limit))
