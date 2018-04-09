#!/bin/python
#https://www.hackerrank.com/challenges/pylons/
import sys

def pylons(k, arr):
    size = len(arr)
    index = 0
    count = 0
    possible_index = None
    while (index < size):
        light_index = None
        span = 0       
        while (span < k):
            
            if (index + span) >= size:
                return count +1
            if arr[index + span] == 1:
                light_index = index + span
            span+=1
            
        if not light_index:
            if not possible_index:
                return -1
            else:
                light_index = possible_index
                       
        possible_index = None
        for i in range(light_index+1, light_index + k + 1):
            
            if i<size and arr[i] == 1:
                possible_index = i
                
        index = light_index + k 
        count = count + 1
    
    return count

if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = map(int, raw_input().strip().split(' '))
    result = pylons(k, arr)
    print result
