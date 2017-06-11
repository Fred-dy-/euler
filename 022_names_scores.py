'''
Created on 11 Jun 2017

@author: fgurkov1
'''
from typing import List
import csv
from pprint import pprint
from builtins import int

def read_names(filename:str)->List[str]:
    with open(filename, "r") as f:
        reader = csv.reader(f)
        names = next(reader)
    return names
        

def score(name:str) -> int:
    return sum([ord(c) - ord('A') + 1 for c in name])


def count_sum_of_scores(names: List[str]) -> int:
    names.sort()
    total = 0
    for i in range(len(names)):
        total += (i + 1) * score(names[i])
    return total
    
if __name__ == '__main__':
    names = read_names("p022_names.txt")
    pprint(count_sum_of_scores(names))
    