'''
Created on 9 Jun 2017

@author: FGurkov1
'''
def largest_factor(n:int) -> int:
    f = 2
    while n != f:
        while n % f == 0 and n != f:
            print(n, f)
            n = n // f
        f = f + 1
    return n

if __name__ == '__main__':
    print(largest_factor(600851475143))