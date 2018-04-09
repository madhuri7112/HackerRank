#https://www.hackerrank.com/challenges/queue-using-two-stacks
#Enter your code here. Read input from STDIN. Print output to STDOUT
def push(stack, num):
    stack.append(num)
    
    return stack

def pop(stack):
    last = stack[-1]
    stack.pop()
    
    return last

def top(stack):
    return stack[-1]
 
stack_1 = []
stack_2 = []
queue = []

def enqueue(num):
    push(stack_1, num)
    
    return stack_1
    
def dequeue():
    
    if len(stack_2)==0:       
        while (len(stack_1)!=0):
            el = stack_1.pop()
            push(stack_2, el)
    
    topel = pop(stack_2)
    
def printFirst():
    
    if len(stack_2)==0:
         
        while (len(stack_1)!=0):
            el = stack_1.pop()
            push(stack_2, el)
    
    topel = top(stack_2)
    print topel
    
    
        
def main():
    n = input()
    while (n!=0):
        inp = raw_input()
        if (len(inp.strip().split(' ')) == 2):
            q, num = map(int, inp.strip().split(' '))
            enqueue(num)
        else:
            q = int(inp)
            if (q ==2):
                dequeue()
            else:
                printFirst()
        n = n-1
    
main()
