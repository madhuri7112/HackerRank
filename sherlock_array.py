#!/bin/python
#https://www.hackerrank.com/challenges/sherlock-and-array/
import sys

def solve(nums):
    # Complete this function
    left_sum = []
    right_sum = []
    
    s = 0   
    for num in nums:
        s = s+num
        left_sum.append(s)
        
    s = 0
    for num in reversed(nums):
        s = s+num
        right_sum.append(s)
        
    right_sum.reverse()
        
    for i in range(len(left_sum)):
        if left_sum[i] == right_sum[i]:
            return "YES"
    
    return "NO"
      

T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    result = solve(a)
    print(result)

