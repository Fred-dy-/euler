'''
Created on 28 Jun 2017

@author: FGurkov1
'''
from typing import Set
from math import sqrt
from pprint import pprint

def is_prime(n: int) -> bool:
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True

def count_digits(n:int) -> int:
    d = 0
    while n > 0:
        n, d = n // 10, d + 1
    return d

def rotate(n:int) -> Set[int]:
    circle = set()
    digits = count_digits(n)
    for d in range(digits):
        r = n % 10
        n = n // 10 + r * 10 ** (digits - 1)
        circle.add(n)
    return circle

def find_circular_primes(limit: int) -> Set[int]:
    circular_primes = set()
    for n in range(2, limit):
        if (not n in circular_primes) and is_prime(n):
            circle = rotate(n)
            if all([is_prime(m) for m in circle]):
                circular_primes.update(circle)
    return circular_primes


if __name__ == '__main__':
    primes = find_circular_primes(1000000)
    pprint(primes)
    pprint(len(primes))