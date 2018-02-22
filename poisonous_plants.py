#!/bin/python

import sys

def poisonousPlants(p):
    # Complete this function
    stack = []
    #stack.append((p[0],0))
    maxDaysAlive = 0
    for index, psn in enumerate(p):
        daysAlive = 0
        while len(stack)!=0 and psn <= stack[-1][0]:
            daysAlive = max(daysAlive, stack.pop()[1])
        
        if (len(stack) == 0):
            daysAlive = 0
        else:
            daysAlive = daysAlive + 1
            
        maxDaysAlive = max(maxDaysAlive, daysAlive)
        stack.append((psn,daysAlive))
        
    return maxDaysAlive

if __name__ == "__main__":
    n = int(raw_input().strip())
    p = map(int, raw_input().strip().split(' '))
    result = poisonousPlants(p)
    print result

