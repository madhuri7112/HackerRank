#!/bin/python3
#https://www.hackerrank.com/challenges/cavity-map

import sys

def is_cavity(i,j,grid,n):
    if i==0 or i == n-1:
        return False
    if j == 0 or j == n-1:
        return False
    curr = grid[i][j]
    
    if curr > grid[i][j-1] and curr > grid[i][j+1] and curr > grid[i-1][j] and curr > grid[i+1][j]:
        return True
    
    return False
    
def cavityMap(grid, n):
    # Complete this function
    cpy = []
    for i in range(n):
        cpy.append([0]*n)
    for i in range(n):
        for j in range(n):
            cpy[i][j] = grid[i][j]
    
    for i in range(n):
        for j in range(n):
            if (is_cavity(i, j, grid, n)):
                cpy[i][j] = "X"
            else:
                cpy[i][j] = grid[i][j]
                
    for i in range(n):
        str1 = ''.join(str(e) for e in cpy[i])
        print (str1)
            
    

if __name__ == "__main__":
    n = int(input().strip())
    grid = []
    grid_i = 0
    for grid_i in range(n):
       grid_t = str(input().strip())
       grid.append(grid_t)
    result = cavityMap(grid, n)
    


