'''
Created on 9 Jun 2017

@author: fgurkov1
'''
def triplet(tsum:int) -> int:
    for a in range(1, tsum):
        for b in range (1, a + 1):
            c = tsum - a - b
            if a**2 + b**2 == c**2:
                return a*b*c
            
if __name__ == '__main__':
    print(triplet(1000))            