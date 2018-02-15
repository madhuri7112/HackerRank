#https://www.hackerrank.com/challenges/minimum-distances/submissions/code/64593587
#!/bin/python

import sys

def minimumDistances(nums):
    # Complete this function
    index_map = {}
    
    min_dist = len(nums) + 1
    for index, num in enumerate(nums):
        if num in index_map:
            prev_index = index_map[num]
            if (index - prev_index) < min_dist:
                min_dist = index - prev_index
        
        index_map[num] = index
                
    if min_dist == len(nums) + 1:
        return -1
    return min_dist

if __name__ == "__main__":
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    result = minimumDistances(a)
    print result

