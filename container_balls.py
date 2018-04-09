#!/bin/python3
#https://www.hackerrank.com/challenges/organizing-containers-of-balls
import sys

def organizingContainers(container, n):
    # Complete this function
    container_count = []
    for cont in container:
        container_count.append(sum(cont))
    balls_type_count = [0] * n
    for cont in container:
        for i in range(n):
            balls_type_count[i] += cont[i]
    container_count.sort()
    balls_type_count.sort()
    
    for index, c in enumerate(container_count):
        if c!=balls_type_count[index]:
            return False
        
    return True
    

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n = int(input().strip())
        container = []
        for container_i in range(n):
           container_t = [int(container_temp) for container_temp in input().strip().split(' ')]
           container.append(container_t)
        result = organizingContainers(container, n)
        if result:
            print ("Possible")
        else:
            print ("Impossible")
        
