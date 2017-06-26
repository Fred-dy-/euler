'''
Created on 10 Jun 2017

@author: fgurkov1
'''
from typing import List

def find_path(matrix:List[List[int]]):
    row_iterator = reversed(matrix)
    previous_row = next(row_iterator)
    for row in row_iterator:
        for i in range(len(row)):
            row[i] += max(previous_row[i], previous_row[i + 1])
        previous_row = row
    return row[0]

def read_file(filename:str)->str:
    with open(filename, "r") as f:
        text = f.read()
        return text

if __name__ == '__main__':
    text = read_file("p067_triangle.txt")

    matrix = [[int(w) for w in line.split(" ")] for line in text.split("\n")]
    print(find_path(matrix))