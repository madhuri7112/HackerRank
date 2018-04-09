#!/bin/python
#https://www.hackerrank.com/challenges/sherlock-and-cost
import sys

def cost(B):
    size = len(B)
    #l[i] = max cost of i elements where ith index is low
    L = [0] * size
    #h[i] = max cost of i elements where ith index is high
    H = [0] * size
    #m[i] = max cost with i elements
    max_cost = [0] * size
    L[0] = 0
    H[0] = 0
    max_cost[0] = max(L[0], H[0])
    
    for i in range(1, size):
        L[i] = max(L[i-1], H[i-1] + abs(B[i-1] - 1))
        H[i] = max(H[i-1] + abs(B[i] - B[i-1]), L[i-1] + abs(B[i] - 1))
        max_cost[i] = max(L[i], H[i])
    
    return max_cost[size -1]
    

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        arr = map(int, raw_input().strip().split(' '))
        result = cost(arr)
        print result

