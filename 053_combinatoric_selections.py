'''
Created on 26 Jul 2017

@author: fgurkov1
'''
from _collections import defaultdict

def count_selections(limit: int, boundary: int) -> int:
    previous = defaultdict(lambda: 0)
    current = defaultdict(lambda: 0)
    count = 0
    previous[0] = 1
    for i in range(1, limit + 1):
        current[0] = 1
        for j in range(1, i + 1):
            current[j] = previous[j - 1] + previous[j]
            if current[j] > boundary:
                count += 1
        previous, current = current, previous
    return count
            
            

if __name__ == '__main__':
    limit = 100
    boundary = 1000000
    print(count_selections(limit, boundary))