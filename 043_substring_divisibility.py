'''
Created on 26 Jul 2017

@author: fgurkov1
'''
from euler.utils.numbers import Number
from euler.utils.permutations import LexPerm
from builtins import int
from typing import List
from pprint import pprint

def is_substring_divisible(number:int, factors: List[int], startIndex: int) -> bool:
    digits = list(reversed(Number.to_digits(number)))
    for i in range(len(factors)):
        candidate = Number.from_digits(digits[startIndex + i:startIndex + i + 3])
        if candidate % factors[i] != 0:
            return False
    return True

if __name__ == '__main__':
    factors = [2, 3, 5, 7, 11, 13, 17]
    startIndex = 1
    substring_divisible = [number for number in [Number.from_digits(digits) for digits in LexPerm(range(10))] if is_substring_divisible(number, factors, startIndex)]
    pprint(substring_divisible)
    print(sum(substring_divisible))