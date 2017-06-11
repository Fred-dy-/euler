'''
Created on 10 Jun 2017

@author: fgurkov1
'''
from typing import List
from pprint import pprint

'''
1000000...0000000(2) -> X(10)
'''

class BigInteger(object):
    
    def __init__(self, digits:List[int], base:int):
        self.digits = digits
        self.base = base
        
    def divide(self, divisor:int):
        result = BigInteger([], self.base)
        remainder = 0
        for digit in self.digits:
            remainder *= self.base
            remainder += digit
            result_digit = remainder // divisor
            remainder %= divisor
            result.digits.append(result_digit)
        return (result, remainder)

    def is_zero(self):
        for digit in self.digits:
            if digit != 0:
                return False
        return True

    def to_base(self, new_base:int):
        result = BigInteger([], new_base)
        number = self
        while not number.is_zero():
            number, remainder = number.divide(new_base)
            result.digits.insert(0, remainder)
        return result

if __name__ == '__main__':
    binary = BigInteger([int(d) for d in "1"+"0"*1000], 2)
    decimal = binary.to_base(10)
    pprint(sum(decimal.digits))