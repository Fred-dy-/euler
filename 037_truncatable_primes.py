'''
Created on 24 Jul 2017

@author: fgurkov1
'''
from builtins import int
from typing import Set
from math import sqrt
from pprint import pprint

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True


def is_truncatable(candidate: int) -> bool:
    number = candidate
    mask = 10
    while mask < number:
        mask *= 10
    while number > 0:
        mask //= 10
        number = number % mask
        if number > 0 and not is_prime(number):
            return False
    return True


def truncatable_primes() -> Set[int]:
    truncatables = set()
    primes = set([2, 3, 5, 7])
    queue = list(primes)
    while queue:
        root = queue.pop()
        for d in range(1, 10):
            candidate = root * 10 + d
            if not candidate in truncatables:
                if is_prime(candidate):
                    queue.append(candidate)
                    if is_truncatable(candidate):
                        truncatables.add(candidate)
    return truncatables

if __name__ == '__main__':
    truncatables = truncatable_primes()
    pprint(truncatables)
    print(sum(truncatables))