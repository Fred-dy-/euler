'''
Created on 11 Jun 2017

@author: fgurkov1
'''
from _collections import defaultdict
from builtins import int
from pprint import pprint

cache = defaultdict(lambda:0)

def sum_of_divisors(number:int) -> int:
    result = cache[number]
    if result == 0:
        for d in range(1, number):
            if number % d == 0:
                result += d
        cache[number] = result
    return result

def is_amicable(number:int, limit:int) -> bool:
    candidate = sum_of_divisors(number)
    return candidate != number and sum_of_divisors(candidate) == number

def sum_amicables(limit:int):
    return sum([number for number in range(1, limit) if is_amicable(number, limit)])

if __name__ == '__main__':
    limit = 10000
    print(sum_amicables(limit))