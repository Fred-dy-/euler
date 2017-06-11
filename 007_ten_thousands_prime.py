'''
Created on 9 Jun 2017

@author: fgurkov1
'''
from math import sqrt

def prime(n:int) -> int:
    primes = []
    candidate = 2
    while len(primes) < n:
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
    return primes[n - 1]

if __name__ == '__main__':
    print(prime(10001))