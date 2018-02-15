//https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/copy-from/64854588
/*
Detect a cycle in a linked list. Note that the head pointer may be 'null' if the list is empty.

A Node is defined as: 
    class Node {
        int data;
        Node next;
    }
*/

boolean hasCycle(Node head) {
     if (head == null || head.next == null || head.next.next == null) {
         return false;
     }
    
    Node slow_ptr = head;
    Node fast_ptr = head.next.next;
    
    while (fast_ptr.next != null && fast_ptr.next.next != null) {
        
        if (slow_ptr == fast_ptr) {
            return true;
        }
        fast_ptr = fast_ptr.next.next;
        slow_ptr = slow_ptr.next;       
    }
    
    return false;
    
    
}

