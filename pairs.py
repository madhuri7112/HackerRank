#!/bin/python
#https://www.hackerrank.com/challenges/pairs/
import sys

def pairs(k, arr):
    # Complete this function
    arr.sort()
    diff_array = []
    for index, a in enumerate(arr):
        if index == 0:
            continue
        diff_array.append(a - arr[index - 1])
    #print diff_array  
    start_index = 0
    end_index = 0
    count = 0
    sum_nums = diff_array[0]
    
    while (end_index < len(diff_array)):
        if sum_nums == k:
            count += 1
            
        if sum_nums >= k:
            
            if start_index == end_index:
                
                end_index = end_index + 1
                if (end_index == len(diff_array)):
                    return count
                else:
                    sum_nums = sum_nums + diff_array[end_index]
        
            else:
                
                sum_nums = sum_nums - diff_array[start_index]
                start_index += 1
        else:
            if start_index == end_index:
                
                end_index = end_index + 1
                if (end_index == len(diff_array)):
                    return count
                else:
                    sum_nums = sum_nums + diff_array[end_index]
            else:
                
                end_index = end_index + 1
                if (end_index == len(diff_array)):
                    return count
                else:
                    sum_nums = sum_nums + diff_array[end_index]
        
    return count
    

if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = map(int, raw_input().strip().split(' '))
    result = pairs(k, arr)
    print result
