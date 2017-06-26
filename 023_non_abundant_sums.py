'''
Created on 26 Jun 2017

@author: FGurkov1
'''
from math import sqrt
from typing import Set, List
from pprint import pprint

def abundant(n: int) -> bool:
    s = sum([i for i in range (1, int(n)) if n % i == 0])
    return s > n

def generate_abundant(limit: int) -> Set[int]:
    return {i for i in range(12, limit) if abundant(i)}

def non_abundant_sum(n:int, abundants:Set[int])->bool:
    for a in abundants:
        if a > n/2:
            return True
        if (n - a) in abundants:
            return False
    return True

def find_non_abundant_sums(limit: int)->List[int]:
    abundants = sorted(generate_abundant(limit))
    return [i for i in range(limit) if non_abundant_sum(i, abundants)]

if __name__ == '__main__':
    pprint([i for i in sorted(generate_abundant(28123))])
    
    print(sum(find_non_abundant_sums(28123)))