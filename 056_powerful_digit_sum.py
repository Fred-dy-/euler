'''
Created on 26 Jul 2017

@author: fgurkov1
'''

if __name__ == '__main__':
    print(max(sum(map(int, str(a**b))) for a in range(100) for b in range(100)))