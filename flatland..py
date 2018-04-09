#https://www.hackerrank.com/challenges/flatland-space-stations
#!/bin/python3

import sys

def flatlandSpaceStations(n, stations):
    # Complete this function
    stations.sort()
    
    size = len(stations)
    
    if size == 1:
        return max(n-1-stations[0], stations[0] - 0)
    diff = stations[1] - stations[0]
    for i in range(1,size-1):
        diff = max(diff, stations[i] - stations[i-1])
    
    diff = max(int(diff/2), n-1 - stations[size-1], stations[0])
    
    return int(diff)

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    c = list(map(int, input().strip().split(' ')))
    result = flatlandSpaceStations(n, c)
    print(result)
