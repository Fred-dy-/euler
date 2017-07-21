'''
Created on 28 Jun 2017

@author: FGurkov1
'''
from _collections import defaultdict
'''
0 1
1 1
2 1+1, 2
3 1+1+1, 1+2
4 1+1+1+1, 1+1+2, 2+2

largest coin
value    1    2    5    10    20    50    100    200
0        0    0    0    0    0    0    0    0
1        1    0    0    0    0    0    0    0
2        1    2    0    0    0    0    0    0
3        1    2    0    0    0    0    0    0
4        1    3    0    0    0    0    0    0
5        1    3    4    0    0    0    0    0
6        1    


'''
def count_coin_sums(n: int) -> int:
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    coin_sets = defaultdict(lambda: 0)
    coin_sets[0] = 1
    
    for coin in coins:
        for value in range(coin, n + 1):
            coin_sets[value] += coin_sets[value - coin]
    return coin_sets[n]

if __name__ == '__main__':
    print(count_coin_sums(200))