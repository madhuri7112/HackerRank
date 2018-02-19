#!/bin/python
#https://www.hackerrank.com/challenges/equal-stacks/problem
import sys


n1,n2,n3 = raw_input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = map(int,raw_input().strip().split(' '))
h2 = map(int,raw_input().strip().split(' '))
h3 = map(int,raw_input().strip().split(' '))

h1.reverse()
h2.reverse()
h3.reverse()

sum_1 = 0
sum_2 = 0
sum_3 = 0

sum_1 = sum(h1)
sum_2 = sum(h2)
sum_3 = sum(h3)

while((not(sum_1==sum_2==sum_3)) and sum_1!=0 and sum_2!=0 and sum_3!=0):
    
    max_sum = max(sum_1, sum_2, sum_3)
    if (sum_1 == max_sum):
        top_1 = h1.pop()
        sum_1 = sum_1 - top_1
    elif (sum_2 == max_sum):
        top_2 = h2.pop()
        sum_2 = sum_2 - top_2
    else:
        top_3 = h3.pop()
        sum_3 = sum_3 - top_3
        
if (sum_1 == sum_2 == sum_3):
    print sum_1
else:
    print '0'

