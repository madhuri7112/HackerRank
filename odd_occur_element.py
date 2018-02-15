#https://www.hackerrank.com/contests/crescent-practice-3rd-years/challenges/find-the-unique-one/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
def main():
    num_tc = input()
    
    for i in range(num_tc):
        len = input()
        input_array = map(int, raw_input().strip().split(' '))
        print "Case "+str(i+1)+": "+str(find_num_odd_occurances(input_array))
        
    
def find_num_odd_occurances(input_array):
    freq = {}
    for num in input_array:
        if num in freq:
            freq[num] = freq[num]+1
        else:
            freq[num] = 1
            
    for num in freq:
        if freq[num]%2!=0:
           return num
        
main()
