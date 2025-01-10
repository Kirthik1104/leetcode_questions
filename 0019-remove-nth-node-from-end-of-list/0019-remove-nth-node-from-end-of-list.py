# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        first = dummy
        second = dummy
        
        # Move second pointer `n+1` steps ahead to maintain a gap of `n`
        for _ in range(n + 1):
            second = second.next
        
        # Move both pointers until second reaches the end
        while second:
            first = first.next
            second = second.next
        
        # Remove the nth node from the end
        first.next = first.next.next
        
        # Return the updated list starting from the real head
        return dummy.next
        