'''
Created on 9 Jun 2017

@author: fgurkov1
'''

def diff(n: int):
    square_of_the_sum = sum([i for i in range(1, n + 1)]) ** 2
    sum_of_the_squares = sum([i**2 for i in range(1, n + 1)])
    return square_of_the_sum - sum_of_the_squares

if __name__ == '__main__':
    print(diff(100))