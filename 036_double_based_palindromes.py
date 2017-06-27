'''
Created on 27 Jun 2017

@author: FGurkov1
'''

def is_palindrome(n:int, b:int) -> bool:
    s1 = n
    s2 = 0
    while n > 0:
        n, s2 = n // b, s2 * b + (n % b)
    return s1 == s2

if __name__ == '__main__':
    print(sum([n for n in range(1000000) if is_palindrome(n, 10) and is_palindrome(n, 2)]))
