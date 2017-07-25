'''
Created on 25 Jul 2017

@author: fgurkov1
'''
from typing import List

class Number(object):
    '''
    Number utility functions
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        pass
    
    @staticmethod
    def from_digits(digits: List[int], radix:int = 10):
        number = 0
        for digit in digits:
            number = number * radix + digit
        return number
    
    @staticmethod
    def to_digits(number:int, radix:int = 10) -> List[int]:
        digits = list()
        while number > 0:
            digits.append(number % radix)
            number //= radix
        return digits
    
    
