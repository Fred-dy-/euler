'''
Created on 26 Jun 2017

@author: FGurkov1
'''

def count_distinct(r1: range, r2: range):
    distinct ={a ** b for a in r1 for b in r2}
    return len(distinct)

if __name__ == '__main__':
    print(count_distinct(range(2, 101), range(2, 101)))