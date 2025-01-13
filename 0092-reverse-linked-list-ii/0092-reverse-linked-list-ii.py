# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left==right:
            return head
        dummy=ListNode(0, head)

        leftprev=dummy

        curr=head # Started curr with head because in the for loop below we want to curr to exactly point at left and leftprev to 1 position before curr or left

        for travel in range(left-1):
            leftprev=curr
            curr=curr.next
        """
        This part is exactly same as the reverse linked list part (but for sublist inside a list)
        """
        prev=None

        for reverse in range(right - left + 1):
            nextpointer = curr.next
            curr.next = prev
            prev = curr
            curr = nextpointer
        
        leftprev.next.next = curr
        leftprev.next = prev

        return dummy.next
        
        

        