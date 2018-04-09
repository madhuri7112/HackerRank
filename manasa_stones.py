#!/bin/python
#https://www.hackerrank.com/challenges/manasa-and-stones/
import sys

def stones(n, a, b):
    # Complete this function
    d1 = min(a,b)
    d2 = max(a,b)
    
    poss_values = []
    #num diffrences is n-1
    for i in range(0, n):
        val = (n-1-i)*d1 + (i)*d2
        poss_values.append(val)
    
    poss_values = list(set(poss_values))
    return sorted(poss_values)

if __name__ == "__main__":
    T = int(raw_input().strip())
    for a0 in xrange(T):
        n = int(raw_input().strip())
        a = int(raw_input().strip())
        b = int(raw_input().strip())
        result = stones(n, a, b)
        print " ".join(map(str, result))



