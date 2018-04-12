#!/bin/python3
#https://www.hackerrank.com/challenges/count-luck/problem
import sys
start_point_char = "M"
end_point_char = "*"
tree_char = "X"
visited_char = "-"
blank_char = "."

def find_starting_point(matrix, n, m):
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == start_point_char:
                return i,j

def is_valid(i, j, n, m):
    if i>=0 and i<n and j>=0 and j<m:
        return True
    else:
        return False
    
def find_path(matrix, n, m, i, j):
    
    if not is_valid(i, j, n, m):
        return []
    
    if matrix[i][j] == tree_char or matrix[i][j] == visited_char: 
        return []
    
    if matrix[i][j] == end_point_char:
        return [(i,j)]
 
    matrix[i][j] = visited_char
    
    right_path = find_path(matrix, n, m, i, j+1)
    left_path = find_path(matrix, n, m, i, j-1)
    top_path = find_path(matrix, n, m, i-1, j)
    bottom_path = find_path(matrix, n, m, i+1, j)
    
    if len(right_path)!= 0:
        right_path.append((i,j))
        
        return right_path
    
    if len(left_path)!= 0:
        left_path.append((i,j))
        
        return left_path
    
    if len(top_path)!= 0:
        top_path.append((i,j))
        
        return top_path
    
    if len(bottom_path)!= 0:
        bottom_path.append((i,j))
        
        return bottom_path
    
    return []

def is_path_possible_to(matrix, x, y, n, m):
    if (is_valid(x, y, n, m) and (matrix[x][y] == blank_char or matrix[x][y] == visited_char or matrix[x][y] == end_point_char)):
        return True
    else:
        return False
    
    
def countLuck(matrix, n, m, k):
    # Complete this function
    start_x, start_y = find_starting_point(matrix, n, m)
    path = find_path(matrix, n, m, start_x, start_y)
    path.reverse()
    wand_waves = 0
           
    for index, coord in enumerate(path[:-1]):
        x, y = coord[0] ,coord[1]
        
        #This is num of paths for which wand wave is not required
        if index == 0:
            path_threshold = 1
        else:
            #If it is not starting point, then one cell backward from which we came is possible too
            path_threshold = 2
        #check if there are more than 1 possible paths from this cell
        cnt = 0
        if (is_path_possible_to(matrix, x+1, y, n, m)):
            cnt += 1
        if (is_path_possible_to(matrix, x-1, y, n, m)):
            cnt += 1
        if (is_path_possible_to(matrix, x, y-1, n, m)):
            cnt += 1
        if (is_path_possible_to(matrix, x, y+1, n, m)):
            cnt += 1
            
        if cnt>path_threshold:
            wand_waves += 1
    if wand_waves == k:
        print ("Impressed")
    else:
        print ("Oops!")
    
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n, m = input().strip().split(' ')
        n, m = [int(n), int(m)]
        matrix = []
        matrix_i = 0
        for matrix_i in range(n):
           matrix_t = list(str(input().strip()))
           matrix.append(matrix_t)
        k = int(input().strip())
        countLuck(matrix, n, m, k)
