'''
Created on 25 Jul 2017

@author: fgurkov1
'''
from builtins import int
from euler.utils.numbers import Number
from typing import Tuple

def find_biggest() -> Tuple[int]:
    max_pandigital = 0
    max_i = 0
    for i in range (1, 10000):
        digits = []
        factor = 1
        while len(digits) < 9:
            digits.extend(reversed(Number.to_digits(i * factor)))
            factor += 1
        if len(digits) == 9 and all(d in digits for d in range(1, 10)):
            pandigital = Number.from_digits(digits)
            if pandigital > max_pandigital:
                max_pandigital = pandigital
                max_i = i
    return max_pandigital, max_i
            

if __name__ == '__main__':
    print(find_biggest())