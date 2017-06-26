'''
Created on 26 Jun 2017

@author: FGurkov1
'''
from builtins import int

def faulhaber_sum(d:int) -> int:
    """ n is the number of the square with the size of the side equal to d """
    n = (d - 1) / 2
    """ the sum of the numbers in the corners of the nth square is
    16n^2 + 4x + 4
    Using Faulhaber's formula (https://en.wikipedia.org/wiki/Faulhaber%27s_formula) for each of the powers 
    and adding 1 for the innermost square we get the below"""
    return 16 * (2*n**3 + 3*n**2 + n) / 6 + 4 * (n**2 + n) / 2 + 4 * n + 1

if __name__ == '__main__':
    print(faulhaber_sum(1001))