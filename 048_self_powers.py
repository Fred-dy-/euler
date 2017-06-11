'''
Created on 11 Jun 2017

@author: fgurkov1
'''
from builtins import int
from pprint import pprint

def self_power_mod(number:int, modulo:int) -> int:
    result = 1
    for i in range(number):
        result = (result * number) % modulo
    return result

if __name__ == '__main__':
    modulo = 10000000000
    '''
    pprint([self_power_mod(number, modulo) for number in range(1, 11)])
    '''
    print(sum([self_power_mod(number, modulo) for number in range(1, 1001)]) % modulo)