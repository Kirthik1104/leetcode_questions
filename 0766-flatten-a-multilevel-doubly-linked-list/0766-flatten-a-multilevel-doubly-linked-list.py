"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        dummy=Node(0)
        prev=dummy
        stack=[head]

        # Use iterative DFS technique using a stack
        while stack:
            curr=stack.pop()  # Pop the stack and assign it to curr
            """
            O-------->1------->2
            0--------<1------->2  
            Prev   curr
            dummy
            """
            prev.next=curr # point prev to point to curr node
            curr.prev=prev # point curr.prev to point to prev node
             
            if curr.next:  # check if next val exist
                stack.append(curr.next)  # first append the next val of curr then append child, then child will be popped before next (LIFO)--> As per question
            if curr.child: # check if child node exists of current node, 
                stack.append(curr.child) # Add it to the top of the stack, so that child node can be processed first before next node ( as per question)
                curr.child=None # Set child pointer to None as per the problem
            
            
            prev=curr #After asiging the curr prev pointer to previous and previous next pointer to curr. We update the prev to curr. Prev moves ahead with new curr all the time

            """
            O-------->1------->2
            0--------<1------->2  
            dummy   curr
            """
            # Dummy was always at 0, we need to detach it from 1, because 1's previous is pointing to 0. dummy.next is 1, its previous is set to None
        dummy.next.prev=None   

        return dummy.next



        