'''
Created on 26 Jul 2017

@author: fgurkov1
'''
from math import sqrt

def find_composite() -> int:
    primes = [2]
    candidate = 3
    while True:
        index = 0
        root = int(sqrt(candidate))
        is_prime = True
        while index < len(primes) and primes[index] <= root:
            if candidate % primes[index] == 0:
                is_prime = False
                break
            index = index + 1
        if is_prime:
            primes.append(candidate)
        else:
            conjecture = False
            for p in primes:
                remainder = (candidate - p) // 2
                if int(sqrt(remainder)) ** 2 == remainder:
                    conjecture = True
                    break
            if not conjecture:
                return candidate
        candidate = candidate + 2


if __name__ == '__main__':
    print(find_composite())