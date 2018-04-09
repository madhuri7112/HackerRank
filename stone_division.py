#!/bin/python3
#https://www.hackerrank.com/challenges/stone-division-2/
import sys



def stoneDivision(n, s, max_divisions):

    if n in max_divisions:
        return max_divisions[n]
    else:
        max_div = 0
        for divisor in s:
            if (divisor>=n):
                continue
            if (divisor!=0 and n%divisor == 0):
                dividend = int(n/divisor)
                max_div = max(max_div, 1+ (dividend* stoneDivision(divisor, s, max_divisions)))
        max_divisions[n] = int(max_div)
        
        return int(max_div)
    
if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, m = input().strip().split(' ')
        n, m = [int(n), int(m)]
        s = list(map(int, input().strip().split(' ')))
        max_divisions = {}      
        result = stoneDivision(n, s, max_divisions)
        print(result)
