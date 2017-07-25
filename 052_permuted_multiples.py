'''
Created on 25 Jul 2017

@author: fgurkov1
'''
from euler.utils.numbers import Number

def find_multiples() -> int:
    number = 0
    while True:
        number = number + 1
        digits = Number.to_digits(number)
        found = True
        for factor in range(2, 7):
            multiple = number * factor
            md = Number.to_digits(multiple)
            if not (all(d in digits for d in md) and all(d in md for d in digits)):
                found = False
                break
        if found:
            return number
            

if __name__ == '__main__':
    print(find_multiples())