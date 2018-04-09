#https://www.hackerrank.com/challenges/beautiful-pairs
#!/bin/python

import sys

def beautifulPairs(n, A, B):
    # Complete this function
    l1hash = {}
    for num in A:
        if num in l1hash:
            l1hash[num] += 1
        else:
            l1hash[num] = 1
    
    count = 0
    for num in B:
        if num in l1hash and l1hash[num]!=0:
            count +=1
            l1hash[num]-=1
    
    if (count == n):
        return count -1
    else:
        return count+1

if __name__ == "__main__":
    n = int(raw_input().strip())
    A = map(int, raw_input().strip().split(' '))
    B = map(int, raw_input().strip().split(' '))
    result = beautifulPairs(n, A, B)
    print result
