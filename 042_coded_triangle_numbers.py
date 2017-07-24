'''
Created on 24 Jul 2017

@author: fgurkov1
'''
from typing import List
import csv
from math import sqrt

def read_words(filename:str)->List[str]:
    with open(filename, "r") as f:
        reader = csv.reader(f)
        names = next(reader)
    return names

def triangle(word):
    value = sum([ord(c) - ord('A') + 1 for c in word])
    v2 = value * 2
    sr = sqrt(v2)
    return v2 == int(sr) * (int(sr) + 1)

if __name__ == '__main__':
    words = read_words("p042_words.txt")

    count = sum([1 for word in words if triangle(word)])
    print(count)
    
    
'''
n * n + n - 2 * v = 0  
'''