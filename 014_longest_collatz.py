'''
Created on 10 Jun 2017

@author: fgurkov1
'''
from _collections import defaultdict

cache = defaultdict(lambda: -1)

def collatz(number: int):
    if number % 2 == 0:
        return number //2
    else:
        return 3 * number + 1

def collatz_length(number: int):
    if number == 1:
        return 1
    if cache[number] == -1:
        next_number = collatz(number)
        length = collatz_length(next_number) + 1
        cache[number] = length
    return cache[number]

def find_longest(limit:int):
    max_length = 0
    starting_number = -1
    for number in range(1, limit):
        length = collatz_length(number)
        print(number, length)
        if max_length < length:
            starting_number, max_length = number, length
    return starting_number, max_length

if __name__ == '__main__':
    print(find_longest(1000000))