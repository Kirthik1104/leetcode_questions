# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        res=head # Just stroring thr pointer to the head, not using anywhere in the loop. Useful for returning the head in the end

        while head and head.next:
            if head.val==head.next.val:
                head.next=head.next.next
            else:
                head=head.next
        return res