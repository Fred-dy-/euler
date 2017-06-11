'''
Created on 11 Jun 2017

@author: fgurkov1
'''
from typing import List
from pprint import pprint
from _collections import defaultdict

class State(object):
    
    def __init__(self):
        self.elements = []
        self.i = 0

class LexPerm(object):
    
    def __init__(self, elements:List):
        self.elements = list(elements)
        self.elements.sort()
        self.current = list(elements)
        self.states = defaultdict(lambda:State())
        self.reset_state(0, self.elements)
        self.has_more = True

    def __iter__(self):
        return self
    
    def __next__(self):
        return self.next()
    
    def next(self):
        if not self.has_more:
            raise StopIteration()
        else:
            self.has_more = not self.permutate(0)
            return self.current

    def permutate(self, position:int):
        state = self.states[position]
        if len(state.elements) == 0:
            return True
        self.current[position] = state.elements[state.i]
        if self.permutate(position + 1):
            state.i += 1
            if state.i == len(state.elements):
                return True
            next_state_elements = state.elements[0:state.i] + state.elements[state.i + 1:]
            self.reset_state(position + 1, next_state_elements)
        return False

    def reset_state(self, position, elements):
        for i in range(len(elements) + 1):
            next_state = self.states[position + i]
            next_state.i = 0
            next_state.elements = elements[i:]

if __name__ == '__main__':
    permutator = LexPerm([d for d in range(10)])
    for i in range(1000000):
        permutation = next(permutator)
    pprint("".join([str(element) for element in permutation]))