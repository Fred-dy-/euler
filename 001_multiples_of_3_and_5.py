'''
Created on 9 Jun 2017

@author: FGurkov1
'''

def count_multiples(limit: int) -> int:
    return sum([n for n in range (1, limit) if n % 3 == 0 or n % 5 == 0])

if __name__ == '__main__':
    print(count_multiples(1000))