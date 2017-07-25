'''
Created on 25 Jul 2017

@author: fgurkov1
'''
from typing import Set, List

def digits() -> Set[int]:
    return set(range(1, 10))


def digitsOf(p) -> List[int]:
    digits = list()
    while p > 0:
        d = p % 10
        digits.append(d)
        p //=10
    return digits


def find_pandigital() -> Set[int]:
    products = set()
    n = [None] * 5
    d0 = digits()
    for n[0] in d0:
        d1 = set(d0)
        d1.remove(n[0])
        for n[1] in d1:
            d2 = set(d1)
            d2.remove(n[1])
            for n[2] in d2:
                d3 = set(d2)
                d3.remove(n[2])
                for n[3] in d3:
                    d4 = set(d3)
                    d4.remove(n[3])
                    for n[4] in d4:
                        d5 = set(d4)
                        d5.remove(n[4])
                        a = n[0] * 10 + n[1]
                        b = n[2] * 100 + n[3] * 10 + n[4]
                        p = a * b
                        pd = digitsOf(p)
                        if len(pd) == 4 and all(d in d5 for d in pd) and all(d in pd for d in d5):
                            print(f"Found {a} * {b} = {p}")
                            products.add(p)
                        a = n[0]
                        b = n[1] * 1000 + n[2] * 100 + n[3] * 10 + n[4]
                        p = a * b
                        pd = digitsOf(p)
                        if len(pd) == 4 and all(d in d5 for d in pd) and all(d in pd for d in d5):
                            print(f"Found {a} * {b} = {p}")
                            products.add(p)
                        
    return products

if __name__ == '__main__':
    print(sum(find_pandigital()))