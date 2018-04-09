#!/bin/python
#https://www.hackerrank.com/challenges/common-child/
import sys

def commonChild(s1, s2):
    # Complete this function
    lcs = []
    m = len(s1)
    n = len(s2)
    
    for i in range(m):
        lcs.append([0]*n)
        
    for i in range(m):
        if (s2[0] == s1[i]):
            lcs[i][0] = 1 
        else:
            lcs[i][0] = lcs[i-1][0]
            
    for i in range(n):
        if (s2[i] == s1[0]):
            lcs[0][i] = 1
        else:
            lcs[0][i] = lcs[0][i-1]
    
    
    for i in range(1,m):
        for j in range(1,n):
            if s1[i] == s2[j]:
                lcs[i][j] = 1 + lcs[i-1][j-1]
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
    
    return lcs[m-1][n-1]

s1 = raw_input().strip()
s2 = raw_input().strip()
result = commonChild(s1, s2)
print(result)
