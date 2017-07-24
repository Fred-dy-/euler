'''
Created on 24 Jul 2017

@author: fgurkov1
'''
from pprint import pprint
from _functools import reduce

'''
length numbers digits
0     1
1     9    10
2    90    180
3   900
'''

def champernowne_digit(index: int) -> int:
    length = 1
    number_count = 9
    digit_count = 10
    while index >= digit_count:
        index -= digit_count
        length += 1
        number_count *= 10
        digit_count = number_count * length
    number_index = index // length
    number = number_index
    if length > 1:
        number += pow(10, length - 1)
    digit_index = length - index % length - 1
    digit = number % 10
    while digit_index > 0:
        number //= 10
        digit = number % 10
        digit_index = digit_index - 1
    return digit


if __name__ == '__main__':
    limit = 6
    print(champernowne_digit(15))
    pprint([champernowne_digit(pow(10, n)) for n in range(limit + 1)])
    pprint(reduce(lambda x, y: x * y, [champernowne_digit(pow(10, n)) for n in range(limit + 1)]))