'''
Created on 9 Jun 2017

@author: fgurkov1
'''
from typing import Iterable
from builtins import int

def smallest_multiple(collection:Iterable[int]) -> int:
    factors = []
    for number in collection:
        print(f"Processing {number}")
        for factor in factors:
            if number % factor == 0:
                number = number // factor
        factor = 2
        print(f"After reduction = {number}")
        while number != 1:
            while number % factor == 0:
                number = number // factor
                factors.append(factor)
                print(f"Adding new factor {factor}. Reducing to {number}")
            factor = factor + 1
    product = 1
    print(f"All factors {factors}")
    for factor in factors:
        product = product * factor
    return product

if __name__ == '__main__':
    print(smallest_multiple(range(1, 21)))