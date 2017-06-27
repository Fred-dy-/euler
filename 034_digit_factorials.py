'''
Created on 27 Jun 2017

@author: FGurkov1
'''
from typing import List
from pprint import pprint

def generate_factorials(limit: int) -> List[int]:
    f = [1, 1]
    for i in range (2, limit):
        f.append(f[i-1] * i)
    return f

def is_digit_factorial(n: int, factorials: List[int]) -> bool:
    s = n
    while n > 0 and s > 0:
        d, n = n % 10, n // 10
        s -= factorials[d]
    
    return s == 0 and n == 0

if __name__ == '__main__':
    factorials = generate_factorials(10)
    pprint(factorials)
    digit_factorials = [n for n in range (3, 3628800) if is_digit_factorial(n, factorials)]
    pprint(digit_factorials)
    s = sum(digit_factorials)
    print(s)