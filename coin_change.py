#https://www.hackerrank.com/challenges/coin-change/
#!/bin/python

import sys
# ways[coin_index][sum] = ways[coin_index - 1][sum] + ways[coin_index][sum - coins[coin_index]]
def getWays(target_sum, coins, num_coins):
    # Complete this function  
    for s in range(target_sum+1):
        if s - coins[0] < 0:
            ways[0][s] = 0
        elif s == coins[0]:
            ways[0][s] = 1
        else:
            ways[0][s] = ways[0][s - coins[0]]
    #print (ways)
    for coin_index in range(1, num_coins):
        for s in range(1, target_sum+1):
            if s - coins[coin_index] >= 0:
                ways[coin_index][s] = ways[coin_index - 1][s] + ways[coin_index][s - coins[coin_index]]
            else:
                ways[coin_index][s] = ways[coin_index - 1][s]
    return ways[num_coins-1][target_sum]
            
        

target_sum, num_coins = input().strip().split(' ')
target_sum, num_coins = [int(target_sum), int(num_coins)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = []
for index, coin in enumerate(c):
    ways.append([])
    for i in range(target_sum+1):
        ways[index].append(1)

print(getWays(target_sum, c, num_coins))
    

