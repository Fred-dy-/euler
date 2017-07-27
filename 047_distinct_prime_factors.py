'''
Created on 26 Jul 2017

@author: fgurkov1
'''
from math import sqrt

def find_distinct(count: int) -> int:
    primes = [2]
    prime_set = set(primes)
    candidate = 3
    first_number = 0
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
            prime_set.add(candidate)
            first_number = 0
        else:
            number = candidate
            factors = 0
            for p in primes:
                divisible = False
                while number % p == 0:
                    divisible, number = True, number // p
                if divisible:
                    factors += 1
                if number in prime_set:
                    factors += 1
                    break
                if number == 1:
                    break
            if factors == count:
                if candidate - first_number > count:
                    first_number = candidate
                elif candidate - first_number + 1 == count:
                    return first_number
            else:
                first_number = 0
        candidate = candidate + 1

if __name__ == '__main__':
    for count in range (2, 5):
        print(find_distinct(count))