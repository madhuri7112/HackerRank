#!/bin/python3
#https://www.hackerrank.com/challenges/bigger-is-greater/
import sys

def biggerIsGreater(strng):
    # Complete this function
    strng = list(strng)
    l = len(strng)
    first_unmatch_index = -1
    for i in range(l-2, -1, -1):
        if strng[i]  < strng[i+1]:
            first_unmatch_index = i
            
            break
    if (first_unmatch_index == -1):
        return "no answer"
    
    target_index = -1
    for i in range(first_unmatch_index+1, l):
         if strng[i] > strng[first_unmatch_index]:
                target_index = i
    temp = strng[first_unmatch_index]
    strng[first_unmatch_index] = strng[target_index]
    strng[target_index] = temp
    
    res = strng[0:first_unmatch_index+1] + sorted(strng[first_unmatch_index+1:])
        
    return "".join(res)
            
        
if __name__ == "__main__":
    T = int(input().strip())
    for a0 in range(T):
        w = input().strip()
        result = biggerIsGreater(w)
        print(result)
