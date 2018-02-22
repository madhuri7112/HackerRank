#!/bin/python

import sys

def maxSum(arr):
    max_sub

def maxSubarray(arr):
    # Complete this function
    max_subarr_so_far = arr[0]
    max_ending = []
    max_ending_here = 0
    max_subseq = 0
    max_num = arr[0]
    ispos = False
    for index, num in enumerate(arr):
        if (num>=0):
            ispos = True
            max_subseq = max_subseq + num
        if (num>max_num):
            max_num = num
        if (num < max_ending_here + num):
            max_ending_here = max_ending_here + num
        else:
            max_ending_here = num
        max_ending.append(max_ending_here)
        max_subarr_so_far = max(max_ending_here, max_subarr_so_far)
    
    if (not ispos):
        max_subseq = max_num
        
    return max_subarr_so_far, max_subseq

def maxSubseq(arr):
    
    max_sum = []
    max_sum_sofar = arr[0]
    
    for index, num in enumerate(arr):
        max_sum_ending_here = num
        for i in range(index):
            max_sum_ending_here = max(max_sum[i]+num, max_sum_ending_here)
        max_sum.append(max_sum_ending_here)
        max_sum_sofar = max(max_sum_ending_here, max_sum_sofar)
        
    return max_sum_sofar

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        arr = map(int, raw_input().strip().split(' '))
        result1, result2 = maxSubarray(arr)
        # = maxSubseq(arr)
        #print " ".join(map(str, result))
        print result1, result2




