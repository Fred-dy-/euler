'''
Created on 27 Jun 2017

@author: FGurkov1
'''
from builtins import int
from math import sqrt

def is_prime(a:int, b:int, i:int) -> bool:
    n = abs(i * i + a * i + b)
    for d in range(2, int(sqrt(n))):
        if n % d == 0:
            return False
    return True 

def count_primes(a: int, b: int) -> int:
    i = 0
    while is_prime(a, b, i):
        i += 1
    return i

if __name__ == '__main__':
    print(max([{'product': a * b, 'count': count_primes(a, b)} for a in range (-999, 1000) for b in range (-1000, 1001)], key=lambda p: p['count']))