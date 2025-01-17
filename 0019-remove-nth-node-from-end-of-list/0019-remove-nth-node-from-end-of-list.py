# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy=ListNode(0, head)
        curr=dummy
        prev=dummy

        for iterate in range(n):
            curr=curr.next
        
        while curr.next:
            curr=curr.next
            prev=prev.next
        
        prev.next=prev.next.next
        return dummy.next























#         #dummynode with value 0, and next is pointing to head, check the ListNode constructor
#         dummy=ListNode(0, head)
#         first=dummy    
#         second=dummy

#         # Move the second pointer by n steps
#         for _ in range(n):
#             second=second.next
        
#        # Start moving each node ahead by 1 position, the first pointer will stop 1 node before the n node which has to be removed
#         # the second pointer will stop exactly before the none
#         while second.next:
#             first=first.next
#             second=second.next
        
#         # skip the nth node
#         first.next=first.next.next

#         # return the head
#         return dummy.next





















        
#         # # dummy node is created to better deal with edge cases of removing first node, tail node.
#         # dummy=ListNode(0, head)
#         # first=dummy
#         # second=dummy

#         # for iterare in range(n+1): # n+1, because we are starting with dummy node
#         #     second=second.next
        
#         # while second is not None:
#         #     second=second.next
#         #     first=first.next
        
#         # first.next=first.next.next
    
#         # return dummy.next
