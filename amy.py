# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/contests/crescent-practice-3rd-years/challenges/amy-and-coins/copy-from/1305458530
def main():
    num_tc = input()
    for tc in range(num_tc):
        len = input()
        inp = map(int, raw_input().strip().split(' '))
        print "Case "+str(tc+1)+": "+str(find_max_coins(inp))
    
    
def find_max_coins(inp):
    #max_coins = []
    if (len(inp) == 1):
        return inp[0]
    elif (len(inp) == 2):
        return max(inp)
    
    max_coins_prev_2 = inp[0]
    max_coins_prev = max(inp[0], inp[1])
    
    for num in inp[2:]:
        max_coins = max(max_coins_prev, max_coins_prev_2+num)
        max_coins_prev_2 = max_coins_prev
        max_coins_prev = max_coins
        
    return max_coins

main()
