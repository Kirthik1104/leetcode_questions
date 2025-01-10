# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0, head)
        first=dummy
        second=dummy

        for _ in range(n):
            second=second.next
        
        while second.next:
            first=first.next
            second=second.next
        
        first.next=first.next.next

        return dummy.next





















        
        # # dummy node is created to better deal with edge cases of removing first node, tail node.
        # dummy=ListNode(0, head)
        # first=dummy
        # second=dummy

        # for iterare in range(n+1): # n+1, because we are starting with dummy node
        #     second=second.next
        
        # while second is not None:
        #     second=second.next
        #     first=first.next
        
        # first.next=first.next.next
    
        # return dummy.next
