#!/bin/python3
#https://www.hackerrank.com/challenges/fraudulent-activity-notifications
import sys
from bisect import * 
def find_median(sorted_arr, d):
    
    if d%2 != 0:
        return float(sorted_arr[int(d/2)])
    else: 
        return float(sorted_arr[int(d/2)] + sorted_arr[int(d/2) -1])/2
    
def activityNotifications(expenditures, d):
    # Complete this function
#     freq = {}
#     for i in range(201):
#         freq[i] = 0
#     cnt = 0
#     for i in range(d):
#         freq[expenditures[i]] += 1
    
    
#     start = 0
#     end = d-1
    
#     while end<len(expenditures)-1:
#         median = find_median(freq, d)
        
#         end = end+1
#         #print (median, expenditures[end])
#         if (expenditures[end] >= 2*median):
#             cnt+=1
        
#         #updating freq map
#         freq[expenditures[end]] += 1
#         freq[expenditures[start]] -= 1
#         start = start + 1
    
#     return cnt
    d_window = []
    for i in range(d):
        d_window.append(expenditures[i])
      
    d_window.sort()
    end_index = d-1
    start_index = 0
    cnt = 0
    while end_index < len(expenditures)-1:
        median = find_median(d_window, d)
        
        end_index = end_index + 1
        if (expenditures[end_index] >= 2*median):
             cnt+=1
        rem_idx = bisect(d_window, expenditures[start_index])
        del d_window[rem_idx-1]
        insort(d_window, expenditures[end_index])
        start_index = start_index + 1
      
    return cnt


if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    expenditures = list(map(int, input().strip().split(' ')))
    result = activityNotifications(expenditures, d)
    print(result)
