#https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/submissions/code/64659925

"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def FindMergeNode(headA, headB):
    
    if (not headA) or (not headB):
        return None
    
    tempA = headA
    tempB = headB
    lenA = 0
    lenB = 0
    
    while tempA.next:
       
        lenA = lenA+1
        tempA = tempA.next
    while tempB.next:
        
        lenB = lenB + 1
        tempB = tempB.next
    
     
    if (lenA > lenB):
        larger_list_head = headA
        smaller_list_head = headB
        diff = lenA - lenB
    else:
        larger_list_head = headB
        smaller_list_head = headA
        diff = lenB - lenA
        
    while diff:
        
        larger_list_head = larger_list_head.next
        diff = diff-1
        
    while larger_list_head != smaller_list_head :
        larger_list_head = larger_list_head.next
        smaller_list_head = smaller_list_head.next
    
    if (smaller_list_head != larger_list_head):
        return None
    else:
        return larger_list_head.data
