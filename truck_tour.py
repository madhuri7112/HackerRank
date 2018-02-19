# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/truck-tour/problem
    
    
def get_index(surplus):
    
    if (len(surplus) == 1):
        return 0

    start = 0
    end = 0
    sum = surplus[start]
    finished = 1
    total = len(surplus)
    moved_start = 0
    
    while (finished != total) :
        
        
        if (sum >=0) :
            #Move only end pointer
            end = (end+1)%total
            sum = sum + surplus[end]
            finished = finished + 1
        else:
            
            if (start == end):
                #Move end pointer
                end = (end + 1)%total
                sum = sum + surplus[end]
                finished = finished + 1
            
            #Move start pointer
            sum = sum - surplus[start]
            start = (start+1)%total
            finished = finished - 1
            moved_start = 1
            
        
        if (start == 0 and moved_start ==1):
            break
    
    if (finished == total):
        return start
    else: 
        return -1
    
def main():
    num = input()
    
    #This is array of the surplus petrol at every stop
    surplus = []
    while(num):
        inp = raw_input().strip().split(" ")
        surplus.append(int(inp[0]) - int(inp[1]))
        num = num -1 
    #print surplus    
    print get_index(surplus)
        
main()
    
