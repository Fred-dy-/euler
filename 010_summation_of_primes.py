'''
Created on 9 Jun 2017

@author: fgurkov1
'''
from math import sqrt
from typing import List
def prime(limit:int) -> List[int]:
    primes = []
    candidate = 2
    while candidate < limit:
        index = 0
        root = int(sqrt(candidate))
        is_prime = True
        print(f"Considering {candidate}")
        while index < len(primes) and primes[index] <= root:
            if candidate % primes[index] == 0:
                print(f"Candidate {candidate} is divisible by {primes[index]}")
                is_prime = False
                break
            index = index + 1
        if is_prime:
            primes.append(candidate)
            print(f"Candidate {candidate} is a prime number {len(primes)}")
        candidate = candidate + 1
    return primes

if __name__ == '__main__':
    print(sum(prime(2000000)))