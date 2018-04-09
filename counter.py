#!/bin/python
#https://www.hackerrank.com/challenges/strange-code
import sys

def strangeCode(t):
    # Complete this function
    start_time = 1
    start_counter_value = 3
    while(1):
        end_time = start_time + start_counter_value - 1
        if t <= end_time:
            break
        start_time = end_time + 1
        start_counter_value = 2*start_counter_value
        
    val = start_counter_value - (t - start_time)
    
    return val
if __name__ == "__main__":
    t = long(raw_input().strip())
    result = strangeCode(t)
    print result
