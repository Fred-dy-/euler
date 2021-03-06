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
    
    def to_int(self):
        result = 0
        for d in self.digits:
            result = result * self.base + d
        return result
    
    def to_str(self):
        return "".join([str(d) for d in self.digits])

class BigFibonacci(object):
    
    def __init__(self):
        self.f1 = BigInteger([1], 10)
        self.f2 = self.f1
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        return self.next()
        
    def next(self):
        result, self.f1, self.f2, self.index = self.f1, self.f2, self.f1.add(self.f2), self.index + 1
        return result, self.index

def find_long_fib(limit:int):
    for f, i in BigFibonacci():
        if len(f.digits) >= limit:
            return i
        
if __name__ == '__main__':
    print(find_long_fib(1000))