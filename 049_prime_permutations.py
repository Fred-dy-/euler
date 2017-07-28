'''
Created on 27 Jul 2017

@author: fgurkov1
'''
from typing import List
from math import sqrt
from euler.utils.numbers import Number
from euler.utils.permutations import LexPerm

def generate_primes(limit:int) -> List[int]:
    primes = [2]
    candidate = 3
    while candidate < limit:
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
        candidate = candidate + 2
    return primes

def find_sequences():
    result = list()
    primes = generate_primes(10000)
    primes = [p for p in primes if p > 1000]
    prime_set = set(primes)
    for p in primes:
        if p not in prime_set:
            continue
        digits = Number.to_digits(p)
        count = 0
        sequence = list()
        for permutation in LexPerm(digits, unique=True):
            number = Number.from_digits(permutation)
            if number in prime_set:
                sequence.append(number)
                count += 1
                prime_set.remove(number)
        if count >= 3:
            for s in LexPerm(sequence, 3):
                if s[1] > s[0] and s[1] - s[0] == s[2] - s[1]:
                    result.append(''.join(map(str, s)))
    return result

if __name__ == '__main__':
    print(find_sequences())