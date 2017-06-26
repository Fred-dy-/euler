'''
Created on 26 Jun 2017

@author: FGurkov1
'''

powers = [d ** 5 for d in range(10)]

def check(n:int) -> bool:
    s = n
    while n > 0 and s > 0:
        d, n = n % 10, n // 10
        s -= powers[d] 
    return s == 0 and n == 0

def sum_to(limit:int) -> int:
    s = sum([x for x in range(2, limit) if check(x)])
    return s

if __name__ == '__main__':
    print(sum_to(300000))