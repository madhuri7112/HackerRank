import sys

def toys(wts):
    # Complete this function
    wts.sort()
    count = 0
    i = 0
    while(i<len(wts)):
        min_wt = wts[i]
        
        while(i < len(wts) and wts[i] <= min_wt + 4):
            i += 1
        count = count + 1
        
    return count
        
    

if __name__ == "__main__":
    n = int(raw_input().strip())
    w = map(int, raw_input().strip().split(' '))
    result = toys(w)
    print result
    
