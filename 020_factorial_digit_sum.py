'''
Created on 10 Jun 2017

@author: fgurkov1
'''

from typing import List

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

    def add(self, other):
        if self.base != other.base:
            other = other.to_base(self.base)
        result = BigInteger([], self.base)
        carry = 0
        max_position = max([len(self.digits), len(other.digits)])
        for i in range(1, max_position + 1):
            d1 = len(self.digits) >= i and self.digits[len(self.digits) - i]
            d2 = len(other.digits) >= i and other.digits[len(other.digits) - i]
            s = d1 + d2 + carry
            d = s % self.base
            carry = s // self.base
            result.digits.insert(0, d)
        if carry > 0:
            result.digits.insert(0, carry)
        return result
            
    def multiply(self, factor):
        result = BigInteger([], self.base)
        carry = 0
        for d in reversed(self.digits):
            product = d * factor + carry
            pd = product % self.base
            carry = product // self.base
            result.digits.insert(0, pd)
        while carry > 0:
            pd = carry % self.base
            carry //= self.base
            result.digits.insert(0, pd)
        return result
    
def factorial(n: int):
    f = BigInteger([1], 10)
    for i in range(2, n + 1):
        f = f.multiply(i)
    return f

if __name__ == '__main__':
    print(sum(factorial(100).digits))