#!/bin/python
#https://www.hackerrank.com/challenges/non-divisible-subset/problem
import sys

def nonDivisibleSubset(k, arr):
    # Complete this function
    mod_frequency_map = {}
    for m in range(k):
        mod_frequency_map[m] = 0
    for num in arr:
        mod_num = num%k       
        mod_frequency_map[mod_num] = mod_frequency_map[mod_num] + 1
    max_count = 0   
    #print mod_frequency_map
    for m in range(k):
      if (m!=0 and 2*m != k):
        #print m, k-m
        max_count = max_count + max(mod_frequency_map[m], mod_frequency_map[k-m])
        
    #Since we double add:  (m, k-m) && (k-m, m)
    max_count = max_count/2
    
    if mod_frequency_map[0]!=0:
        max_count = max_count +1
        
    if k%2 == 0 and mod_frequency_map[k/2]!=0:
        max_count = max_count +1
        
    return max_count

if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = map(int, raw_input().strip().split(' '))
    result = nonDivisibleSubset(k, arr)
    print result

