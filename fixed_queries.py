#https://www.hackerrank.com/challenges/queries-with-fixed-length/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
def getResult(nums, d):
    
    left_max = []
    lm = nums[0]
    for i,num in enumerate(nums):
        if(i!=0 and i%d == 0):
            lm = nums[i]
        if (num>lm):
            lm = num
        left_max.append(lm)
    right_max = []
    rm = nums[-1]
    
    for i,num in reversed(list(enumerate(nums))):
        if((i+1)%d == 0):
            rm = nums[i]
        if(num>rm):
            rm = num
        right_max.append(rm)
    right_max.reverse()
    
    min_of_max_k = max(right_max[0], left_max[d-1])
    i=0
    while(d+i-1<len(nums)):
        max_k = max(right_max[i], left_max[d+i-1])
        min_of_max_k = min(min_of_max_k, max_k)
        i+=1
        
    return min_of_max_k
        

def main():
    n,q = map(int,raw_input().strip().split(" "))
    nums = map(int,raw_input().strip().split(" "))
    while(q):
        print getResult(nums, input())
        q-=1
    
main()
