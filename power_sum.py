#https://www.hackerrank.com/challenges/the-power-sum
#!/bin/python

import sys

def powerSum(num, power, min_int):
    
    if (num == 0):
        return 1
    
    if (num<0):
        return 0
    
    ways = 0
    i = min_int
    
    while (i**power<=num):
        ways = ways + powerSum(num - i**power, power, i+1)
        i = i+1
    
    
    return ways
    
    
if __name__ == "__main__":
    X = int(raw_input().strip())
    N = int(raw_input().strip())
    result = powerSum(X, N, 1)
    print result
