#!/bin/python3
#https://www.hackerrank.com/challenges/angry-children/
import sys

def angryChildren(k, arr, n):
    # Complete this function
    arr.sort()
    
    unfairness = arr[k-1] - arr[0]
    start = 1
    end = k
    while (end<n):
        unfairness = min(unfairness, arr[end] - arr[start])
        start+=1
        end += 1
        
    return unfairness
    

if __name__ == "__main__":
    n = int(input().strip())
    k = int(input().strip())
    arr = []
    arr_i = 0
    for arr_i in range(n):
       arr_t = int(input().strip())
       arr.append(arr_t)
    result = angryChildren(k, arr, n)
    print(result)
