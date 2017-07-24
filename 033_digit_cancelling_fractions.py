'''
Created on 25 Jul 2017

@author: fgurkov1
'''
from builtins import int
from typing import List, Tuple
from pprint import pprint

def find_fractions() -> List[Tuple[int]]:
    fractions = list()
    for denominator in range(2, 10):
        for nominator in range (1, denominator):
            for digit in range(1, 10):
                f = cancelling(nominator, denominator, digit)
                if f:
                    fractions.append(f)
    return fractions

def cancelling(nominator, denominator, digit) -> Tuple[int]:
    d1 = denominator * 10 + digit
    p1 = nominator * d1
    if p1 % denominator == 0 and p1 // denominator < 100:
        n1 = p1 // denominator
        nd1, nd2 = n1 // 10, n1 % 10
        if nd1 == nominator and nd2 == digit or nd1 == digit and nd2 == nominator:
            return (n1, d1, nominator, denominator)
    d1 = digit * 10 + denominator
    p1 = nominator * d1
    if p1 % denominator == 0 and p1 // denominator < 100:
        n1 = p1 // denominator
        nd1, nd2 = n1 // 10, n1 % 10
        if nd1 == nominator and nd2 == digit or nd1 == digit and nd2 == nominator:
            return (n1, d1, nominator, denominator)
    return
                
if __name__ == '__main__':
    print(cancelling(4, 8, 9))
    pprint(find_fractions())
    '''
    This print the four fractions, the actual answer needs implementation of lcm/gcd, which I have already done elsewhere...
    '''