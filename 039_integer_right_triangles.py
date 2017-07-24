'''
Created on 24 Jul 2017

@author: fgurkov1
'''
from pprint import pprint


def count_triangles(p: int) -> int:
    count = 0
    
    for a in range(1, p // 2):
        for b in range(1, a):
            c = p - a - b
            if a * a + b * b == c * c:
                count += 1
    return count


if __name__ == '__main__':
    print(count_triangles(120))
    limit = 1000
    pprint(max([(count_triangles(p), p) for p in range (limit + 1)]))