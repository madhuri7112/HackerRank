#!/bin/python3
#https://www.hackerrank.com/challenges/greedy-florist/
import sys

def getMinimumCost(n, k, c):
    # Complete this function
    c.sort(reverse=True)
    total_price = 0
    bought = 0
    factor = 0
    flower_index = 0
    while (bought!=n):
        if (bought%k ==0):
            factor += 1
        total_price = total_price + factor*c[flower_index]
        flower_index+=1
        bought+=1
        
    return total_price

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
c = list(map(int, input().strip().split(' ')))
minimumCost = getMinimumCost(n, k, c)
print(minimumCost)
