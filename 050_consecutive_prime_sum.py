'''
Created on 25 Jul 2017

@author: fgurkov1
'''
from math import sqrt
from typing import List, Tuple
from builtins import int
from pprint import pprint

def generate_primes(limit:int) -> List[int]:
    primes = []
    candidate = 2
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
        candidate = candidate + 1
    return primes

def find_longest_consecutive_sum(elements: List[int]) -> Tuple[int]:
    sum_up_to = []
    running_sum = 0
    for i in range(len(elements)):
        sum_up_to.append(running_sum)
        running_sum += elements[i]
    sum_up_to.append(running_sum)
    sum_limit = elements[len(elements) - 1]
    sum_length = 0
    sum_value = 0
    start_index = 0
    end_index = 0
    lookup = set(elements)
    for i in range(len(elements) - 1):
        for j in range(i + sum_length + 1, len(elements)):
            current_sum = sum_up_to[j + 1] - sum_up_to[i]
            if current_sum > sum_limit:
                break
            if current_sum in lookup:
                start_index, end_index, sum_length, sum_value = i, j, j - i + 1, current_sum
    return start_index, end_index, sum_length, sum_value

if __name__ == '__main__':
    limit = 1000000
    pprint(find_longest_consecutive_sum(generate_primes(limit)))