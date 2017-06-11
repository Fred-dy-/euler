'''
Created on 9 Jun 2017

@author: FGurkov1
'''

def is_palindrome(n:int) -> bool:
    s = str(n)
    for i in range(0, len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

def brute_force(r1, r2):
    max_palindrome = -1
    for n1 in r1:
        for n2 in r2:
            product = n1 * n2
            if product > max_palindrome and is_palindrome(product):
                max_palindrome = product
    return max_palindrome

if __name__ == '__main__':
    print(brute_force(range(100, 1000), range(100, 1000)))
