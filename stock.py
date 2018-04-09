#!/bin/python3
#https://www.hackerrank.com/challenges/stockmax/
import sys

def stockmax(prices):
    # Complete this function
    max_right = 0
    profit = 0
    for price in reversed(prices):
        max_right = max(max_right, price)
        if price < max_right:
            profit = profit + (max_right - price)
    return profit    
    
    

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        prices = list(map(int, input().strip().split(' ')))
        result = stockmax(prices)
        print(result)
