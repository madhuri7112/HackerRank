#!/bin/python3
#https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem
import sys

def is_valid(r, c, n, m):
    if r >= 0 and r < n and c >= 0 and c < m:
        return True
    else:
        return False
    
def dfs(r, c, n, m, matrix):
    
    if not is_valid(r,c, n, m):
        return 0
    
    if matrix[r][c] == 0 or matrix[r][c] == 2:
        matrix[r][c] = 2
        return 0
    
    #Mark as visited
    matrix[r][c] = 2
    
    cnt = 1 + dfs(r-1, c-1, n, m, matrix) + dfs(r-1, c, n, m, matrix) + dfs(r-1, c+1, n, m, matrix) + dfs(r, c-1, n, m, matrix)  + dfs(r, c+1, n, m, matrix) + dfs(r+1, c-1, n, m, matrix) + dfs(r+1, c, n, m, matrix) + dfs(r+1, c+1, n, m, matrix)
       
    return cnt
    
def connectedCell(matrix, n, m):
    max_cnt = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                cnt = dfs(i, j, n, m, matrix)
                max_cnt = max(cnt, max_cnt)
    return max_cnt

if __name__ == "__main__":
    n = int(input().strip())
    m = int(input().strip())
    matrix = []
    for matrix_i in range(n):
        matrix_t = [int(matrix_temp) for matrix_temp in input().strip().split(' ')]
        matrix.append(matrix_t)
    result = connectedCell(matrix, n, m)
    print(result)
