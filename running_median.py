#!/bin/python3
#https://www.hackerrank.com/challenges/find-the-running-median/
import os
import sys
from  heapq import *
#
# Complete the runningMedian function below.
#
def runningMedian(nums):
    #
    # Write your code here.
    #
    more_minhp = []
    less_maxhp = []
    median = None
    medians = []
    for index, num in enumerate(nums):
        
        if index == 0:
            median = num
            medians.append(float(median))
            heappush(more_minhp, num)
            continue
        
        cnt_more = len(more_minhp)
        cnt_less = len(less_maxhp)
        
        if cnt_more == cnt_less:
            
            if num >= median:
                heappush(more_minhp, num)
                median = more_minhp[0]
            else:
                heappush(less_maxhp, -1 * num)
                median = -1 * less_maxhp[0]
                
        elif cnt_more > cnt_less:
            
            if num >= median:
                top = heappop(more_minhp)
                heappush(less_maxhp, -1 * top)
                heappush(more_minhp, num)
                
            else:
                heappush(less_maxhp, -1 * num)
            #print (more_minhp[0], less_maxhp[0])
            median = float(more_minhp[0] + -1*less_maxhp[0])/2
        
        elif cnt_more < cnt_less:
            
            if num < median:
                top = -1*heappop(less_maxhp)
                heappush(more_minhp, top)
                heappush(less_maxhp, -1 * num)
                
            else:
                heappush(more_minhp, num)
            #print (more_minhp[0], less_maxhp[0])
            median = float(more_minhp[0] + -1*less_maxhp[0])/2
        
        medians.append(float(median))
        
    return medians
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
