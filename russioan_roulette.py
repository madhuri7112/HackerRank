#https://www.hackerrank.com/contests/w36/challenges/revised-russian-roulette/submissions/code/1305607389
#!/bin/python

import sys

def revisedRussianRoulette(doors):
    # Complete this function
    max_ops = 0
    min_ops = 0
    for index, door in enumerate(doors):
        if door == 0:
            continue
        if door == 1:
            
            if index==len(doors) - 1:
                min_ops = min_ops + 1
                max_ops = max_ops + 1
            else:
                if doors[index+1] == 1:
                    min_ops = min_ops + 1
                    max_ops = max_ops + 2
                    doors[index+1] = 0
                    doors[index] = 0
                else:
                    min_ops = min_ops + 1
                    max_ops = max_ops + 1
                    doors[index] = 0
                   
    return min_ops, max_ops
    
                    
            

if __name__ == "__main__":
    n = int(raw_input().strip())
    doors = map(int, raw_input().strip().split(' '))
    result = revisedRussianRoulette(doors)
    print " ".join(map(str, result))

